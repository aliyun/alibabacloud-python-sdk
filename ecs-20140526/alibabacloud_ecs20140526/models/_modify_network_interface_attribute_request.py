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
        # The connection tracking configuration.
        # 
        # Before using this parameter, we recommend that you read [Connection timeout management](https://help.aliyun.com/document_detail/2865958.html).
        self.connection_tracking_configuration = connection_tracking_configuration
        # Specifies whether to delete the elastic network interface when its attached instance is released. Valid values:
        # 
        # - `true`: The elastic network interface is deleted.
        # 
        # - `false`: The elastic network interface is retained.
        self.delete_on_release = delete_on_release
        # The description of the elastic network interface. The description must be 2 to 255 characters in length and cannot start with `http://` or `https://`.
        # 
        # Default value: empty.
        self.description = description
        # This parameter is not publicly available.
        self.enhanced_network = enhanced_network
        # The ID of the elastic network interface.
        # 
        # This parameter is required.
        self.network_interface_id = network_interface_id
        # The name of the elastic network interface. The name must be 2 to 128 characters in length, start with a letter or a Chinese character, and not start with `http://` or `https://`. It can contain letters, digits, Chinese characters, colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # Default value: empty.
        self.network_interface_name = network_interface_name
        # The traffic configuration of the elastic network interface.
        self.network_interface_traffic_config = network_interface_traffic_config
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of queues for the elastic network interface. Valid values: 1 to 2048.
        # 
        # - You can change the number of queues for an elastic network interface only when it is in the `Available` state or is attached to an instance in the `Stopped` state.
        # 
        # - The number of queues cannot exceed the maximum supported by the instance type. The total number of queues for all elastic network interfaces attached to the instance cannot exceed the instance\\"s queue quota. You can call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation to query the `MaximumQueueNumberPerEni` and `TotalEniQueueQuantity` values for an instance type.
        self.queue_number = queue_number
        # The ID of the region where the elastic network interface is located. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The queue depth for inbound traffic on the elastic network interface.
        # 
        # > This parameter is available by invitation only. To use this feature, submit a ticket.
        # 
        # Note the following:
        # 
        # - This parameter is available only for instance types of the 7th generation and later.
        # 
        # - This parameter is available only for instances that use Linux images.
        # 
        # - A larger queue depth for inbound traffic increases throughput and reduces the packet loss rate, but consumes more memory.
        self.rx_queue_size = rx_queue_size
        # The IDs of new security groups to associate with the secondary elastic network interface. The interface is then detached from its original security groups.
        # 
        # - The number of security groups that you can specify is limited by the maximum number of security groups to which an elastic network interface can be attached. For more information, see [Usage limits](~~25412#SecurityGroupQuota~~).
        # 
        # - The changes take effect after a short delay.
        self.security_group_id = security_group_id
        # Specifies whether to enable the source/destination check. For enhanced security, we recommend enabling this feature. Valid values:
        # 
        # - `true`: Enabled
        # 
        # - `false`: Disabled
        # 
        # Default value: `false`.
        # 
        # > This feature is available only in specific regions. Before you use this parameter, read [Source/destination check](https://help.aliyun.com/document_detail/2863210.html).
        self.source_dest_check = source_dest_check
        # The queue depth for outbound traffic on the elastic network interface.
        # 
        # > This parameter is available by invitation only. To use this feature, submit a ticket.
        # 
        # Note the following:
        # 
        # - This parameter is available only for instance types of the 7th generation and later.
        # 
        # - This parameter is available only for instances that use Linux images.
        # 
        # - A larger queue depth for outbound traffic increases throughput and reduces the packet loss rate, but consumes more memory.
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
        # The traffic mode of the elastic network interface. Valid values:
        # 
        # - `Standard`: The standard TCP traffic mode.
        # 
        # - `HighPerformance`: The RDMA traffic mode with the Elastic RDMA Interface (ERI) feature enabled.
        # 
        # If the elastic network interface is attached to an instance, note the following:
        # 
        # - The total number of ERI-enabled elastic network interfaces on the instance cannot exceed the quota for the instance type. You can call the [DescribeInstanceTypes operation to query the value of the `EriQuantity` parameter.]()
        # 
        # > This parameter is available by invitation only.
        self.network_interface_traffic_mode = network_interface_traffic_mode
        # The number of queues for the elastic network interface.
        # If the elastic network interface is attached to an instance, note the following:
        # 
        # - The value cannot exceed the maximum number of queues per elastic network interface that is supported by the instance type.
        # 
        # - The total number of queues for all elastic network interfaces on the instance cannot exceed the queue quota for the instance type. You can call the [DescribeInstanceTypes operation to query the `MaximumQueueNumberPerEni` and `TotalEniQueueQuantity` values for an instance type.]()
        # 
        # > This parameter is available by invitation only. To use this feature, submit a ticket.
        self.queue_number = queue_number
        # The number of queue pairs for the ERI.
        # If the elastic network interface is attached to an instance, note the following:
        # 
        # - The value cannot exceed the maximum number of queue pairs per ERI that is supported by the instance type. You can call the [DescribeInstanceTypes operation to query the value of the `QueuePairNumber` parameter for an instance type.]()
        # 
        # > This parameter is available by invitation only. To use this feature, submit a ticket.
        self.queue_pair_number = queue_pair_number
        # The queue depth for inbound traffic on the elastic network interface.
        # 
        # > This parameter is available by invitation only. To use this feature, submit a ticket.
        # 
        # Note the following:
        # 
        # - This parameter is available only for instance types of the 7th generation and later.
        # 
        # - This parameter is available only for instances that use Linux images.
        # 
        # - A larger queue depth for inbound traffic increases throughput and reduces the packet loss rate, but consumes more memory.
        self.rx_queue_size = rx_queue_size
        # The queue depth for outbound traffic on the elastic network interface.
        # 
        # > This parameter is available by invitation only. To use this feature, submit a ticket.
        # 
        # Note the following:
        # 
        # - This parameter is available only for instance types of the 7th generation and later.
        # 
        # - This parameter is available only for instances that use Linux images.
        # 
        # - A larger queue depth for outbound traffic increases throughput and reduces the packet loss rate, but consumes more memory.
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
        enable_rss: bool = None,
        enable_sriov: bool = None,
        virtual_function_quantity: int = None,
        virtual_function_total_queue_number: int = None,
    ):
        # > This parameter is not publicly available.
        self.enable_rss = enable_rss
        # This parameter is not publicly available.
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

class ModifyNetworkInterfaceAttributeRequestConnectionTrackingConfiguration(DaraModel):
    def __init__(
        self,
        tcp_closed_and_time_wait_timeout: int = None,
        tcp_established_timeout: int = None,
        udp_timeout: int = None,
    ):
        # The timeout period, in seconds, for TCP connections in the `TIME_WAIT` or `CLOSE_WAIT` state. The value must be an integer from 3 to 15.
        # 
        # Default value: 3.
        # 
        # > If your ECS instance is used with Network Load Balancer (NLB) or Classic Load Balancer (CLB), the default timeout period for connections in the `TIME_WAIT` state is 15 seconds.
        self.tcp_closed_and_time_wait_timeout = tcp_closed_and_time_wait_timeout
        # The timeout period for TCP connections in the `ESTABLISHED` state, in seconds. Valid values: 30, 60, 80, 100, 200, 300, 500, 700, and 910.
        # 
        # Default value: 910.
        self.tcp_established_timeout = tcp_established_timeout
        # The timeout period for UDP flows, in seconds. Valid values: 10, 20, 30, 60, 80, and 100.
        # 
        # Default value: 30.
        # 
        # > If your ECS instance is used with Network Load Balancer (NLB) or Classic Load Balancer (CLB), the default value is 100 seconds.
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

