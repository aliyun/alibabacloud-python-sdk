# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachEnsInstancesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        scripts: str = None,
    ):
        # The instance ID. Only a single ID is supported.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The command to execute on the instance. The command must be encoded in Base64 and UTF-8.
        # 
        # This parameter is required.
        self.scripts = scripts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.scripts is not None:
            result['Scripts'] = self.scripts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Scripts') is not None:
            self.scripts = m.get('Scripts')

        return self

