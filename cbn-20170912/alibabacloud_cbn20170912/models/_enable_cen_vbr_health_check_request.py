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
        # The Cloud Enterprise Network (CEN) instance ID.
        # 
        # This parameter is required.
        self.cen_id = cen_id
        # The description.  
        # 
        # The description must be 1 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The interval at which health check probe packets are sent. Unit: seconds. Default value: **2**. Valid values: **2** to **3**.
        self.health_check_interval = health_check_interval
        # Specifies whether to enable only the health check detection feature. Valid values:
        # 
        # - **true**: Only the detection feature is enabled.
        # 
        #         If only the health check detection feature is enabled, route switchover is not triggered when the health check detects that the link is down.
        # 
        #         > Make sure that you have other methods to ensure link redundancy. Otherwise, enabling this feature may cause link interruptions.
        # 
        # - **false** (default): The detection-only feature is not enabled.
        #         
        #         This feature is disabled by default. When the health check detects that the link is down, if redundant routes exist in the CEN instance, the health check immediately triggers a route switchover to use an available link.
        self.health_check_only = health_check_only
        # The source IP address for health checks. The following configuration methods are supported:
        # 
        # - **Automatically generated source IP** (recommended): The system automatically allocates an IP address from the 100.96.0.0/16 CIDR block.
        # 
        # - **Custom source IP**: The source IP address can be any unused IP address within the 10.0.0.0/8, 192.168.0.0/16, or 172.16.0.0/12 CIDR block. The IP address cannot cause an IP address conflict with addresses that need to communicate with each other in the CEN instance, or with the Alibaba Cloud-side or customer-side IP address of the VBR instance.
        self.health_check_source_ip = health_check_source_ip
        # The destination IP address for health checks.
        # 
        # The destination IP address is the customer-side IP address of the VBR instance.
        # 
        # This parameter is required.
        self.health_check_target_ip = health_check_target_ip
        # The number of probe packets sent during a health check. Unit: packets. Valid values: **3** to **8**. Default value: **8**.
        self.healthy_threshold = healthy_threshold
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The VBR instance ID.
        # 
        # This parameter is required.
        self.vbr_instance_id = vbr_instance_id
        # The ID of the Alibaba Cloud account that owns the VBR instance.
        # 
        # > This parameter is required if the VBR instance and the CEN instance belong to different accounts.
        self.vbr_instance_owner_id = vbr_instance_owner_id
        # The region ID of the VBR instance.
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

