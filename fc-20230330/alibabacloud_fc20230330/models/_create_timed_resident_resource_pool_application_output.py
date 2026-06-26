# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTimedResidentResourcePoolApplicationOutput(DaraModel):
    def __init__(
        self,
        application_status: str = None,
        timed_pool_id: str = None,
    ):
        self.application_status = application_status
        self.timed_pool_id = timed_pool_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_status is not None:
            result['applicationStatus'] = self.application_status

        if self.timed_pool_id is not None:
            result['timedPoolId'] = self.timed_pool_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationStatus') is not None:
            self.application_status = m.get('applicationStatus')

        if m.get('timedPoolId') is not None:
            self.timed_pool_id = m.get('timedPoolId')

        return self

