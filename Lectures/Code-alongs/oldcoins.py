class OldCoinStash:
    def __init__(self, owner: str) -> None:
        # these attributes are public
        self.owner = owner

        # private - by convention use underscore prefix
        self._riksdaler = 0
        self._skilling = 0

    def deposit(self, riksdaler: float = 0, skilling: float = 0) -> None:
        if riksdaler < 0 or skilling < 0:
            raise ValueError(f"Stop depositing negative values. {riksdaler} riksdaler or {skilling} skillingar not okay")
        
        self._riksdaler += riksdaler
        self._skilling += skilling

    def withdraw(self, riksdaler: float = 0, skilling: float = 0) -> None:
        if riksdaler > self._riksdaler or skilling > self._skilling:
            raise ValueError("You can't withdraw more coins than you have")
        self._riksdaler -= riksdaler
        self._skilling -= skilling

    def check_balance(self) -> str:
        return f"Coins in stash: {self._riksdaler} riksdaler and {self._skilling} skillingar"

    def __repr__(self) -> str:
        return f"OldCoinStash(owner='{self.owner}')"