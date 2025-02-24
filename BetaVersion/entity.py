import Maap
from vector import *
from Interface import *
from Resources import *
from Pace import *
from formatting import *

class Player(Maap.Entity):

    # command data
    # command data fetching is analogous to using enums--
    # e.g.  "up" has an index of 0 in commands.
    #       hence its input is command_inputs[0] = 'w',
    #       and its cost is command_costs[0] = 1.
    commands = (
        "up",
        "down",
        "left",
        "right",
    )

    command_inputs = (
        'w',
        's',
        'a',
        'd'
    )

    command_costs = (
        1,
        1,
        1,
        1
    )

    _coords = None  # coordinates relative to player's domain.
    _score  = 0     # calculated based on player's performance.
    name    = "Joseph R. Biden, the 46th President of the United States" # for highscore bookkeeping.
    tokens  = 0     # in-game currency.

    def __init__(self, domain, tokens: int, command_costs: tuple = None):
        self.new_level(domain, tokens)
        if command_costs:
            self.command_costs = command_costs
    
    # to move player into a new map, its data has to be updated.
    def new_level(self, domain, tokens):
        self.domain     = domain            # map entity is residing in.
        self.displaced  = Maap.FreeSpace()  # game object player is standing on, replaced by player.
        self._coords    = None
        self.coords     = Vector(domain.startpoint) # coordinates.
        self.tokens     = tokens
        self.turn       = 1

    @property
    def coords(self) -> Vector:
        return self._coords

    @coords.setter
    def coords(self, value: Vector):
        if self.domain.CanAccess(value):
            destination = self.domain.data[value.y][value.x]
            match type(destination):
                case Maap.Coin:
                    # collect coin
                    gain = destination.value
                    self.tokens += gain
                    self.domain.data[value.y][value.x] = Maap.FreeSpace() # coin collected, coin becomes free space
                    self.just_set_coords(value)
                    
                    # feedback
                    print(f"Gained {gain} tokens!")
                    short_pause()
                case Maap.Tunnel:
                    # enter tunnel
                    price = destination.price
                    if self.tokens >= price:
                        print(f"Where shall <{self.Display()}> go?")
                        tunnels, proposals = self.print_environment(visualize_tunnels=True)
                        self.just_set_coords(Vector(tunnels[int(prompt(proposals)) - 1])) # teleportation
                        self.tokens -= price # payment
                    else:
                        print(f"Insufficient tokens to go through tunnel!\nTunnel costs: {self.tokens} TOKEN(S)")
                        short_pause()
                case Maap.Box:
                    # push box
                    if destination.be_pushed(value - self.coords):
                        self.coords = value # move to the same spot again, with recursion
                case _:
                    self.just_set_coords(value)
    
    @property
    def score(self):
        return self._score
    
    def tally_score(self):
        self._score += self.tokens

    # returns True if player moves successfully.
    def move(self, by: tuple):
        last = self.coords.to_tuple()
        self.coords = self.coords + Vector(by)
        return not self.coords.to_tuple() == last
    
    def move_dir(self, code: str, steps: int = 1): # accepts 'u', 'd', 'l', 'r' (each represents a 2D direction)
        return self.move(direction(code) * steps)
    
    # prints the map the player is in.
    def print_environment(self, visualize_tunnels = False):
        INCR, INTV = 3, 5 # increment length, intervals at which numbres are displayed
        width_indicator = [' '] * (self.domain.width + 5)
        tunnels, tunnel_proposals, tunnel_count = [], {}, 0
        for i in (ii*INTV for ii in range(self.domain.width // INTV + 1)):
            for j, c in enumerate(str(i)):
                width_indicator[i+j] = c
        print(' '*(INCR+1) + ''.join(width_indicator))
        for i in range(self.domain.height):
            lline = ("{:>" + str(INCR) + "} ").format(str(i)) if i % INTV == 0 else " "*(INCR+1)
            rline = ""
            for j, data in enumerate(self.domain.data[i]):
                disp = data.Display()
                def annotate(msg):
                    nonlocal rline
                    rline += f"<<[x={j}, {msg}]"
                match data.__class__.__name__:
                    case "Player":
                        annotate("You")
                    case "Tunnel":
                        annotate(f"{APPEARANCES['Tunnel']}:-{data.price}T")
                        if visualize_tunnels:
                            tunnel_count += 1
                            tunnels.append(data.coords)
                            tunnel_proposals[str(tunnel_count)] = f"Goto {data.coords}"
                            disp = ansi_format(str(tunnel_count), Format.purple)
                    case "Coin":
                        annotate(f"{APPEARANCES['Coin']}:+{data.value}T")
                lline += disp
            print(lline, rline)
        if visualize_tunnels:
            return tunnels, tunnel_proposals # assets for tunnelling.
        return

    def use_command(self, command_num: int):
        command, cost = self.commands[command_num], self.command_costs[command_num]
        assert command in self.commands, f"Command not found!\nAvailable commands: {commands}" # for safety.
        if self.tokens >= cost:
            if command in ("up", "down", "left", "right"):
                code = (
                    'u',
                    'd',
                    'l',
                    'r'
                )
                if self.move_dir(code[command_num]):
                    self.tokens -= cost
                else:
                    print(ansi_format("bump", Format.italic))
                    short_pause()
            else:
                print("Insufficient tokens!")
                short_pause()
    
    # prints all the info you need about the player and the environment its in.
    def info(self):
        print('\n' * 10)

        # display screen
        self.print_environment()
            
        # display player statistics
        print()
        fancy_bar(f"TURN {self.turn}", length=self.tokens, start_from=1)
        print(f"{ansi_format('OPERATOR:', Format.bold)} {self.name}")
        print(f"{ansi_format('SUBJECT', Format.bold)} <{self.Display()}> x={self.coords.x}, y={self.coords.y}")
        print(f"{ansi_format('TOKENS:', Format.bold)} {self.tokens}")
        fancy_bar(length=self.tokens)
    
    # runs a frame of the gameplay loop. returns a command for run_level.
    def run_frame(self):
        if self.coords.to_tuple() == self.domain.endpoint:
            return "Next Map"
        elif self.tokens <= 0:
            return "End Game"
        else:
            self.info()
            
            # curates a list of usable commands.
            proposals, i = {}, 1
            for i in range(len(self.commands)):
                command, inp, cost = self.commands[i], self.command_inputs[i], self.command_costs[i]
                proposals[inp] = f"Use command <{command.upper()}>\t--{cost} TOKEN(S)"
                i += 1

            proposals['o'] = "Options..."
            
            received = prompt(proposals).lower()
            if received in self.command_inputs:
                self.use_command(self.command_inputs.index(received))
                self.turn += 1
            elif received == 'o':
                opt = options()
                if opt == 'n':
                    return self.instantiate_frame()
                return opt
            return "None"

