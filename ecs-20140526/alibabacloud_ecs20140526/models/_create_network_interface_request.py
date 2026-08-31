# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreateNetworkInterfaceRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        client_token: str = None,
        connection_tracking_configuration: main_models.CreateNetworkInterfaceRequestConnectionTrackingConfiguration = None,
        delete_on_release: bool = None,
        description: str = None,
        enable_primary_ipv_6: bool = None,
        enhanced_network: main_models.CreateNetworkInterfaceRequestEnhancedNetwork = None,
        instance_type: str = None,
        ipv_4prefix: List[str] = None,
        ipv_4prefix_count: int = None,
        ipv_6address: List[str] = None,
        ipv_6address_count: int = None,
        ipv_6prefix: List[str] = None,
        ipv_6prefix_count: int = None,
        network_interface_name: str = None,
        network_interface_traffic_config: main_models.CreateNetworkInterfaceRequestNetworkInterfaceTrafficConfig = None,
        network_interface_traffic_mode: str = None,
        owner_account: str = None,
        owner_id: int = None,
        primary_ip_address: str = None,
        private_ip_address: List[str] = None,
        queue_number: int = None,
        queue_pair_number: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        rx_queue_size: int = None,
        secondary_private_ip_address_count: int = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        source_dest_check: bool = None,
        tag: List[main_models.CreateNetworkInterfaceRequestTag] = None,
        tx_queue_size: int = None,
        v_switch_id: str = None,
        visible: bool = None,
    ):
        # > This parameter is deprecated.
        self.business_type = business_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The network connectivity tracking configuration.
        # 
        # Before you use this parameter, read [Connection timeout management](https://help.aliyun.com/document_detail/2865958.html).
        self.connection_tracking_configuration = connection_tracking_configuration
        # Specifies whether to retain the ENI when the associated instance is released. Valid values:
        # 
        # - true: does not retain the ENI.
        # 
        # - false: retains the ENI.
        self.delete_on_release = delete_on_release
        # The description of the network interface controller (NIC). The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        # 
        # Default value: empty.
        self.description = description
        self.enable_primary_ipv_6 = enable_primary_ipv_6
        # > This parameter is not publicly available.
        self.enhanced_network = enhanced_network
        # The type of the Elastic Network Interface (ENI). Valid values:
        # 
        # - Secondary: secondary ENI.
        # - Trunk: trunk network interface controller (NIC) (in invitational preview).
        # 
        # Default value: Secondary.
        self.instance_type = instance_type
        # One or more IPv4 prefixes to assign to the network interface controller (NIC). Valid values of N: 1 to 10.
        # > If you want to set IPv4 prefixes for the network interface controller (NIC), you must set either the parameter Ipv4Prefix.N or the parameter Ipv4PrefixCount but not both.
        self.ipv_4prefix = ipv_4prefix
        # The number of IPv4 prefixes to assign to the network interface controller (NIC). Valid values: 1 to 10.
        # > If you want to set IPv4 prefixes for the network interface controller (NIC), you must set either the parameter Ipv4Prefix.N or the parameter Ipv4PrefixCount but not both.
        self.ipv_4prefix_count = ipv_4prefix_count
        # One or more IPv6 addresses to assign to the network interface controller (NIC). You can specify up to 10 IPv6 addresses. Valid values of N: 1 to 10.
        # 
        # Example: Ipv6Address.1=2001:db8:1234:1a00::\\*\\*\\*\\*
        # 
        # > If you want to set IPv6 addresses for the network interface controller (NIC), you must set either the parameter `Ipv6Addresses.N` or the parameter `Ipv6AddressCount` but not both.
        self.ipv_6address = ipv_6address
        # The number of IPv6 addresses to randomly generate for the network interface controller (NIC). Valid values: 1 to 10.
        # 
        # > If you want to set IPv6 addresses for the network interface controller (NIC), you must set either the parameter `Ipv6Addresses.N` or the parameter `Ipv6AddressCount` but not both.
        self.ipv_6address_count = ipv_6address_count
        # One or more IPv6 prefixes to assign to the network interface controller (NIC). Valid values of N: 1 to 10.
        # > If you want to set IPv6 prefixes for the network interface controller (NIC), you must set either the parameter Ipv6Prefix.N or the parameter Ipv6PrefixCount but not both.
        self.ipv_6prefix = ipv_6prefix
        # The number of IPv6 prefixes to assign to the network interface controller (NIC). Valid values: 1 to 10.
        # > If you want to set IPv6 prefixes for the network interface controller (NIC), you must set either the parameter Ipv6Prefix.N or the parameter Ipv6PrefixCount but not both.
        self.ipv_6prefix_count = ipv_6prefix_count
        # The name of the network interface controller (NIC). The name must be 2 to 128 characters in length and can contain characters from the Unicode letter categorization (including English and Chinese characters) and ASCII digits (0-9). The name can contain colons (:), underscores (_), periods (.), or hyphens (-).
        # 
        # Default value: empty.
        self.network_interface_name = network_interface_name
        # The traffic configuration parameter set of the network interface controller (NIC).
        self.network_interface_traffic_config = network_interface_traffic_config
        # The communication pattern of the network interface controller (NIC). Valid values:
        # 
        # - Standard: uses the TCP communication pattern.
        # - HighPerformance: enables the Elastic RDMA Interface (ERI) and uses the RDMA communication pattern.
        # 
        # > A network interface controller (NIC) in RDMA communication pattern can be attached only to an instance whose instance type supports ERI. The number of ENIs in RDMA pattern cannot exceed the limit of the instance family. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html) and [Configure eRDMA on enterprise-level instances](https://help.aliyun.com/document_detail/336853.html)<props="china"> and [Configure eRDMA on GPU-accelerated instances](https://help.aliyun.com/document_detail/2248432.html).
        # 
        # Default value: Standard.
        self.network_interface_traffic_mode = network_interface_traffic_mode
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The primary private IP address of the network interface controller (NIC).
        # 
        # The specified IP address must be an idle address within the CIDR block of the vSwitch. If you do not specify this parameter, an idle private IP address in the vSwitch CIDR block is randomly allocated by default.
        self.primary_ip_address = primary_ip_address
        # One or more secondary private IP addresses selected from the idle addresses within the CIDR block of the vSwitch to which the network interface controller (NIC) belongs. Valid values of N: 0 to 10.
        # 
        # > When you allocate secondary private IP addresses, you cannot specify both the parameter `PrivateIpAddress.N` and the parameter `SecondaryPrivateIpAddressCount` at the same time.
        self.private_ip_address = private_ip_address
        # The number of queues for the network interface controller (NIC). Valid values: 1 to 2048.
        # 
        # When you attach the ENI to an instance, the value must be less than the maximum number of queues per network interface controller (NIC) supported by the instance type. You can call [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) to query the `MaximumQueueNumberPerEni` field.
        # 
        # Default value: empty. When the ENI is attached, the default queue number for the instance type is used. You can call [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) to query the `SecondaryEniQueueNumber` field.
        self.queue_number = queue_number
        # The number of queues for the RDMA ENI.
        # 
        # If you want to attach multiple RDMA ENIs to an instance, we recommend that you manually specify QueuePairNumber for each ENI based on the upper limit of `QueuePairNumber` supported by the instance type and the number of ENIs you plan to use. Make sure that the total QueuePairNumber of all ENIs does not exceed the maximum value allowed by the instance type. Call [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) to query the upper limit for the instance type.
        # 
        # >Notice: If QueuePairNumber is not specified for an RDMA ENI, the upper limit of QueuePairNumber for all RDMA ENIs supported by the instance type is used by default. Therefore, after an RDMA ENI without a specified QueuePairNumber is attached, no more RDMA ENIs can be added (regular ENIs are not affected by this limit).</notice>
        self.queue_pair_number = queue_pair_number
        # The region ID of the network interface controller (NIC) to create. You can invoke [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID. You can call [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) to query resource group information.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The inbound queue depth of the network interface controller (NIC).
        # 
        # Take note of the following items:
        # 
        # - The inbound queue depth of the network interface controller (NIC) must be equal to the outbound queue depth. Valid values: 8192 to 16384. The value must be a power of 2.
        # 
        # - A larger inbound queue depth increases inbound throughput but consumes more memory.
        # 
        # > This parameter is not publicly available.
        self.rx_queue_size = rx_queue_size
        # The number of private IP addresses for automatic creation by ECS. Valid values: 1 to 49.
        self.secondary_private_ip_address_count = secondary_private_ip_address_count
        # The ID of the security group to which the network interface controller (NIC) belongs. The security group and the ENI must be in the same VPC.
        # 
        # > When you invoke this operation, you must set either `SecurityGroupId` or `SecurityGroupIds.N` but not both.
        self.security_group_id = security_group_id
        # The IDs of one or more security groups to which the network interface controller (NIC) belongs. The security groups and the ENI must be in the same VPC. The valid values of N depend on the quota for the maximum number of security groups to which an ENI can belong. For more information, see [Limits](https://help.aliyun.com/document_detail/25412.html).
        # 
        # > When you invoke this operation, you must set either `SecurityGroupId` or `SecurityGroupIds.N` but not both.
        self.security_group_ids = security_group_ids
        # Specifies whether to enable source/destination checking. We recommend that you enable this feature to improve network security. Valid values:
        # 
        # - true: enabled.
        # 
        # - false: disabled.
        # 
        # Default value: false.
        # 
        # > This feature is supported only in specific regions. Before you use this feature, read [Source/destination checking](https://help.aliyun.com/document_detail/2863210.html).
        self.source_dest_check = source_dest_check
        # The tags of the network interface controller (NIC).
        self.tag = tag
        # The outbound queue depth of the network interface controller (NIC).
        # 
        # Take note of the following items:
        # 
        # - The outbound queue depth of the network interface controller (NIC) must be equal to the inbound queue depth. Valid values: 8192 to 16384. The value must be a power of 2.
        # 
        # - A larger outbound queue depth increases outbound throughput but consumes more memory.
        # 
        # > This parameter is not publicly available.
        self.tx_queue_size = tx_queue_size
        # The vSwitch ID of the network interface controller (NIC). The private IP address of the ENI is allocated from the idle addresses within the CIDR block of the vSwitch.
        # 
        # >Notice: The network interface controller (NIC) and the instance to which you want to attach the ENI must be in the same zone but can belong to different vSwitches.</notice>
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # > This parameter is deprecated.
        self.visible = visible

    def validate(self):
        if self.connection_tracking_configuration:
            self.connection_tracking_configuration.validate()
        if self.enhanced_network:
            self.enhanced_network.validate()
        if self.network_interface_traffic_config:
            self.network_interface_traffic_config.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.connection_tracking_configuration is not None:
            result['ConnectionTrackingConfiguration'] = self.connection_tracking_configuration.to_map()

        if self.delete_on_release is not None:
            result['DeleteOnRelease'] = self.delete_on_release

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_primary_ipv_6 is not None:
            result['EnablePrimaryIPv6'] = self.enable_primary_ipv_6

        if self.enhanced_network is not None:
            result['EnhancedNetwork'] = self.enhanced_network.to_map()

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.ipv_4prefix is not None:
            result['Ipv4Prefix'] = self.ipv_4prefix

        if self.ipv_4prefix_count is not None:
            result['Ipv4PrefixCount'] = self.ipv_4prefix_count

        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count

        if self.ipv_6prefix is not None:
            result['Ipv6Prefix'] = self.ipv_6prefix

        if self.ipv_6prefix_count is not None:
            result['Ipv6PrefixCount'] = self.ipv_6prefix_count

        if self.network_interface_name is not None:
            result['NetworkInterfaceName'] = self.network_interface_name

        if self.network_interface_traffic_config is not None:
            result['NetworkInterfaceTrafficConfig'] = self.network_interface_traffic_config.to_map()

        if self.network_interface_traffic_mode is not None:
            result['NetworkInterfaceTrafficMode'] = self.network_interface_traffic_mode

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.primary_ip_address is not None:
            result['PrimaryIpAddress'] = self.primary_ip_address

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.queue_number is not None:
            result['QueueNumber'] = self.queue_number

        if self.queue_pair_number is not None:
            result['QueuePairNumber'] = self.queue_pair_number

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.rx_queue_size is not None:
            result['RxQueueSize'] = self.rx_queue_size

        if self.secondary_private_ip_address_count is not None:
            result['SecondaryPrivateIpAddressCount'] = self.secondary_private_ip_address_count

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        if self.source_dest_check is not None:
            result['SourceDestCheck'] = self.source_dest_check

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.tx_queue_size is not None:
            result['TxQueueSize'] = self.tx_queue_size

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.visible is not None:
            result['Visible'] = self.visible

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConnectionTrackingConfiguration') is not None:
            temp_model = main_models.CreateNetworkInterfaceRequestConnectionTrackingConfiguration()
            self.connection_tracking_configuration = temp_model.from_map(m.get('ConnectionTrackingConfiguration'))

        if m.get('DeleteOnRelease') is not None:
            self.delete_on_release = m.get('DeleteOnRelease')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnablePrimaryIPv6') is not None:
            self.enable_primary_ipv_6 = m.get('EnablePrimaryIPv6')

        if m.get('EnhancedNetwork') is not None:
            temp_model = main_models.CreateNetworkInterfaceRequestEnhancedNetwork()
            self.enhanced_network = temp_model.from_map(m.get('EnhancedNetwork'))

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Ipv4Prefix') is not None:
            self.ipv_4prefix = m.get('Ipv4Prefix')

        if m.get('Ipv4PrefixCount') is not None:
            self.ipv_4prefix_count = m.get('Ipv4PrefixCount')

        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')

        if m.get('Ipv6Prefix') is not None:
            self.ipv_6prefix = m.get('Ipv6Prefix')

        if m.get('Ipv6PrefixCount') is not None:
            self.ipv_6prefix_count = m.get('Ipv6PrefixCount')

        if m.get('NetworkInterfaceName') is not None:
            self.network_interface_name = m.get('NetworkInterfaceName')

        if m.get('NetworkInterfaceTrafficConfig') is not None:
            temp_model = main_models.CreateNetworkInterfaceRequestNetworkInterfaceTrafficConfig()
            self.network_interface_traffic_config = temp_model.from_map(m.get('NetworkInterfaceTrafficConfig'))

        if m.get('NetworkInterfaceTrafficMode') is not None:
            self.network_interface_traffic_mode = m.get('NetworkInterfaceTrafficMode')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrimaryIpAddress') is not None:
            self.primary_ip_address = m.get('PrimaryIpAddress')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('QueueNumber') is not None:
            self.queue_number = m.get('QueueNumber')

        if m.get('QueuePairNumber') is not None:
            self.queue_pair_number = m.get('QueuePairNumber')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RxQueueSize') is not None:
            self.rx_queue_size = m.get('RxQueueSize')

        if m.get('SecondaryPrivateIpAddressCount') is not None:
            self.secondary_private_ip_address_count = m.get('SecondaryPrivateIpAddressCount')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        if m.get('SourceDestCheck') is not None:
            self.source_dest_check = m.get('SourceDestCheck')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateNetworkInterfaceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TxQueueSize') is not None:
            self.tx_queue_size = m.get('TxQueueSize')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('Visible') is not None:
            self.visible = m.get('Visible')

        return self

class CreateNetworkInterfaceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the network interface controller (NIC). Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with aliyun or acs:. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the network interface controller (NIC). Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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

class CreateNetworkInterfaceRequestNetworkInterfaceTrafficConfig(DaraModel):
    def __init__(
        self,
        network_interface_traffic_mode: str = None,
        queue_number: int = None,
        queue_pair_number: int = None,
        rx_queue_size: int = None,
        tx_queue_size: int = None,
    ):
        # The communication pattern of the network interface controller (NIC).
        self.network_interface_traffic_mode = network_interface_traffic_mode
        # The number of queues for the network interface controller (NIC).
        self.queue_number = queue_number
        # The number of queues for the RDMA ENI.
        self.queue_pair_number = queue_pair_number
        # The inbound queue depth of the network interface controller (NIC).
        # 
        # 
        # <props="china">
        # 
        # >This parameter is in invitational preview and is not publicly available. If you want to use this parameter, [submit a ticket](https://selfservice.console.aliyun.com/ticket/createIndex) to request access.
        # 
        # 
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is in invitational preview and is not publicly available. If you want to use this parameter, [submit a ticket](https://smartservice.console.aliyun.com/service/create-ticket-intl) to request access.
        # 
        # 
        # 
        # Take note of the following items:
        # 
        # - This parameter applies only to seventh-generation and later ECS instance types.
        # 
        # - This parameter currently applies only to Linux images.
        # 
        # - A larger inbound queue depth of the network interface controller (NIC) increases inbound throughput and reduces packet loss probability but consumes more memory.
        self.rx_queue_size = rx_queue_size
        # The outbound queue depth of the network interface controller (NIC).
        # 
        # 
        # <props="china">
        # 
        # >This parameter is in invitational preview and is not publicly available. If you want to use this parameter, [submit a ticket](https://selfservice.console.aliyun.com/ticket/createIndex) to request access.
        # 
        # 
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is in invitational preview and is not publicly available. If you want to use this parameter, [submit a ticket](https://smartservice.console.aliyun.com/service/create-ticket-intl) to request access.
        # 
        # 
        # 
        # Take note of the following items:
        # 
        # - This parameter applies only to seventh-generation and later ECS instance types.
        # 
        # - This parameter currently applies only to Linux images.
        # 
        # - A larger outbound queue depth of the network interface controller (NIC) increases outbound throughput and reduces packet loss probability but consumes more memory.
        self.tx_queue_size = tx_queue_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_interface_traffic_mode is not None:
            result['NetworkInterfaceTrafficMode'] = self.network_interface_traffic_mode

        if self.queue_number is not None:
            result['QueueNumber'] = self.queue_number

        if self.queue_pair_number is not None:
            result['QueuePairNumber'] = self.queue_pair_number

        if self.rx_queue_size is not None:
            result['RxQueueSize'] = self.rx_queue_size

        if self.tx_queue_size is not None:
            result['TxQueueSize'] = self.tx_queue_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkInterfaceTrafficMode') is not None:
            self.network_interface_traffic_mode = m.get('NetworkInterfaceTrafficMode')

        if m.get('QueueNumber') is not None:
            self.queue_number = m.get('QueueNumber')

        if m.get('QueuePairNumber') is not None:
            self.queue_pair_number = m.get('QueuePairNumber')

        if m.get('RxQueueSize') is not None:
            self.rx_queue_size = m.get('RxQueueSize')

        if m.get('TxQueueSize') is not None:
            self.tx_queue_size = m.get('TxQueueSize')

        return self

class CreateNetworkInterfaceRequestEnhancedNetwork(DaraModel):
    def __init__(
        self,
        enable_express: bool = None,
        enable_rss: bool = None,
        enable_sriov: bool = None,
        virtual_function_quantity: int = None,
        virtual_function_total_queue_number: int = None,
    ):
        self.enable_express = enable_express
        # > This parameter is not publicly available.
        self.enable_rss = enable_rss
        # > This parameter is not publicly available.
        self.enable_sriov = enable_sriov
        self.virtual_function_quantity = virtual_function_quantity
        self.virtual_function_total_queue_number = virtual_function_total_queue_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_express is not None:
            result['EnableExpress'] = self.enable_express

        if self.enable_rss is not None:
            result['EnableRss'] = self.enable_rss

        if self.enable_sriov is not None:
            result['EnableSriov'] = self.enable_sriov

        if self.virtual_function_quantity is not None:
            result['VirtualFunctionQuantity'] = self.virtual_function_quantity

        if self.virtual_function_total_queue_number is not None:
            result['VirtualFunctionTotalQueueNumber'] = self.virtual_function_total_queue_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableExpress') is not None:
            self.enable_express = m.get('EnableExpress')

        if m.get('EnableRss') is not None:
            self.enable_rss = m.get('EnableRss')

        if m.get('EnableSriov') is not None:
            self.enable_sriov = m.get('EnableSriov')

        if m.get('VirtualFunctionQuantity') is not None:
            self.virtual_function_quantity = m.get('VirtualFunctionQuantity')

        if m.get('VirtualFunctionTotalQueueNumber') is not None:
            self.virtual_function_total_queue_number = m.get('VirtualFunctionTotalQueueNumber')

        return self

class CreateNetworkInterfaceRequestConnectionTrackingConfiguration(DaraModel):
    def __init__(
        self,
        tcp_closed_and_time_wait_timeout: int = None,
        tcp_established_timeout: int = None,
        udp_timeout: int = None,
    ):
        # The timeout period for TCP connections in the TIME_WAIT and CLOSED states. Unit: seconds. Valid values: integers from 3 to 15.
        # 
        # Default value: 3.
        # 
        # > If your ECS instance is used with NLB/CLB, the default timeout period for connections in the `TIME_WAIT` state is 15 seconds.
        self.tcp_closed_and_time_wait_timeout = tcp_closed_and_time_wait_timeout
        # The timeout period for established TCP connections. Unit: seconds. Valid values: [30, 60, 80, 100, 200, 300, 500, 700, 910].
        # 
        # Default value: 910.
        self.tcp_established_timeout = tcp_established_timeout
        # The timeout period for UDP flows. Unit: seconds. Valid values: [10, 20, 30, 60, 80, 100].
        # 
        # Default value: 30.
        # 
        # > If your ECS instance is used with NLB/CLB, the default value is 100 seconds.
        self.udp_timeout = udp_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tcp_closed_and_time_wait_timeout is not None:
            result['TcpClosedAndTimeWaitTimeout'] = self.tcp_closed_and_time_wait_timeout

        if self.tcp_established_timeout is not None:
            result['TcpEstablishedTimeout'] = self.tcp_established_timeout

        if self.udp_timeout is not None:
            result['UdpTimeout'] = self.udp_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TcpClosedAndTimeWaitTimeout') is not None:
            self.tcp_closed_and_time_wait_timeout = m.get('TcpClosedAndTimeWaitTimeout')

        if m.get('TcpEstablishedTimeout') is not None:
            self.tcp_established_timeout = m.get('TcpEstablishedTimeout')

        if m.get('UdpTimeout') is not None:
            self.udp_timeout = m.get('UdpTimeout')

        return self

