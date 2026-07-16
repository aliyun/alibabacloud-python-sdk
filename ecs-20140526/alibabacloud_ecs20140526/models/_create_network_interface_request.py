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
        # A client token to ensure request idempotence. Your client generates this token, which must be unique across requests. The token can contain only ASCII characters and must not exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The connection tracking settings.
        # 
        # Before using this parameter, read [Connection timeout management](https://help.aliyun.com/document_detail/2865958.html).
        self.connection_tracking_configuration = connection_tracking_configuration
        # Specifies whether to release the elastic network interface when its attached instance is released. Valid values:
        # 
        # - `true`: The elastic network interface is released.
        # 
        # - `false`: The elastic network interface is retained.
        self.delete_on_release = delete_on_release
        # The description of the elastic network interface. The description must be 2 to 256 characters long and cannot start with `http://` or `https://`.
        # 
        # Default value: empty.
        self.description = description
        # > This parameter is not publicly available.
        self.enhanced_network = enhanced_network
        # The type of the elastic network interface. Valid values:
        # 
        # - `Secondary`: a secondary elastic network interface.
        # 
        # - `Trunk`: a trunk network interface. (This feature is available by invitation only.)
        # 
        # Default value: `Secondary`.
        self.instance_type = instance_type
        # One or more IPv4 prefixes to assign to the elastic network interface. Valid values of N: 1 to 10.
        # 
        # > You must specify either `Ipv4Prefix.N` or `Ipv4PrefixCount`, but not both, to assign IPv4 prefixes.
        self.ipv_4prefix = ipv_4prefix
        # The number of IPv4 prefixes to assign to the elastic network interface. Valid values: 1 to 10.
        # 
        # > You must specify either `Ipv4Prefix.N` or `Ipv4PrefixCount`, but not both, to assign IPv4 prefixes.
        self.ipv_4prefix_count = ipv_4prefix_count
        # One or more IPv6 addresses to assign to the elastic network interface. You can specify up to 10 IPv6 addresses. Valid values of N: 1 to 10.
        # 
        # Example: `Ipv6Address.1=2001:db8:1234:1a00::****`
        # 
        # > You must specify either `Ipv6Address.N` or `Ipv6AddressCount`, but not both, to assign IPv6 addresses.
        self.ipv_6address = ipv_6address
        # The number of random IPv6 addresses to assign to the elastic network interface. Valid values: 1 to 10.
        # 
        # > You must specify either `Ipv6Address.N` or `Ipv6AddressCount`, but not both, to assign IPv6 addresses.
        self.ipv_6address_count = ipv_6address_count
        # One or more IPv6 prefixes to assign to the elastic network interface. Valid values of N: 1 to 10.
        # 
        # > You must specify either `Ipv6Prefix.N` or `Ipv6PrefixCount`, but not both, to assign IPv6 prefixes.
        self.ipv_6prefix = ipv_6prefix
        # The number of IPv6 prefixes to assign to the elastic network interface. Valid values: 1 to 10.
        # 
        # > You must specify either `Ipv6Prefix.N` or `Ipv6PrefixCount`, but not both, to assign IPv6 prefixes.
        self.ipv_6prefix_count = ipv_6prefix_count
        # The name of the elastic network interface. The name must be 2 to 128 characters long and can contain Unicode letters (such as English and Chinese characters), digits (0-9), colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # Default value: empty.
        self.network_interface_name = network_interface_name
        # The communication parameters of the elastic network interface.
        self.network_interface_traffic_config = network_interface_traffic_config
        # The traffic mode of the elastic network interface. Valid values:
        # 
        # - `Standard`: uses the TCP traffic mode.
        # 
        # - `HighPerformance`: enables the Elastic RDMA Interface (ERI) and uses the RDMA traffic mode.
        # 
        # > An elastic network interface in RDMA traffic mode can be attached only to an ERI-supported instance type. The number of these elastic network interfaces that can be attached is limited by the instance family. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html), [Configure eRDMA on an enterprise-level instance](https://help.aliyun.com/document_detail/336853.html)<props="china">, and [Configure eRDMA on a GPU instance](https://help.aliyun.com/document_detail/2248432.html).
        # 
        # Default value: `Standard`.
        self.network_interface_traffic_mode = network_interface_traffic_mode
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The primary private IP address of the elastic network interface.
        # 
        # The IP address must be an available IP address within the CIDR block of the VSwitch. If this parameter is not specified, the system randomly assigns an available IP address from the VSwitch\\"s CIDR block.
        self.primary_ip_address = primary_ip_address
        # One or more secondary private IP addresses to assign to the elastic network interface. The IP addresses must be available addresses from the CIDR block of the VSwitch to which the elastic network interface belongs. Valid values of N: 0 to 10.
        # 
        # > You cannot specify both `PrivateIpAddress.N` and `SecondaryPrivateIpAddressCount` to assign secondary private IP addresses.
        self.private_ip_address = private_ip_address
        # The number of queues for the elastic network interface. Valid values: 1 to 2048.
        # 
        # When attached to an instance, this value must be less than the maximum number of queues per elastic network interface that the instance type supports. You can call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation and check the `MaximumQueueNumberPerEni` value in the response to query this limit.
        # 
        # If you do not specify this parameter, the default queue number for the instance type is used upon attachment.
        self.queue_number = queue_number
        # The number of queue pairs for the RDMA-enabled elastic network interface.
        # 
        # If you want to attach multiple RDMA-enabled elastic network interfaces to an instance, we recommend that you specify a `QueuePairNumber` value for each elastic network interface. The value should be based on the maximum `QueuePairNumber` value supported by the instance type and the number of elastic network interfaces that you plan to use. The total number of queue pairs for all elastic network interfaces cannot exceed the maximum value for the instance type. You can call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) operation to query the maximum value.
        # 
        # >Notice: 
        # 
        # If you do not specify `QueuePairNumber` for an RDMA-enabled elastic network interface, the system defaults to the maximum value that the instance type supports. Consequently, you cannot attach any more RDMA-enabled elastic network interfaces to that instance. This does not affect standard elastic network interfaces.
        self.queue_pair_number = queue_pair_number
        # The ID of the region in which to create the elastic network interface. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to view the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group. You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to query resource groups.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The receive (Rx) queue depth of the elastic network interface.
        # 
        # - The receive (Rx) and transmit (Tx) queue depths must be equal. The value must be a power of 2 between 8,192 and 16,384.
        # 
        # - A larger Rx queue depth can improve receive throughput but consumes more memory.
        # 
        # > This parameter is not publicly available.
        self.rx_queue_size = rx_queue_size
        # The number of secondary private IP addresses to automatically assign to the elastic network interface. Valid values: 1 to 49.
        self.secondary_private_ip_address_count = secondary_private_ip_address_count
        # The ID of the security group for the elastic network interface. The security group and the elastic network interface must be in the same VPC.
        # 
        # > You must specify either `SecurityGroupId` or `SecurityGroupIds.N`, but not both.
        self.security_group_id = security_group_id
        # The IDs of one or more security groups to which to add the elastic network interface. The security groups and the elastic network interface must be in the same VPC. The valid values of N depend on the maximum number of security groups to which an elastic network interface can be added. For more information, see [Limits](https://help.aliyun.com/document_detail/25412.html).
        # 
        # > You must specify either `SecurityGroupId` or `SecurityGroupIds.N`, but not both.
        self.security_group_ids = security_group_ids
        # Specifies whether to enable source/destination check. Enabling this feature enhances network security. Valid values:
        # 
        # - `true`: enabled.
        # 
        # - `false`: disabled.
        # 
        # Default value: false.
        # 
        # > This feature is available only in some regions. Before you use this feature, read [Source/destination check](https://help.aliyun.com/document_detail/2863210.html).
        self.source_dest_check = source_dest_check
        # The tags to add to the elastic network interface.
        self.tag = tag
        # The transmit (Tx) queue depth of the elastic network interface.
        # 
        # - The transmit (Tx) and receive (Rx) queue depths must be equal. The value must be a power of 2 between 8,192 and 16,384.
        # 
        # - A larger Tx queue depth can improve transmit throughput but consumes more memory.
        # 
        # > This parameter is not publicly available.
        self.tx_queue_size = tx_queue_size
        # The ID of the VSwitch for the elastic network interface. The private IP addresses for the elastic network interface are assigned from the available CIDR block of the VSwitch.
        # 
        # >Notice: 
        # 
        # The elastic network interface and the instance to be attached must be in the same availability zone but can belong to different VSwitches.
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
        # The key of the tag. Valid values for N: 1 to 20. The tag key cannot be an empty string. It can be up to 128 characters long and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The value of the tag. Valid values for N: 1 to 20. The tag value can be an empty string. It can be up to 128 characters long and cannot contain `http://` or `https://`.
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
        # The traffic mode of the elastic network interface.
        self.network_interface_traffic_mode = network_interface_traffic_mode
        # The number of queues for the elastic network interface.
        self.queue_number = queue_number
        # The number of queue pairs for the RDMA-enabled elastic network interface.
        self.queue_pair_number = queue_pair_number
        # The receive (Rx) queue depth of the elastic network interface.
        # 
        # <props="china">
        # 
        # > This parameter is available by invitation only. To request access, submit a ticket.
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is available by invitation only. To request access, submit a ticket.
        # 
        # 
        # 
        # - This parameter is applicable only to seventh-generation or later ECS instance types.
        # 
        # - This parameter is applicable only to Linux images.
        # 
        # - A larger Rx queue depth can improve receive throughput and reduce the packet loss rate, but consumes more memory.
        self.rx_queue_size = rx_queue_size
        # The transmit (Tx) queue depth of the elastic network interface.
        # 
        # <props="china">
        # 
        # > This parameter is available by invitation only. To request access, submit a ticket.
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is available by invitation only. To request access, submit a ticket.
        # 
        # 
        # 
        # - This parameter is applicable only to seventh-generation or later ECS instance types.
        # 
        # - This parameter is applicable only to Linux images.
        # 
        # - A larger Tx queue depth can improve transmit throughput and reduce the packet loss rate, but consumes more memory.
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
        enable_rss: bool = None,
        enable_sriov: bool = None,
        virtual_function_quantity: int = None,
        virtual_function_total_queue_number: int = None,
    ):
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
        # The timeout for a TCP connection in the TIME_WAIT or closing state, in seconds. Valid values: integers from 3 to 15.
        # 
        # Default value: 3.
        # 
        # > If your ECS instance works with NLB or CLB, the default timeout period for connections in the `TIME_WAIT` state is 15 seconds.
        self.tcp_closed_and_time_wait_timeout = tcp_closed_and_time_wait_timeout
        # The timeout for an established TCP connection, in seconds. Valid values: 30, 60, 80, 100, 200, 300, 500, 700, and 910.
        # 
        # Default value: 910.
        self.tcp_established_timeout = tcp_established_timeout
        # The timeout for a UDP stream, in seconds. Valid values: 10, 20, 30, 60, 80, and 100.
        # 
        # Default value: 30.
        # 
        # > If your ECS instance works with NLB or CLB, the default value is 100 seconds.
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

