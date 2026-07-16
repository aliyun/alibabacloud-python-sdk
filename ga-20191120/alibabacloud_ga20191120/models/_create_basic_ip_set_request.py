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
        # The ID of the region to be accelerated.
        # 
        # You can invoke the [ListAvailableBusiRegions](https://help.aliyun.com/document_detail/261190.html) operation to query the active acceleration regions for the specified Alibaba Cloud Global Accelerator (GA) instance.
        # 
        # This parameter is required.
        self.accelerate_region_id = accelerate_region_id
        # The instance ID of the basic Alibaba Cloud Global Accelerator (GA) instance.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # The bandwidth of the acceleration area. Unit: **Mbps**.
        # 
        # The minimum bandwidth that can be allocated to an acceleration area is 2 Mbps.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of a request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # The ISP type of the public network in the acceleration region. Valid values:
        # - **BGP** (default): BGP (Multi-ISP)
        # - **BGP_PRO**: BGP (Multi-ISP) Pro
        # 
        # If you are a whitelist user of single-ISP bandwidth, you can also select the following types:
        # - **ChinaTelecom**: China Telecom (single ISP)
        # - **ChinaUnicom**: China Unicom (single ISP)
        # - **ChinaMobile**: China Shift (single ISP)
        # - **ChinaTelecom_L2**: China Telecom (single ISP)_L2
        # - **ChinaUnicom_L2**: China Unicom (single ISP)_L2
        # - **ChinaMobile_L2**: China Shift (single ISP)_L2
        # > - This parameter is required for basic Alibaba Cloud Global Accelerator (GA) instances that use the **pay-by-traffic** billing method.
        # > - If the acceleration region of the basic Alibaba Cloud Global Accelerator (GA) instance is Hong Kong (China) and the instance is attached with a basic bandwidth plan of the BGP (Multi-ISP) Pro type, the default value is BGP (Multi-ISP) Pro.
        # > - The supported single-ISP line types vary by acceleration region.
        self.isp_type = isp_type
        # The region ID of the basic Alibaba Cloud Global Accelerator (GA) instance. Set the value to **ap-southeast-1**.
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

