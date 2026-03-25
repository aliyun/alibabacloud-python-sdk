# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeCenPrivateZoneRoutesResponseBody(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        page_number: int = None,
        page_size: int = None,
        private_zone_dns_servers: str = None,
        private_zone_infos: main_models.DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfos = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The IP address of the DNS server used by PrivateZone.
        self.private_zone_dns_servers = private_zone_dns_servers
        self.private_zone_infos = private_zone_infos
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.private_zone_infos:
            self.private_zone_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.private_zone_dns_servers is not None:
            result['PrivateZoneDnsServers'] = self.private_zone_dns_servers

        if self.private_zone_infos is not None:
            result['PrivateZoneInfos'] = self.private_zone_infos.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrivateZoneDnsServers') is not None:
            self.private_zone_dns_servers = m.get('PrivateZoneDnsServers')

        if m.get('PrivateZoneInfos') is not None:
            temp_model = main_models.DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfos()
            self.private_zone_infos = temp_model.from_map(m.get('PrivateZoneInfos'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfos(DaraModel):
    def __init__(
        self,
        private_zone_info: List[main_models.DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfosPrivateZoneInfo] = None,
    ):
        self.private_zone_info = private_zone_info

    def validate(self):
        if self.private_zone_info:
            for v1 in self.private_zone_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PrivateZoneInfo'] = []
        if self.private_zone_info is not None:
            for k1 in self.private_zone_info:
                result['PrivateZoneInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.private_zone_info = []
        if m.get('PrivateZoneInfo') is not None:
            for k1 in m.get('PrivateZoneInfo'):
                temp_model = main_models.DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfosPrivateZoneInfo()
                self.private_zone_info.append(temp_model.from_map(k1))

        return self

class DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfosPrivateZoneInfo(DaraModel):
    def __init__(
        self,
        access_region_id: str = None,
        host_region_id: str = None,
        host_vpc_id: str = None,
        status: str = None,
    ):
        self.access_region_id = access_region_id
        self.host_region_id = host_region_id
        self.host_vpc_id = host_vpc_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_region_id is not None:
            result['AccessRegionId'] = self.access_region_id

        if self.host_region_id is not None:
            result['HostRegionId'] = self.host_region_id

        if self.host_vpc_id is not None:
            result['HostVpcId'] = self.host_vpc_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessRegionId') is not None:
            self.access_region_id = m.get('AccessRegionId')

        if m.get('HostRegionId') is not None:
            self.host_region_id = m.get('HostRegionId')

        if m.get('HostVpcId') is not None:
            self.host_vpc_id = m.get('HostVpcId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

