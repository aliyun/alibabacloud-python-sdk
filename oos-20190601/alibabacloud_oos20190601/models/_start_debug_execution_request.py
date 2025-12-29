# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartDebugExecutionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        properties: str = None,
        region_id: str = None,
        task_type: str = None,
    ):
        self.client_token = client_token
        self.properties = properties
        self.region_id = region_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

