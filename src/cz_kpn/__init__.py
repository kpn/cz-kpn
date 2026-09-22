from typing import Any

__all__ = ["KPNCz"]


def __getattr__(name: str) -> Any:
    if name == "KPNCz":
        from cz_kpn.rules import KPNCz

        return KPNCz
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
