# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyInstancesSSLResponseBody(DaraModel):
    def __init__(
        self,
        instance_names: List[str] = None,
        request_id: str = None,
    ):
        self.instance_names = instance_names
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_names is not None:
            result['InstanceNames'] = self.instance_names

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceNames') is not None:
            self.instance_names = m.get('InstanceNames')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

