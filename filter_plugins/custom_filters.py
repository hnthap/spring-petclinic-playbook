from typing import Callable


class FilterModule:
  def filters(self) -> dict[str, Callable[..., str]]:
    return { "make_uppercase": self.make_uppercase }
  
  @staticmethod
  def make_uppercase(string: object) -> str:
    return str(string).upper()
