# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class CreateOptimizeRunRequest(DaraModel):
    def __init__(
        self,
        input: Any = None,
        preview: bool = None,
        client_token: str = None,
    ):
        # The JSON input defined by the task type, preserving the original object or array structure. ExperienceMining accepts a start/end/processTimeMaxNS object. SkillOptimize accepts an inline input array, a skills/window object for SLS, or a skills/records object for ATIF or xTrace. The server validates the input based on the task type and configuration. Memory extraction continues to use the original ContextStore API.
        # 
        # This parameter is required.
        self.input = input
        # Specifies whether to execute an independent pre-run of the complete algorithm. The pre-run generates candidate results and evidence without publishing them to the target dataset or advancing the formal run history. A formal run executes the algorithm independently.
        self.preview = preview
        # The idempotency token. Use the same value when you retry the same creation request.
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['input'] = self.input

        if self.preview is not None:
            result['preview'] = self.preview

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('input') is not None:
            self.input = m.get('input')

        if m.get('preview') is not None:
            self.preview = m.get('preview')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

