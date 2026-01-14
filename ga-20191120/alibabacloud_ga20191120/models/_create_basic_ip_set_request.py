# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBasicIpSetRequest(DaraModel):
    def __init__(
        self,
        accelerate_region_id: str = None,
        accelerator_id: str = None,
        bandwidth: int = None,
        client_token: str = None,
        isp_type: str = None,
        region_id: str = None,
    ):
        # The ID of the acceleration region.
        # 
        # You can call the [ListAvailableBusiRegions](https://help.aliyun.com/document_detail/261190.html) operation to query the most recent acceleration region list.
        # 
        # This parameter is required.
        self.accelerate_region_id = accelerate_region_id
        # The ID of the basic GA instance.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # The bandwidth that you want to allocate to the acceleration region. Unit: **Mbit/s**.
        # 
        # You must allocate at least 2 Mbit/s of bandwidth to the acceleration region.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The line type of the elastic IP address (EIP) in the acceleration region. Valid values:
        # 
        # *   **BGP** (default): BGP (Multi-ISP) lines.
        # *   **BGP_PRO**: BGP (Multi-ISP) Pro lines.
        # 
        # Valid values if you are allowed to use single-ISP bandwidth:
        # 
        # *   **ChinaTelecom**
        # *   **ChinaUnicom**
        # *   **ChinaMobile**
        # *   **ChinaTelecom_L2**
        # *   **ChinaUnicom_L2**
        # *   **ChinaMobile_L2**
        # 
        # > 
        # 
        # *   If the bandwidth metering method of the GA instance is **pay-by-data-transfer**, this parameter is required.
        # 
        # *   If the acceleration region is China (Hong Kong) and a basic bandwidth plan whose bandwidth type is Premium is associated with the GA instance, the default value of IspType is BGP_PRO.
        # 
        # *   The supported single-ISP type varies based on the acceleration region.
        self.isp_type = isp_type
        # The region ID of the basic GA instance. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerate_region_id is not None:
            result['AccelerateRegionId'] = self.accelerate_region_id

        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.isp_type is not None:
            result['IspType'] = self.isp_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')

        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('IspType') is not None:
            self.isp_type = m.get('IspType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

