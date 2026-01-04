# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkRegionBlockResponseBody(DaraModel):
    def __init__(
        self,
        config: main_models.DescribeNetworkRegionBlockResponseBodyConfig = None,
        request_id: str = None,
    ):
        # The configuration of blocked locations.
        self.config = config
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = main_models.DescribeNetworkRegionBlockResponseBodyConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeNetworkRegionBlockResponseBodyConfig(DaraModel):
    def __init__(
        self,
        countries: List[int] = None,
        provinces: List[int] = None,
        region_block_switch: str = None,
    ):
        # The codes of the countries or areas from which the requests are blocked.
        self.countries = countries
        # The codes of the administrative regions in China from which the requests are blocked.
        self.provinces = provinces
        # The status of the Location Blacklist policy. Valid values:
        # 
        # *   **on**: enabled
        # *   **off**: disabled
        self.region_block_switch = region_block_switch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.countries is not None:
            result['Countries'] = self.countries

        if self.provinces is not None:
            result['Provinces'] = self.provinces

        if self.region_block_switch is not None:
            result['RegionBlockSwitch'] = self.region_block_switch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Countries') is not None:
            self.countries = m.get('Countries')

        if m.get('Provinces') is not None:
            self.provinces = m.get('Provinces')

        if m.get('RegionBlockSwitch') is not None:
            self.region_block_switch = m.get('RegionBlockSwitch')

        return self

