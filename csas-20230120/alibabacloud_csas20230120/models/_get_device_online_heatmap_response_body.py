# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetDeviceOnlineHeatmapResponseBody(DaraModel):
    def __init__(
        self,
        device_online_heatmap: List[List[int]] = None,
        request_id: str = None,
    ):
        # The online time distribution.
        self.device_online_heatmap = device_online_heatmap
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_online_heatmap is not None:
            result['DeviceOnlineHeatmap'] = self.device_online_heatmap

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceOnlineHeatmap') is not None:
            self.device_online_heatmap = m.get('DeviceOnlineHeatmap')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

