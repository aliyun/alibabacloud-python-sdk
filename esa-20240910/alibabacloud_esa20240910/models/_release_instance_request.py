# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReleaseInstanceRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The ID of the security instance. This must be a DDoS security instance ID in the format of esa-ddos-*. You can call the ListDDoSInstances operation to obtain the ID. Site instance IDs in the format of esa-site-* are not supported.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

