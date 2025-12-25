# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRegionsResponseBody(DaraModel):
    def __init__(
        self,
        regions: main_models.DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        # The available regions and zones.
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
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = main_models.DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m.get('Regions'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRegionsResponseBodyRegions(DaraModel):
    def __init__(
        self,
        rdsregion: List[main_models.DescribeRegionsResponseBodyRegionsRDSRegion] = None,
    ):
        self.rdsregion = rdsregion

    def validate(self):
        if self.rdsregion:
            for v1 in self.rdsregion:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RDSRegion'] = []
        if self.rdsregion is not None:
            for k1 in self.rdsregion:
                result['RDSRegion'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rdsregion = []
        if m.get('RDSRegion') is not None:
            for k1 in m.get('RDSRegion'):
                temp_model = main_models.DescribeRegionsResponseBodyRegionsRDSRegion()
                self.rdsregion.append(temp_model.from_map(k1))

        return self

class DescribeRegionsResponseBodyRegionsRDSRegion(DaraModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
        zone_id: str = None,
        zone_name: str = None,
    ):
        # The region name. The return value of this parameter is in the language that is specified by the **AcceptLanguage** parameter. For example, if the value of the RegionId parameter in the response is cn-hangzhou, the following values are returned for the LocalName parameter:
        # 
        # *   If the value of the **AcceptLanguage** parameter is **zh-CN**, the value  1()is returned for the LocalName parameter.
        # *   If the value of the **AcceptLanguage** parameter is **en-US**, the value China (Hangzhou) is returned for the LocalName parameter.
        self.local_name = local_name
        # The endpoint that is used to connect to Alibaba Cloud services in the region. For more information, see [Endpoints](https://help.aliyun.com/document_detail/610370.html).
        self.region_endpoint = region_endpoint
        # The region ID.
        self.region_id = region_id
        # The zone ID.
        self.zone_id = zone_id
        # The zone name. The return value of this parameter is in the language that is specified by the **AcceptLanguage** parameter. For example, if the value of the ZoneId parameter in the response is cn-hangzhou-j, the following values are returned for the ZoneName parameter:
        # 
        # *   If the value of the **AcceptLanguage** parameter is **zh-CN**, the value   J is returned for the ZoneName parameter.
        # *   If the value of the **AcceptLanguage** parameter is **en-US**, the value Hangzhou Zone J is returned for the ZoneName parameter.
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

