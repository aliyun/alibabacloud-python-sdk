# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class CreateIpSetsRequest(DaraModel):
    def __init__(
        self,
        accelerate_region: List[main_models.CreateIpSetsRequestAccelerateRegion] = None,
        accelerator_id: str = None,
        client_token: str = None,
        region_id: str = None,
    ):
        # The information about the acceleration regions.
        # 
        # This parameter is required.
        self.accelerate_region = accelerate_region
        # The GA instance ID.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The region ID of the GA instance. Set the value to **cn-hangzhou**.
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

        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accelerate_region = []
        if m.get('AccelerateRegion') is not None:
            for k1 in m.get('AccelerateRegion'):
                temp_model = main_models.CreateIpSetsRequestAccelerateRegion()
                self.accelerate_region.append(temp_model.from_map(k1))

        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CreateIpSetsRequestAccelerateRegion(DaraModel):
    def __init__(
        self,
        accelerate_region_id: str = None,
        bandwidth: int = None,
        ip_version: str = None,
        isp_type: str = None,
    ):
        # The ID of the acceleration region.
        # 
        # The number of regions that you can add varies based on the specification of the GA instance. For more information, see [Overview](https://help.aliyun.com/document_detail/153127.html).
        # 
        # This parameter is required.
        self.accelerate_region_id = accelerate_region_id
        # The bandwidth that you want to allocate to the acceleration region. Unit: **Mbit/s**.
        # 
        # >*  This parameter is required.
        # >*   You must allocate at least 2 Mbit/s of bandwidth to each acceleration region.
        # >*   The total bandwidth of all acceleration regions cannot exceed the bandwidth limit of your basic bandwidth plan.
        self.bandwidth = bandwidth
        # The IP version used to connect to the GA instance. Valid values:
        # 
        # *   **IPv4** (default)
        # *   **IPv6**
        # *   **DUAL_STACK**: IPv4 and IPv6
        # 
        # > Only pay-as-you-go standard GA instances support DUAL_STACK.
        self.ip_version = ip_version
        # The line type of the elastic IP address (EIP) in the acceleration region. Valid values:
        # 
        # *   **BGP**: BGP (Multi-ISP) lines.
        # *   **BGP_PRO**: BGP (Multi-ISP) Pro lines
        # 
        # > *   This parameter is required only if the bandwidth metering method of the GA instance is **pay-by-data transfer**.
        # >*   Different acceleration regions support different line types of EIPs.
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

