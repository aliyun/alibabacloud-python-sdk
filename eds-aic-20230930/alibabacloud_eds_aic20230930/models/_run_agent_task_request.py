# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RunAgentTaskRequest(DaraModel):
    def __init__(
        self,
        biz_region_id: str = None,
        instance_ids: List[str] = None,
        max_steps: int = None,
        timeout_seconds: int = None,
        user_prompt: str = None,
    ):
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # This parameter is required.
        self.instance_ids = instance_ids
        self.max_steps = max_steps
        self.timeout_seconds = timeout_seconds
        # This parameter is required.
        self.user_prompt = user_prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.max_steps is not None:
            result['MaxSteps'] = self.max_steps

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        if self.user_prompt is not None:
            result['UserPrompt'] = self.user_prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('MaxSteps') is not None:
            self.max_steps = m.get('MaxSteps')

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        if m.get('UserPrompt') is not None:
            self.user_prompt = m.get('UserPrompt')

        return self

