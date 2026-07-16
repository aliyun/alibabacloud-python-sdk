# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class ModifyOfficeSiteAcceleratorRequest(DaraModel):
    def __init__(
        self,
        accelerate_region: List[main_models.ModifyOfficeSiteAcceleratorRequestAccelerateRegion] = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        # The information about the regions to accelerate.
        self.accelerate_region = accelerate_region
        # The office network ID.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.accelerate_region:
            for v1 in self.accelerate_region:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccelerateRegion'] = []
        if self.accelerate_region is not None:
            for k1 in self.accelerate_region:
                result['AccelerateRegion'].append(k1.to_map() if k1 else None)

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accelerate_region = []
        if m.get('AccelerateRegion') is not None:
            for k1 in m.get('AccelerateRegion'):
                temp_model = main_models.ModifyOfficeSiteAcceleratorRequestAccelerateRegion()
                self.accelerate_region.append(temp_model.from_map(k1))

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ModifyOfficeSiteAcceleratorRequestAccelerateRegion(DaraModel):
    def __init__(
        self,
        accelerate_region_id: str = None,
        bandwidth: int = None,
        ip_version: str = None,
        isp_type: str = None,
    ):
        # The ID of the region to accelerate.
        # 
        # The number of regions that you can add is limited by the total bandwidth and the instance type of the GA instance. For more information about the number of access regions supported by each instance type, see [Overview of GA instances](t1855472.xdita#).
        # 
        # This parameter is required.
        self.accelerate_region_id = accelerate_region_id
        # The peak public bandwidth. Unit: Mbps.
        # 
        # > For the pay-by-bandwidth metering method, the value ranges from 10 to 1000.
        # 
        # This parameter is required.
        self.bandwidth = bandwidth
        # The IP protocol version used to access GA instances. Valid values:
        # 
        # - **IPv4** (default)
        # 
        # - **IPv6**
        # 
        # - **DUAL_STACK**: IPv4 and IPv6
        # 
        # > * Only standard pay-as-you-go GA instances support the DUAL_STACK option.
        self.ip_version = ip_version
        # The Internet line type in the acceleration region. Valid values:
        # 
        # - **BGP**: BGP (Multi-ISP) lines.
        # 
        # - **BGP_PRO**: BGP (Multi-ISP) Pro lines.
        # 
        # > * This parameter is required for GA instances that use the pay-by-data-transfer metering method.
        # >
        # > * The supported line types vary based on the acceleration region.
        # 
        # This parameter is required.
        self.isp_type = isp_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerate_region_id is not None:
            result['AccelerateRegionId'] = self.accelerate_region_id

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.isp_type is not None:
            result['IspType'] = self.isp_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('IspType') is not None:
            self.isp_type = m.get('IspType')

        return self

