# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryUpgradableVersionsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        minor: bool = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether to query the minor versions that you can upgrade to. Default value: true. Valid values:
        # 
        # *   true: The minor versions that you can upgrade to.
        # *   false: The major versions that you can upgrade to.
        self.minor = minor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.minor is not None:
            result['Minor'] = self.minor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Minor') is not None:
            self.minor = m.get('Minor')

        return self

