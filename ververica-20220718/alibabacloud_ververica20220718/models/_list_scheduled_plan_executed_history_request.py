# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListScheduledPlanExecutedHistoryRequest(DaraModel):
    def __init__(
        self,
        deployment_id: str = None,
        origin: str = None,
    ):
        # This parameter is required.
        self.deployment_id = deployment_id
        self.origin = origin

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id

        if self.origin is not None:
            result['origin'] = self.origin

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')

        if m.get('origin') is not None:
            self.origin = m.get('origin')

        return self

