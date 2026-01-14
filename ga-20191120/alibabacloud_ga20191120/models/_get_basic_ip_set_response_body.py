# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBasicIpSetResponseBody(DaraModel):
    def __init__(
        self,
        accelerate_region_id: str = None,
        accelerator_id: str = None,
        bandwidth: int = None,
        ip_address: str = None,
        ip_set_id: str = None,
        ip_version: str = None,
        isp_type: str = None,
        request_id: str = None,
        state: str = None,
    ):
        # The ID of the region where the basic GA instance is deployed.
        self.accelerate_region_id = accelerate_region_id
        # The ID of the basic GA instance.
        self.accelerator_id = accelerator_id
        # The bandwidth of the acceleration region of the basic GA instance. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The accelerated IP address.
        self.ip_address = ip_address
        # The ID of the acceleration region of the basic GA instance.
        self.ip_set_id = ip_set_id
        # The Internet protocol version. Only **IPv4** may be returned.
        self.ip_version = ip_version
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
        self.isp_type = isp_type
        # The ID of the request.
        self.request_id = request_id
        # The status of the acceleration region of the basic GA instance. Valid values:
        # 
        # *   **init**: The acceleration region is being initialized.
        # *   **active**: The acceleration region is in the running state.
        # *   **updating**: The acceleration region is being configured.
        # *   **Deleting**: The acceleration region is being deleted.
        self.state = state

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

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.isp_type is not None:
            result['IspType'] = self.isp_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')

        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('IspType') is not None:
            self.isp_type = m.get('IspType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

