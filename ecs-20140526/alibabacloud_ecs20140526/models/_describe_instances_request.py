# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesRequest(DaraModel):
    def __init__(
        self,
        filter: List[main_models.DescribeInstancesRequestFilter] = None,
        additional_attributes: List[str] = None,
        device_available: bool = None,
        dry_run: bool = None,
        eip_addresses: str = None,
        hpc_cluster_id: str = None,
        http_endpoint: str = None,
        http_put_response_hop_limit: int = None,
        http_tokens: str = None,
        image_id: str = None,
        inner_ip_addresses: str = None,
        instance_charge_type: str = None,
        instance_ids: str = None,
        instance_name: str = None,
        instance_network_type: str = None,
        instance_type: str = None,
        instance_type_family: str = None,
        internet_charge_type: str = None,
        io_optimized: bool = None,
        ipv_6address: List[str] = None,
        key_pair_name: str = None,
        lock_reason: str = None,
        max_results: int = None,
        need_sale_cycle: bool = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        private_ip_addresses: str = None,
        public_ip_addresses: str = None,
        rdma_ip_addresses: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_id: str = None,
        status: str = None,
        tag: List[main_models.DescribeInstancesRequestTag] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.filter = filter
        # The list of additional attributes of the instance.
        self.additional_attributes = additional_attributes
        # > This parameter is in invitational preview and is not publicly available.
        self.device_available = device_available
        # Specifies whether to perform only a dry run. Valid values:
        # 
        # - true: performs only a dry run. The system checks the request for potential issues, including invalid AccessKey pairs, unauthorized RAM users, and missing parameter values. If the request fails the dry run, the corresponding error is returned. If the request passes the dry run, the DryRunOperation error code is returned.  
        # - false: performs a dry run and sends the request. If the request passes the dry run, a 2XX HTTP status code is returned and the operation is performed. 
        # 
        # Default value: false.
        self.dry_run = dry_run
        # The Elastic IP Address (EIP) list of instances. This parameter takes effect when InstanceNetworkType is set to vpc. The value can be a JSON array that consists of up to 100 IP addresses. Separate the IP addresses with commas (,).
        self.eip_addresses = eip_addresses
        # The ID of the HPC cluster to which the instance belongs.
        self.hpc_cluster_id = hpc_cluster_id
        # Specifies whether the access channel for instance metadata is enabled. Valid values:
        # - enabled: enabled.
        # - disabled: disabled.
        # 
        # Default value: enabled.
        # > For more information about instance metadata, see [Overview of instance metadata](https://help.aliyun.com/document_detail/49122.html).
        self.http_endpoint = http_endpoint
        # > This parameter is not publicly available.
        self.http_put_response_hop_limit = http_put_response_hop_limit
        # Specifies whether the China mode (IMDSv2) is forcefully used for accessing instance metadata. Valid values:
        # - optional: not forcefully used.
        # - required: forcefully used. After this value is set, instance metadata cannot be accessed in normal mode.
        # 
        # Default value: optional.
        # > For more information about instance metadata access modes, see [Instance metadata access modes](https://help.aliyun.com/document_detail/150575.html).
        self.http_tokens = http_tokens
        # The image ID.
        self.image_id = image_id
        # The internal IP address list of instances in the classic network type. This parameter takes effect when InstanceNetworkType is set to classic. The value can be a JSON array that consists of up to 100 IP addresses. Separate the IP addresses with commas (,).
        self.inner_ip_addresses = inner_ip_addresses
        # The billing method of the instance. Valid values: 
        #          
        # - PostPaid: pay-as-you-go. 
        # - PrePaid: subscription.
        self.instance_charge_type = instance_charge_type
        # The IDs of instances. The value can be a JSON array that consists of up to 100 instance IDs. Separate the IDs with commas (,).
        self.instance_ids = instance_ids
        # The name of the instance. Fuzzy search with the wildcard * is supported.
        self.instance_name = instance_name
        # The network type of the instance. Valid values:
        # 
        # - classic: classic network.
        # - vpc: VPC.
        self.instance_network_type = instance_network_type
        # The instance type of the instance.
        self.instance_type = instance_type
        # The instance family of the instance.
        self.instance_type_family = instance_type_family
        # The billing method for public bandwidth. Valid values:
        # 
        # - PayByBandwidth: pay-by-bandwidth.
        # - PayByTraffic: pay-by-traffic.
        # 
        # > In **pay-by-traffic** mode, the peak inbound and outbound bandwidths are used as bandwidth upper limits and are not guaranteed. When resource contention occurs, the peak bandwidths may be limited. If you require guaranteed bandwidth, use the **pay-by-bandwidth** mode.
        self.internet_charge_type = internet_charge_type
        # Specifies whether the instance is I/O optimized. Valid values:
        # 
        # - true: The instance is I/O optimized.
        # - false: The instance is not I/O optimized.
        self.io_optimized = io_optimized
        # The IPv6 addresses assigned to the network interface controller (NIC).
        self.ipv_6address = ipv_6address
        # The name of the SSH key pair bound to the instance.
        self.key_pair_name = key_pair_name
        # The reason why the resource is locked. Valid values:
        # 
        # - financial: locked due to overdue payment.
        # 
        # - security: locked for security reasons.
        # 
        # - Recycling: the spot instance is pending release.
        # 
        # - dedicatedhostfinancial: the ECS instance is locked because the dedicated host has an overdue payment.
        # 
        # - refunded: locked due to a refund.
        self.lock_reason = lock_reason
        # The maximum number of entries per page for a paging query. Maximum value: 100.
        # 
        # Default value:
        # 
        # - If this parameter is not set or is set to a value smaller than 10, the default value is 10.
        # - If the value is greater than 100, the default value is 100.
        self.max_results = max_results
        # > This parameter is in invitational preview and is not publicly available.
        self.need_sale_cycle = need_sale_cycle
        # The query token. Set the value to the NextToken value returned in the previous API call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # > This parameter is about to go offline. Use NextToken and MaxResults to complete paging query operations.
        self.page_number = page_number
        # > This parameter is about to go offline. Use NextToken and MaxResults to complete paging query operations.
        self.page_size = page_size
        # The private IP addresses of instances whose network type is VPC. This parameter takes effect when InstanceNetworkType is set to vpc. The value can be a JSON array that consists of up to 100 IP addresses. Separate the IP addresses with commas (,).
        self.private_ip_addresses = private_ip_addresses
        # The public IP addresses of instances. The value can be a JSON array that consists of up to 100 IP addresses. Separate the IP addresses with commas (,).
        self.public_ip_addresses = public_ip_addresses
        # The RDMA IP address of the HPC instance.
        self.rdma_ip_addresses = rdma_ip_addresses
        # The region ID of the instance. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs. When you use this parameter to filter resources, the resource count cannot exceed 1,000.
        # 
        # > Filtering by the default resource group is not supported.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the security group to which the instance belongs.
        self.security_group_id = security_group_id
        # The instance status. Valid values: 
        # 
        # - Pending: being created.
        # - Running: running.
        # - Starting: being started.
        # - Stopping: being stopped.
        # - Stopped: stopped.
        self.status = status
        # The list of tags.
        self.tag = tag
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

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

        if self.additional_attributes is not None:
            result['AdditionalAttributes'] = self.additional_attributes

        if self.device_available is not None:
            result['DeviceAvailable'] = self.device_available

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.eip_addresses is not None:
            result['EipAddresses'] = self.eip_addresses

        if self.hpc_cluster_id is not None:
            result['HpcClusterId'] = self.hpc_cluster_id

        if self.http_endpoint is not None:
            result['HttpEndpoint'] = self.http_endpoint

        if self.http_put_response_hop_limit is not None:
            result['HttpPutResponseHopLimit'] = self.http_put_response_hop_limit

        if self.http_tokens is not None:
            result['HttpTokens'] = self.http_tokens

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.inner_ip_addresses is not None:
            result['InnerIpAddresses'] = self.inner_ip_addresses

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized

        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.need_sale_cycle is not None:
            result['NeedSaleCycle'] = self.need_sale_cycle

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.private_ip_addresses is not None:
            result['PrivateIpAddresses'] = self.private_ip_addresses

        if self.public_ip_addresses is not None:
            result['PublicIpAddresses'] = self.public_ip_addresses

        if self.rdma_ip_addresses is not None:
            result['RdmaIpAddresses'] = self.rdma_ip_addresses

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.DescribeInstancesRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('AdditionalAttributes') is not None:
            self.additional_attributes = m.get('AdditionalAttributes')

        if m.get('DeviceAvailable') is not None:
            self.device_available = m.get('DeviceAvailable')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EipAddresses') is not None:
            self.eip_addresses = m.get('EipAddresses')

        if m.get('HpcClusterId') is not None:
            self.hpc_cluster_id = m.get('HpcClusterId')

        if m.get('HttpEndpoint') is not None:
            self.http_endpoint = m.get('HttpEndpoint')

        if m.get('HttpPutResponseHopLimit') is not None:
            self.http_put_response_hop_limit = m.get('HttpPutResponseHopLimit')

        if m.get('HttpTokens') is not None:
            self.http_tokens = m.get('HttpTokens')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InnerIpAddresses') is not None:
            self.inner_ip_addresses = m.get('InnerIpAddresses')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')

        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NeedSaleCycle') is not None:
            self.need_sale_cycle = m.get('NeedSaleCycle')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrivateIpAddresses') is not None:
            self.private_ip_addresses = m.get('PrivateIpAddresses')

        if m.get('PublicIpAddresses') is not None:
            self.public_ip_addresses = m.get('PublicIpAddresses')

        if m.get('RdmaIpAddresses') is not None:
            self.rdma_ip_addresses = m.get('RdmaIpAddresses')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeInstancesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the instance. Valid values of N: 1 to 20.
        # 
        # If you use a single tag to filter resources, the resource count with the tag cannot exceed 1,000. If you use multiple tags to filter resources, the resource count that are attached to all specified tags cannot exceed 1,000. If the resource count exceeds 1,000, call the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation.
        self.key = key
        # The tag value of the instance. Valid values of N: 1 to 20.
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

class DescribeInstancesRequestFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The filter key for querying resources. The value must be `CreationStartTime`. Set both `Filter.1.Key` and `Filter.1.Value` to query resources created after a specified point in time.
        self.key = key
        # The filter value for querying resources. You must also specify the `Filter.1.Key` parameter when you specify this parameter. Specify the time in the `yyyy-MM-ddTHH:mmZ` format in UTC+0.
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

