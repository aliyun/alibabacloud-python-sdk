# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableCenVbrHealthCheckRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        description: str = None,
        health_check_interval: int = None,
        health_check_only: bool = None,
        health_check_source_ip: str = None,
        health_check_target_ip: str = None,
        healthy_threshold: int = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vbr_instance_id: str = None,
        vbr_instance_owner_id: int = None,
        vbr_instance_region_id: str = None,
    ):
        # The ID of the Cloud Enterprise Network (CEN) instance.
        # 
        # This parameter is required.
        self.cen_id = cen_id
        # The description.
        # 
        # The description must be 1 to 256 characters in length and cannot start with `http:// `or `https://`.
        self.description = description
        # The time interval at which probe packets are sent during a health check. Unit: seconds. Default value: 2. Valid values: **2** to **3**.
        self.health_check_interval = health_check_interval
        # Specifies whether to enable only the detection feature. Valid values:
        # 
        # - **true**: Yes.
        # 
        #   ```
        #     If you enable only the detection feature, the system performs a health check but does not switch routes when the Express Connect circuit is down.
        # 
        #     > Make sure that you have another way to ensure link redundancy. Otherwise, network interruptions may occur.
        #   ```
        # 
        # - **false** (default): No.
        # 
        #   ```
        #     This feature is disabled by default. If the health check detects a link failure and a redundant route is available in the CEN instance, the system immediately switches to the available route.
        #   ```
        self.health_check_only = health_check_only
        # The source IP address for the health check. You can configure the source IP address in one of the following ways:
        # 
        # - **Automatic IP address** (recommended): The system automatically assigns an IP address from the 100.96.0.0/16 CIDR block.
        # 
        # - **Custom IP address**: You can specify an unused IP address from the 10.0.0.0/8, 192.168.0.0/16, or 172.16.0.0/12 CIDR block. The specified IP address cannot conflict with an IP address that is used for communication in the CEN instance. The specified IP address also cannot conflict with the Alibaba Cloud-side or client-side IP address of the VBR instance.
        self.health_check_source_ip = health_check_source_ip
        # The destination IP address for the health check.
        # 
        # The destination IP address is the client-side IP address of the VBR instance.
        # 
        # This parameter is required.
        self.health_check_target_ip = health_check_target_ip
        # The number of probe packets that are sent during a health check. Unit: packets. Valid values: 3 to **8**. Default value: **8**.
        self.healthy_threshold = healthy_threshold
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the VBR instance.
        # 
        # This parameter is required.
        self.vbr_instance_id = vbr_instance_id
        # The ID of the Alibaba Cloud account to which the VBR instance belongs.
        # 
        # > This parameter is required if the VBR instance and the CEN instance belong to different Alibaba Cloud accounts.
        self.vbr_instance_owner_id = vbr_instance_owner_id
        # The ID of the region where the VBR instance is deployed.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query region IDs.
        # 
        # This parameter is required.
        self.vbr_instance_region_id = vbr_instance_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.description is not None:
            result['Description'] = self.description

        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval

        if self.health_check_only is not None:
            result['HealthCheckOnly'] = self.health_check_only

        if self.health_check_source_ip is not None:
            result['HealthCheckSourceIp'] = self.health_check_source_ip

        if self.health_check_target_ip is not None:
            result['HealthCheckTargetIp'] = self.health_check_target_ip

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.vbr_instance_id is not None:
            result['VbrInstanceId'] = self.vbr_instance_id

        if self.vbr_instance_owner_id is not None:
            result['VbrInstanceOwnerId'] = self.vbr_instance_owner_id

        if self.vbr_instance_region_id is not None:
            result['VbrInstanceRegionId'] = self.vbr_instance_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')

        if m.get('HealthCheckOnly') is not None:
            self.health_check_only = m.get('HealthCheckOnly')

        if m.get('HealthCheckSourceIp') is not None:
            self.health_check_source_ip = m.get('HealthCheckSourceIp')

        if m.get('HealthCheckTargetIp') is not None:
            self.health_check_target_ip = m.get('HealthCheckTargetIp')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('VbrInstanceId') is not None:
            self.vbr_instance_id = m.get('VbrInstanceId')

        if m.get('VbrInstanceOwnerId') is not None:
            self.vbr_instance_owner_id = m.get('VbrInstanceOwnerId')

        if m.get('VbrInstanceRegionId') is not None:
            self.vbr_instance_region_id = m.get('VbrInstanceRegionId')

        return self

