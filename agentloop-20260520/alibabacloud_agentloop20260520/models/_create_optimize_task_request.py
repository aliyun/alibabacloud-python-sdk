# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CreateOptimizeTaskRequest(DaraModel):
    def __init__(
        self,
        config: Dict[str, Any] = None,
        optimize_task_name: str = None,
        status: str = None,
        type: str = None,
        client_token: str = None,
    ):
        # The type-specific configurations. Optional prompts for ExperienceMining and SkillOptimize only support inline Markdown. The main text is saved to inputs.prompt.content (non-empty UTF-8, up to 16 KiB).
        self.config = config
        # The name of the optimization task. The name of a new service task is specified by the caller and must be unique within the same AgentSpace.
        self.optimize_task_name = optimize_task_name
        # The status of the task. Valid values: Enabled, Disabled.
        self.status = status
        # The type of the optimization task. Valid values: ExperienceMining, SkillOptimize, EfficiencyAnalysis, SOPGeneration, EvalMining, PolicyMining, and AssetMining. The memory base uses the current ContextStore and the original Worker, and is not integrated with Mining.
        self.type = type
        # The idempotency token.
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config

        if self.optimize_task_name is not None:
            result['optimizeTaskName'] = self.optimize_task_name

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('optimizeTaskName') is not None:
            self.optimize_task_name = m.get('optimizeTaskName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

