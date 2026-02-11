# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConsistencySnapshotRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        current_timestamp: int = None,
        pid: str = None,
        proxy_user_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.app_type = app_type
        self.current_timestamp = current_timestamp
        # This parameter is required.
        self.pid = pid
        self.proxy_user_id = proxy_user_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.current_timestamp is not None:
            result['CurrentTimestamp'] = self.current_timestamp

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('CurrentTimestamp') is not None:
            self.current_timestamp = m.get('CurrentTimestamp')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

