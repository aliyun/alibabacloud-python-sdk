# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        request_id: str = None,
    ):
        # The instance IDs of the Simple Application Server instances.
        self.instance_ids = instance_ids
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

