from .agents.base import Agent


class Orchestrator:
    def register(self, name: str, agent: Agent) -> None:
        # logique privée — non incluse
        raise NotImplementedError("logique privée — non incluse")
