# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ModifyNetworkInterfaceAttributeRequest(DaraModel):
    def __init__(
        self,
        connection_tracking_configuration: main_models.ModifyNetworkInterfaceAttributeRequestConnectionTrackingConfiguration = None,
        delete_on_release: bool = None,
        description: str = None,
        enable_primary_ipv_6: bool = None,
        enhanced_network: main_models.ModifyNetworkInterfaceAttributeRequestEnhancedNetwork = None,
        network_interface_id: str = None,
        network_interface_name: str = None,
        network_interface_traffic_config: main_models.ModifyNetworkInterfaceAttributeRequestNetworkInterfaceTrafficConfig = None,
        owner_account: str = None,
        owner_id: int = None,
        queue_number: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        rx_queue_size: int = None,
        security_group_id: List[str] = None,
        source_dest_check: bool = None,
        tx_queue_size: int = None,
    ):
        # The network connectivity tracking configuration information collection.
        # 
        # Before you use this parameter, read [Connection timeout management](https://help.aliyun.com/document_detail/2865958.html) carefully.
        self.connection_tracking_configuration = connection_tracking_configuration
        # Specifies whether to retain the ENI when the instance is released. Valid values:
        # 
        # - true: The ENI is not retained.
        # 
        # - false: The ENI is retained.
        self.delete_on_release = delete_on_release
        # The description of the network interface controller (NIC). The description must be 2 to 255 characters in length and cannot start with `http://` or `https://`.
        # 
        # Default value: empty.
        self.description = description
        # Specifies whether to enable the primary IPv6 address for the network interface controller (NIC).
        self.enable_primary_ipv_6 = enable_primary_ipv_6
        # This parameter is not available for public use.
        self.enhanced_network = enhanced_network
        # The ID of the network interface controller (NIC).
        # 
        # This parameter is required.
        self.network_interface_id = network_interface_id
        # The name of the Elastic Network Interface (ENI). The name must be 2 to 128 characters in length and must start with a letter or a Chinese character. It cannot start with `http://` or `https://`. It supports characters in the Letter category of Unicode, such as English letters, Chinese characters, and digits. It can contain colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # Default value: empty.
        self.network_interface_name = network_interface_name
        # The traffic parameters of the network interface controller (NIC).
        self.network_interface_traffic_config = network_interface_traffic_config
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of queues for the ENI. Valid values: 1 to 2048.
        # 
        # - You can modify the number of queues for an ENI that is in the `Available` state, or for an ENI that is attached (`InUse`) to an instance that is in the `Stopped` state.
        # 
        # - The number of queues for the ENI cannot exceed the maximum number of queues per ENI allowed by the instance type. The total number of queues for all ENIs attached to the instance cannot exceed the total queue quota allowed by the instance type. You can call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation and query the `MaximumQueueNumberPerEni` and `TotalEniQueueQuantity` parameters to obtain the maximum number of queues per ENI and the total queue quota for the instance type.
        self.queue_number = queue_number
        # The region ID of the network interface controller (NIC). You can invoke the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The inbound queue depth of the network interface controller (NIC).
        # 
        # > This parameter is in invitational preview and is not available for public use. If you need to use it, submit a ticket to apply for whitelist access.
        # 
        # Take note of the following items:
        # 
        # - This parameter applies only to seventh-generation and later ECS instance types.
        # - This parameter currently applies only to Linux images.
        # - A larger inbound queue depth can increase inbound throughput and reduce the packet loss rate, but it consumes more memory.
        self.rx_queue_size = rx_queue_size
        # The list of security group IDs. The secondary network interface controller (NIC) is added to the specified security groups and removed from its current security groups.
        # 
        # - The valid values of N depend on the quota of security groups that each network interface controller (NIC) can join. For more information, see [Limits](~~25412#SecurityGroupQuota~~).
        # 
        # - The modification takes effect shortly, but there may be a slight delay.
        self.security_group_id = security_group_id
        # Specifies whether to enable source/destination checking. We recommend that you enable this feature to improve network security. Valid values:
        # 
        # - true: enabled.
        # 
        # - false: disabled.
        # 
        # Default value: false.
        # 
        # > This feature is supported only in specific regions. Before you use it, read [Source/destination checking](https://help.aliyun.com/document_detail/2863210.html) carefully.
        self.source_dest_check = source_dest_check
        # The outbound queue depth of the network interface controller (NIC).
        # 
        # > This parameter is in invitational preview and is not available for public use. If you need to use it, submit a ticket to apply for whitelist access.
        # 
        # Take note of the following items:
        # 
        # - This parameter applies only to seventh-generation and later ECS instance types.
        # - This parameter currently applies only to Linux images.
        # - A larger outbound queue depth can increase outbound throughput and reduce the packet loss rate, but it consumes more memory.
        self.tx_queue_size = tx_queue_size

    def validate(self):
        if self.connection_tracking_configuration:
            self.connection_tracking_configuration.validate()
        if self.enhanced_network:
            self.enhanced_network.validate()
        if self.network_interface_traffic_config:
            self.network_interface_traffic_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.network_interface_name is not None:
            result['NetworkInterfaceName'] = self.network_interface_name

        if self.network_interface_traffic_config is not None:
            result['NetworkInterfaceTrafficConfig'] = self.network_interface_traffic_config.to_map()

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.queue_number is not None:
            result['QueueNumber'] = self.queue_number

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.rx_queue_size is not None:
            result['RxQueueSize'] = self.rx_queue_size

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.source_dest_check is not None:
            result['SourceDestCheck'] = self.source_dest_check

        if self.tx_queue_size is not None:
            result['TxQueueSize'] = self.tx_queue_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionTrackingConfiguration') is not None:
            temp_model = main_models.ModifyNetworkInterfaceAttributeRequestConnectionTrackingConfiguration()
            self.connection_tracking_configuration = temp_model.from_map(m.get('ConnectionTrackingConfiguration'))

        if m.get('DeleteOnRelease') is not None:
            self.delete_on_release = m.get('DeleteOnRelease')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnablePrimaryIPv6') is not None:
            self.enable_primary_ipv_6 = m.get('EnablePrimaryIPv6')

        if m.get('EnhancedNetwork') is not None:
            temp_model = main_models.ModifyNetworkInterfaceAttributeRequestEnhancedNetwork()
            self.enhanced_network = temp_model.from_map(m.get('EnhancedNetwork'))

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('NetworkInterfaceName') is not None:
            self.network_interface_name = m.get('NetworkInterfaceName')

        if m.get('NetworkInterfaceTrafficConfig') is not None:
            temp_model = main_models.ModifyNetworkInterfaceAttributeRequestNetworkInterfaceTrafficConfig()
            self.network_interface_traffic_config = temp_model.from_map(m.get('NetworkInterfaceTrafficConfig'))

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('QueueNumber') is not None:
            self.queue_number = m.get('QueueNumber')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RxQueueSize') is not None:
            self.rx_queue_size = m.get('RxQueueSize')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SourceDestCheck') is not None:
            self.source_dest_check = m.get('SourceDestCheck')

        if m.get('TxQueueSize') is not None:
            self.tx_queue_size = m.get('TxQueueSize')

        return self

class ModifyNetworkInterfaceAttributeRequestNetworkInterfaceTrafficConfig(DaraModel):
    def __init__(
        self,
        network_interface_traffic_mode: str = None,
        queue_number: int = None,
        queue_pair_number: int = None,
        rx_queue_size: int = None,
        tx_queue_size: int = None,
    ):
        # The traffic pattern of the network interface controller (NIC). Valid values of the parameter:
        # 
        # - Standard: uses the TCP traffic pattern.
        # - HighPerformance: enables the Elastic RDMA Interface (ERI) and uses the RDMA traffic pattern.
        # 
        # When the Elastic Network Interface (ENI) is attached to an instance, take note of the following items:
        # - The total number of RDMA network interface controllers (NICs) for the instance cannot exceed the RDMA network interface controller (NIC) quota allowed by the instance type. You can invoke the DescribeInstanceTypes operation and query the EriQuantity parameter to obtain the RDMA network interface controller (NIC) quota for the instance type.
        # 
        # > This parameter is in invitational preview and is not available for public use.
        self.network_interface_traffic_mode = network_interface_traffic_mode
        # The number of queues for the network interface controller (NIC).
        # When the Elastic Network Interface (ENI) is attached to an instance, take note of the following items:
        # - The number of queues cannot exceed the maximum number of queues per network interface controller (NIC) allowed by the instance type.
        # - The total number of queues for all network interface controllers (NICs) attached to the instance cannot exceed the total queue quota allowed by the instance type. You can invoke the DescribeInstanceTypes operation and query the MaximumQueueNumberPerEni and TotalEniQueueQuantity parameters to obtain the maximum number of queues per network interface controller (NIC) and the total queue quota for the instance type.
        # 
        # > This parameter is in invitational preview and is not available for public use.
        self.queue_number = queue_number
        # The number of queues for the RDMA network interface controller (NIC).
        # When the Elastic Network Interface (ENI) is attached to an instance, take note of the following items:
        # - The number of queues cannot exceed the maximum number of queues per RDMA network interface controller (NIC) allowed by the instance type. You can invoke the DescribeInstanceTypes operation and query the QueuePairNumber parameter to obtain the maximum number of queues per RDMA network interface controller (NIC) for the instance type.
        # 
        # > This parameter is in invitational preview and is not available for public use.
        self.queue_pair_number = queue_pair_number
        # The inbound queue depth of the network interface controller (NIC).
        # 
        # > This parameter is in invitational preview and is not available for public use. If you need to use it, submit a ticket to apply for whitelist access.
        # 
        # Take note of the following items:
        # 
        # - This parameter applies only to seventh-generation and later ECS instance types.
        # - This parameter currently applies only to Linux images.
        # - A larger inbound queue depth can increase inbound throughput and reduce the packet loss rate, but it consumes more memory.
        self.rx_queue_size = rx_queue_size
        # The outbound queue depth of the network interface controller (NIC).
        # 
        # > This parameter is in invitational preview and is not available for public use. If you need to use it, submit a ticket to apply for whitelist access.
        # 
        # Take note of the following items:
        # 
        # - This parameter applies only to seventh-generation and later ECS instance types.
        # - This parameter currently applies only to Linux images.
        # - A larger outbound queue depth can increase outbound throughput and reduce the packet loss rate, but it consumes more memory.
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

class ModifyNetworkInterfaceAttributeRequestEnhancedNetwork(DaraModel):
    def __init__(
        self,
        enable_express: bool = None,
        enable_rss: bool = None,
        enable_sriov: bool = None,
        virtual_function_quantity: int = None,
        virtual_function_total_queue_number: int = None,
    ):
        # > This parameter is not available for public use.
        self.enable_express = enable_express
        # > This parameter is not available for public use.
        self.enable_rss = enable_rss
        # This parameter is not available for public use.
        self.enable_sriov = enable_sriov
        # The number of virtual functions when SR-IOV is enabled. Valid values: 1 to 256.
        self.virtual_function_quantity = virtual_function_quantity
        # The total number of queues for virtual functions when SR-IOV is enabled.
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

class ModifyNetworkInterfaceAttributeRequestConnectionTrackingConfiguration(DaraModel):
    def __init__(
        self,
        tcp_closed_and_time_wait_timeout: int = None,
        tcp_established_timeout: int = None,
        udp_timeout: int = None,
    ):
        # The timeout period for closed and TIME_WAIT TCP connections. Unit: seconds. Valid values: integers from 3 to 15.
        # 
        # Default value: 3.
        # 
        # > If your ECS instance is used together with an NLB or CLB instance, the default timeout period for connections in the `TIME_WAIT` state is 15 seconds.
        self.tcp_closed_and_time_wait_timeout = tcp_closed_and_time_wait_timeout
        # The timeout period for established TCP connections. Unit: seconds. Valid values: 30, 60, 80, 100, 200, 300, 500, 700, and 910.
        # 
        # Default value: 910.
        self.tcp_established_timeout = tcp_established_timeout
        # The timeout period for UDP flows. Unit: seconds. Valid values: 10, 20, 30, 60, 80, and 100.
        # 
        # Default value: 30.
        # 
        # > If your ECS instance is used together with an NLB or CLB instance, the default value is 100 seconds.
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

