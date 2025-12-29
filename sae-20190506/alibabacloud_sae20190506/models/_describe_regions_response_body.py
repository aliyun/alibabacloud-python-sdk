# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeRegionsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        regions: main_models.DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: The call was successful.
        # *   **3xx**: The call was redirected.
        # *   **4xx**: The call failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The returned message.
        self.message = message
        # The regions.
        self.regions = regions
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.regions is not None:
            result['Regions'] = self.regions.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Regions') is not None:
            temp_model = main_models.DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m.get('Regions'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRegionsResponseBodyRegions(DaraModel):
    def __init__(
        self,
        region: List[main_models.DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for v1 in self.region:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Region'] = []
        if self.region is not None:
            for k1 in self.region:
                result['Region'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k1 in m.get('Region'):
                temp_model = main_models.DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k1))

        return self

class DescribeRegionsResponseBodyRegionsRegion(DaraModel):
    def __init__(
        self,
        local_name: str = None,
        recommend_zones: main_models.DescribeRegionsResponseBodyRegionsRegionRecommendZones = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        # The region name. Valid values:
        # 
        # *   **China (Hangzhou)**
        # *   **China (Shanghai)**
        # *   **China (Beijing)**
        # *   **China (Zhangjiakou)**
        # *   **China (Shenzhen)**
        # *   **China (Guangzhou)**
        # *   **China (Hong Kong)**
        # *   **Singapore**
        # *   **US (Silicon Valley)**
        self.local_name = local_name
        # The recommended zones.
        self.recommend_zones = recommend_zones
        # The endpoint for the region. Valid values:
        # 
        # *   **sae.cn-hangzhou.aliyuncs.com**
        # *   **sae.cn-shanghai.aliyuncs.com**
        # *   **sae.cn-beijing.aliyuncs.com**
        # *   **sae.cn-zhangjiakou.aliyuncs.com**
        # *   **sae.cn-shenzhen.aliyuncs.com**
        # *   **sae.cn-guangzhou.aliyuncs.com**
        # *   **sae.cn-hongkong.aliyuncs.com**
        # *   **sae.ap-southeast-1.aliyuncs.com**
        # *   **sae.us-west-1.aliyuncs.com**
        self.region_endpoint = region_endpoint
        # The region ID. Valid values:
        # 
        # *   **cn-hangzhou**: the ID of the China (Hangzhou) region
        # *   **cn-shanghai**: the ID of the China (Shanghai) region
        # *   **cn-beijing**: the ID of the China (Beijing) region
        # *   **cn-zhangjiakou**: the ID of the China (Zhangjiakou) region
        # *   **cn-shenzhen**: the ID of the China (Shenzhen) region
        # *   **cn-guangzhou**: the ID of the China (Guangzhou) region
        # *   **cn-hongkong**: the ID of the China (Hong Kong) region
        # *   **ap-southeast-1**: the ID of the Singapore region
        # *   **us-west-1**: the ID of the US (Silicon Valley) region
        self.region_id = region_id

    def validate(self):
        if self.recommend_zones:
            self.recommend_zones.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.recommend_zones is not None:
            result['RecommendZones'] = self.recommend_zones.to_map()

        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('RecommendZones') is not None:
            temp_model = main_models.DescribeRegionsResponseBodyRegionsRegionRecommendZones()
            self.recommend_zones = temp_model.from_map(m.get('RecommendZones'))

        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class DescribeRegionsResponseBodyRegionsRegionRecommendZones(DaraModel):
    def __init__(
        self,
        recommend_zone: List[str] = None,
    ):
        self.recommend_zone = recommend_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.recommend_zone is not None:
            result['RecommendZone'] = self.recommend_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecommendZone') is not None:
            self.recommend_zone = m.get('RecommendZone')

        return self

