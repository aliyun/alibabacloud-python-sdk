# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDnsGtmAccessStrategiesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        strategy_mode: str = None,
    ):
        # The instance ID.<props="china"> Call [DescribeDnsGtmInstances](https://help.aliyun.com/zh/dns/api-alidns-2015-01-09-describednsgtminstances?spm=a2c4g.11186623.help-menu-29697.d_0_5_1_3_8_8.2aea3618RlSR9K) to obtain the instance ID.
        # <props="intl">Call [DescribeDnsGtmInstances](https://www.alibabacloud.com/help/zh/dns/api-alidns-2015-01-09-describednsgtminstances?spm=a2c63.p38356.help-menu-search-29697.d_0) to obtain the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The language of the response. Default value: en. Valid values: en, zh, and ja.
        self.lang = lang
        # The page number. The value starts from **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 100. Default value: 20.
        self.page_size = page_size
        # The type of the access policy.
        # 
        # - GEO: Geographic location-based access policy
        # 
        # - LATENCY: Latency-based access policy
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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.strategy_mode is not None:
            result['StrategyMode'] = self.strategy_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StrategyMode') is not None:
            self.strategy_mode = m.get('StrategyMode')

        return self

