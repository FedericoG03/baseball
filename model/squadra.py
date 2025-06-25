from dataclasses import dataclass

@dataclass
class Squadra:
    ID: int
    teamCode: str
    name: str

    def __hash__(self):
        return hash(self.ID)

    def __eq__(self, other):
        return self.ID == other.ID
