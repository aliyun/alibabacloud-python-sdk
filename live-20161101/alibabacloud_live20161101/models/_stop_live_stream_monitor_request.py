# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopLiveStreamMonitorRequest(DaraModel):
    def __init__(
        self,
        monitor_id: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # The ID of the monitoring session.
        # 
        # >  You can obtain the monitoring session ID**** from the response of the [CreateLiveStreamMonitor](https://help.aliyun.com/document_detail/2848129.html) operation.
        # 
        # This parameter is required.
        self.monitor_id = monitor_id
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.monitor_id is not None:
            result['MonitorId'] = self.monitor_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorId') is not None:
            self.monitor_id = m.get('MonitorId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

