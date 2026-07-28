# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeEipAddressesRequest(DaraModel):
    def __init__(
        self,
        filter: List[main_models.DescribeEipAddressesRequestFilter] = None,
        allocation_id: str = None,
        associated_instance_id: str = None,
        associated_instance_type: str = None,
        charge_type: str = None,
        dry_run: bool = None,
        eip_address: str = None,
        eip_name: str = None,
        isp: str = None,
        include_reservation_data: bool = None,
        lock_reason: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        public_ip_address_pool_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_protection_enabled: bool = None,
        segment_instance_id: str = None,
        service_managed: bool = None,
        status: str = None,
        tag: List[main_models.DescribeEipAddressesRequestTag] = None,
    ):
        self.filter = filter
        # The ID of the EIP instance to query. 
        # 
        # You can specify up to 50 EIP instance IDs. Separate multiple instance IDs with commas (,).
        # 
        # > If you specify both **EipAddress** and **AllocationId**, you can specify up to 50 EIP instance IDs for **AllocationId** and up to 50 EIP IP addresses for **EipAddress**.
        self.allocation_id = allocation_id
        # The instance ID of the cloud resource.
        self.associated_instance_id = associated_instance_id
        # The type of the cloud resource instance to attach. Valid values: 
        # - **EcsInstance** (default): an ECS instance in a VPC.
        # - **SlbInstance**: a CLB instance in a VPC.
        # - **Nat**: a NAT gateway.
        # - **HaVip**: a high-availability virtual IP address. 
        # - **NetworkInterface**: a secondary elastic network interface (ENI).
        # - **IpAddress**: an IP address.
        # 
        # > Each ECS instance, CLB instance, high-availability virtual IP address, and IP address can be attached with only one EIP at a time. A NAT gateway can be attached with multiple EIPs. The number of EIPs that can be attached to a secondary elastic network interface (ENI) depends on the EIP association pattern. For more information, see [EIP overview](https://help.aliyun.com/document_detail/72125.html).
        self.associated_instance_type = associated_instance_type
        # The billing method of the EIP. Valid values:
        # - **PostPaid**: pay-as-you-go.
        # - **PrePaid**: subscription.
        self.charge_type = charge_type
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run. The system checks the required parameters, request syntax, and business restrictions. If the check fails, the corresponding error is returned. If the check succeeds, the `DryRunOperation` error code is returned.
        # 
        # - **false** (default): performs a dry run and sends the request. If the check succeeds, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The IP address of the EIP to query.
        # 
        # You can specify up to 50 EIP addresses. Separate multiple IP addresses with commas (,).
        # 
        # > If you specify both **EipAddress** and **AllocationId**, you can specify up to 50 EIP IP addresses for **EipAddress** and up to 50 EIP instance IDs for **AllocationId**.
        self.eip_address = eip_address
        # The name of the EIP.
        # 
        # The name must be 1 to 128 characters in length and must start with a letter or Chinese character. It can contain digits, underscores (_), and hyphens (-).
        self.eip_name = eip_name
        # The line type. Valid values:
        # 
        # - **BGP** (default): BGP (multi-ISP) line. All regions support BGP (multi-ISP) EIPs.
        # - **BGP_PRO**: BGP (multi-ISP) Pro line. Only Hong Kong (China), Singapore, Tokyo (Japan), Kuala Lumpur (Malaysia), Manila (Philippines), Jakarta (Indonesia), and Bangkok (Thailand) regions support BGP (multi-ISP) Pro EIPs.
        # 
        # For more information about BGP (multi-ISP) and BGP (multi-ISP) Pro lines, see [EIP line types](https://help.aliyun.com/document_detail/32321.html).
        # 
        # If you are a whitelist user of single-ISP bandwidth, you can also specify the following values:
        # - **ChinaTelecom**: China Telecom
        # - **ChinaUnicom**: China Unicom
        # - **ChinaMobile**: China Mobile
        # - **ChinaTelecom_L2**: China Telecom L2
        # - **ChinaUnicom_L2**: China Unicom L2
        # - **ChinaMobile_L2**: China Mobile L2
        # 
        # If you are a user of Alibaba Finance Cloud in the China (Hangzhou) region, this parameter is required. Set the value to **BGP_FinanceCloud**.
        self.isp = isp
        # Specifies whether to include pending order data. Valid values:
        # 
        # - **false** (default): Does not include pending order data.
        # 
        # - **true**: Includes pending order data.
        self.include_reservation_data = include_reservation_data
        # The lock type. Valid values:
        # 
        # - **financial**: locked due to overdue payment.
        # 
        # - **security**: locked for security reasons.
        self.lock_reason = lock_reason
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the list. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page in a paged query. Maximum value: **100**. Default value: **10**.
        self.page_size = page_size
        # The ID of the IP address pool to which the EIP belongs.
        self.public_ip_address_pool_id = public_ip_address_pool_id
        # The region ID of the EIP.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the EIP belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Indicates whether Anti-DDoS (Enhanced) is enabled. Valid values:
        # - **false**: not enabled.
        # - **true**: enabled.
        self.security_protection_enabled = security_protection_enabled
        # The instance ID of the contiguous EIP group.
        self.segment_instance_id = segment_instance_id
        # Specifies whether the instance is a managed instance. Valid values:
        # - **true**: a managed instance.
        # - **false**: not a managed instance.
        # 
        # If you leave this parameter empty, all instances are queried.
        self.service_managed = service_managed
        # The status of the EIP. Valid values:
        # 
        # - **Associating**: being associated.
        # 
        # - **Unassociating**: being disassociated.
        # 
        # - **InUse**: allocated.
        # 
        # - **Available**: available.
        # - **Releasing**: being released.
        self.status = status
        # The tags used to filter EIPs.
        self.tag = tag

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.associated_instance_id is not None:
            result['AssociatedInstanceId'] = self.associated_instance_id

        if self.associated_instance_type is not None:
            result['AssociatedInstanceType'] = self.associated_instance_type

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.eip_address is not None:
            result['EipAddress'] = self.eip_address

        if self.eip_name is not None:
            result['EipName'] = self.eip_name

        if self.isp is not None:
            result['ISP'] = self.isp

        if self.include_reservation_data is not None:
            result['IncludeReservationData'] = self.include_reservation_data

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.public_ip_address_pool_id is not None:
            result['PublicIpAddressPoolId'] = self.public_ip_address_pool_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_protection_enabled is not None:
            result['SecurityProtectionEnabled'] = self.security_protection_enabled

        if self.segment_instance_id is not None:
            result['SegmentInstanceId'] = self.segment_instance_id

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.DescribeEipAddressesRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('AssociatedInstanceId') is not None:
            self.associated_instance_id = m.get('AssociatedInstanceId')

        if m.get('AssociatedInstanceType') is not None:
            self.associated_instance_type = m.get('AssociatedInstanceType')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EipAddress') is not None:
            self.eip_address = m.get('EipAddress')

        if m.get('EipName') is not None:
            self.eip_name = m.get('EipName')

        if m.get('ISP') is not None:
            self.isp = m.get('ISP')

        if m.get('IncludeReservationData') is not None:
            self.include_reservation_data = m.get('IncludeReservationData')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PublicIpAddressPoolId') is not None:
            self.public_ip_address_pool_id = m.get('PublicIpAddressPoolId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityProtectionEnabled') is not None:
            self.security_protection_enabled = m.get('SecurityProtectionEnabled')

        if m.get('SegmentInstanceId') is not None:
            self.segment_instance_id = m.get('SegmentInstanceId')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeEipAddressesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeEipAddressesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # A tag key can be up to 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # A tag value can be up to 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeEipAddressesRequestFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The filter key for querying resources. Set the value to **CreationStartTime**, which specifies the start time when the resource was created.
        self.key = key
        # The filter value for querying resources. Specify the value in UTC. Format: `YYYY-MM-DDThh:mmZ`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

