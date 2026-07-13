# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDnsGtmAccessStrategyAvailableConfigRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        strategy_mode: str = None,
    ):
        # The instance ID. You can call the [DescribeDnsGtmInstances](https://www.alibabacloud.com/help/en/dns/api-alidns-2015-01-09-describednsgtminstances) operation to obtain the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The language of the response. Default: en. Valid values: en, zh, and ja.
        self.lang = lang
        # The scheduling mode. Valid values:
        # 
        # - GEO: Geolocation-based
        # 
        # - LATENCY: Latency-based
        # 
        # This parameter is required.
        self.strategy_mode = strategy_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.strategy_mode is not None:
            result['StrategyMode'] = self.strategy_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('StrategyMode') is not None:
            self.strategy_mode = m.get('StrategyMode')

        return self

