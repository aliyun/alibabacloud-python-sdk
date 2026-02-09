# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AicsOpenApiInvokeShrinkRequest(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        node_id: str = None,
        param_shrink: str = None,
        service_id: str = None,
        type: str = None,
    ):
        self.job_id = job_id
        self.node_id = node_id
        self.param_shrink = param_shrink
        # This parameter is required.
        self.service_id = service_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.param_shrink is not None:
            result['Param'] = self.param_shrink

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Param') is not None:
            self.param_shrink = m.get('Param')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

