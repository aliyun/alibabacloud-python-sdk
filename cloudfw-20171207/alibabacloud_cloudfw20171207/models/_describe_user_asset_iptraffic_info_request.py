# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserAssetIPTrafficInfoRequest(DaraModel):
    def __init__(
        self,
        asset_ip: str = None,
        lang: str = None,
        traffic_time: str = None,
    ):
        # The IP address of the asset.
        # 
        # This parameter is required.
        self.asset_ip = asset_ip
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.traffic_time = traffic_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_ip is not None:
            result['AssetIP'] = self.asset_ip

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.traffic_time is not None:
            result['TrafficTime'] = self.traffic_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetIP') is not None:
            self.asset_ip = m.get('AssetIP')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('TrafficTime') is not None:
            self.traffic_time = m.get('TrafficTime')

        return self

