from dataclasses import dataclass, field
@dataclass
class RunState:
    status: str = "intake"
    findings: list = field(default_factory=list)
