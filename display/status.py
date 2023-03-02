from abc import ABC, abstractmethod

class StatusBase(ABC):

    @abstractmethod
    def switch_off(self) -> None:
        """Chaning state on False."""
        pass
    
    @abstractmethod
    def switch_on(self) -> None:
        """Chaning state on True."""
        pass


class Status(StatusBase):
    _status: bool = False

    def __init__(self, status: bool = True) -> None:
        self._status = status
    
    @property
    def status(self) -> bool:
        return self._status
    
    def switch_off(self) -> None:
        self._status = False
    
    def switch_on(self) -> None:
        self._status = True