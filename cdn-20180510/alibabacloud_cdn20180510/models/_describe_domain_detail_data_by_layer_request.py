# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainDetailDataByLayerRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        field: str = None,
        isp_name_en: str = None,
        layer: str = None,
        location_name_en: str = None,
        start_time: str = None,
    ):
        # The name of the Internet service provider (ISP) for your Alibaba Cloud CDN service. You can call the [DescribeCdnRegionAndIsp](https://help.aliyun.com/document_detail/91077.html) operation to query ISP names.
        # 
        # If you do not specify an ISP, data of all ISPs is queried.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The protocol by which you want to query data. Valid values: **http**, **https**, **quic**, and **all**.
        # 
        # The default value is **all**.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # >  The end time must be later than the start time.
        # 
        # This parameter is required.
        self.field = field
        # The ID of the request.
        self.isp_name_en = isp_name_en
        # The amount of network traffic. Unit: bytes.
        self.layer = layer
        # The detailed data of the accelerated domain names.
        self.location_name_en = location_name_en
        # The name of the region. You can call the [DescribeCdnRegionAndIsp](https://help.aliyun.com/document_detail/91077.html) operation to query regions.
        # 
        # If you do not specify a region, data in all regions is queried.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.field is not None:
            result['Field'] = self.field

        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

