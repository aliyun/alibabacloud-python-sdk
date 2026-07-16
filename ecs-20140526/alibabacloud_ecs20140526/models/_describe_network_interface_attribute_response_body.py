# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkInterfaceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        associated_public_ip: main_models.DescribeNetworkInterfaceAttributeResponseBodyAssociatedPublicIp = None,
        attachment: main_models.DescribeNetworkInterfaceAttributeResponseBodyAttachment = None,
        bond_interface_specification: main_models.DescribeNetworkInterfaceAttributeResponseBodyBondInterfaceSpecification = None,
        connection_tracking_configuration: main_models.DescribeNetworkInterfaceAttributeResponseBodyConnectionTrackingConfiguration = None,
        creation_time: str = None,
        delete_on_release: bool = None,
        description: str = None,
        enhanced_network: main_models.DescribeNetworkInterfaceAttributeResponseBodyEnhancedNetwork = None,
        instance_id: str = None,
        ipv_4prefix_sets: main_models.DescribeNetworkInterfaceAttributeResponseBodyIpv4PrefixSets = None,
        ipv_6prefix_sets: main_models.DescribeNetworkInterfaceAttributeResponseBodyIpv6PrefixSets = None,
        ipv_6sets: main_models.DescribeNetworkInterfaceAttributeResponseBodyIpv6Sets = None,
        mac_address: str = None,
        network_interface_id: str = None,
        network_interface_name: str = None,
        network_interface_traffic_config: main_models.DescribeNetworkInterfaceAttributeResponseBodyNetworkInterfaceTrafficConfig = None,
        network_interface_traffic_mode: str = None,
        owner_id: str = None,
        private_ip_address: str = None,
        private_ip_sets: main_models.DescribeNetworkInterfaceAttributeResponseBodyPrivateIpSets = None,
        qo_sconfig: main_models.DescribeNetworkInterfaceAttributeResponseBodyQoSConfig = None,
        queue_number: int = None,
        queue_pair_number: int = None,
        request_id: str = None,
        resource_group_id: str = None,
        security_group_ids: main_models.DescribeNetworkInterfaceAttributeResponseBodySecurityGroupIds = None,
        service_id: int = None,
        service_managed: bool = None,
        slave_interface_specification: main_models.DescribeNetworkInterfaceAttributeResponseBodySlaveInterfaceSpecification = None,
        source_dest_check: bool = None,
        status: str = None,
        tags: main_models.DescribeNetworkInterfaceAttributeResponseBodyTags = None,
        tcp_option_address_enabled: str = None,
        type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The elastic IP address that is associated with the primary private IP address of the elastic network interface.
        self.associated_public_ip = associated_public_ip
        # > This parameter is in invitational preview and is not publicly available.
        self.attachment = attachment
        # > This parameter is in invitational preview and is not publicly available.
        self.bond_interface_specification = bond_interface_specification
        # The connection tracking configuration.
        # 
        # For more information, see [Connection timeout management](https://help.aliyun.com/document_detail/2865958.html).
        # 
        # > This parameter is returned only if the `Attribute` parameter is set to `connectionTrackingConfiguration` in the request.
        self.connection_tracking_configuration = connection_tracking_configuration
        # The time when the elastic network interface was created.
        self.creation_time = creation_time
        # Indicates whether to release the elastic network interface when the associated instance is released.
        # 
        # - `true`: The interface is released.
        # 
        # - `false`: The interface is retained.
        self.delete_on_release = delete_on_release
        # The description of the elastic network interface.
        self.description = description
        # This parameter is not publicly available.
        self.enhanced_network = enhanced_network
        # The ID of the instance to which the elastic network interface is attached.
        # 
        # > This parameter is not returned if the elastic network interface is managed by another Alibaba Cloud service.
        self.instance_id = instance_id
        self.ipv_4prefix_sets = ipv_4prefix_sets
        self.ipv_6prefix_sets = ipv_6prefix_sets
        self.ipv_6sets = ipv_6sets
        # The MAC address of the elastic network interface.
        self.mac_address = mac_address
        # The ID of the elastic network interface.
        self.network_interface_id = network_interface_id
        # The name of the elastic network interface.
        self.network_interface_name = network_interface_name
        # The communication parameters of the elastic network interface.
        self.network_interface_traffic_config = network_interface_traffic_config
        # The communication mode of the elastic network interface. Valid values:
        # 
        # - `Standard`: Uses TCP communication.
        # 
        # - `HighPerformance`: Uses the Elastic RDMA Interface (ERI) for RDMA communication.
        # 
        # > The `HighPerformance` value is supported only by RDMA-enhanced instances, such as the c7re family.
        self.network_interface_traffic_mode = network_interface_traffic_mode
        # The ID of the account to which the elastic network interface belongs.
        self.owner_id = owner_id
        # The primary private IP address of the elastic network interface.
        self.private_ip_address = private_ip_address
        self.private_ip_sets = private_ip_sets
        # The QoS settings.
        self.qo_sconfig = qo_sconfig
        # The number of queues supported by the elastic network interface.
        # 
        # - For a primary network interface, this parameter returns the default number of queues for the instance type.
        # 
        # - For a secondary network interface:
        # 
        #   - If the interface is in the `InUse` state:
        # 
        #     - If the queue number was not modified, the default value for the instance type is returned.
        # 
        #     - If the queue number was modified, the new value is returned.
        # 
        #   - If the secondary network interface is in the `Available` state:
        # 
        #     - If the queue number was not modified, this parameter is not returned.
        # 
        #     - If the queue number was modified, the new value is returned.
        self.queue_number = queue_number
        # > This parameter is in invitational preview and is not publicly available.
        self.queue_pair_number = queue_pair_number
        # The request ID.
        self.request_id = request_id
        # The ID of the enterprise resource group to which the elastic network interface belongs. If you use this parameter to filter resources, the number of resources cannot exceed 1,000.
        # 
        # > Resources in the default resource group cannot be filtered.
        self.resource_group_id = resource_group_id
        self.security_group_ids = security_group_ids
        # The ID of the virtual service provider (VSP) for the elastic network interface.
        self.service_id = service_id
        # Indicates whether the elastic network interface is managed by an Alibaba Cloud service or a VSP.
        self.service_managed = service_managed
        # > This parameter is in invitational preview and is not publicly available.
        self.slave_interface_specification = slave_interface_specification
        # This parameter is not publicly available.
        self.source_dest_check = source_dest_check
        # The status of the elastic network interface. Valid values:
        # 
        # - `Available`: The elastic network interface is available.
        # 
        # - `Attaching`: The elastic network interface is being attached.
        # 
        # - `InUse`: The elastic network interface is attached.
        # 
        # - `Detaching`: The elastic network interface is being detached.
        # 
        # - `Deleting`: The elastic network interface is being deleted.
        self.status = status
        self.tags = tags
        # > This parameter is in invitational preview and is not publicly available.
        self.tcp_option_address_enabled = tcp_option_address_enabled
        # The type of the elastic network interface. Valid values:
        # 
        # - `Primary`: The primary network interface.
        # 
        # - `Secondary`: The secondary network interface.
        self.type = type
        # The ID of the vSwitch to which the elastic network interface is connected.
        self.v_switch_id = v_switch_id
        # The ID of the VPC to which the elastic network interface belongs.
        self.vpc_id = vpc_id
        # The ID of the zone.
        self.zone_id = zone_id

    def validate(self):
        if self.associated_public_ip:
            self.associated_public_ip.validate()
        if self.attachment:
            self.attachment.validate()
        if self.bond_interface_specification:
            self.bond_interface_specification.validate()
        if self.connection_tracking_configuration:
            self.connection_tracking_configuration.validate()
        if self.enhanced_network:
            self.enhanced_network.validate()
        if self.ipv_4prefix_sets:
            self.ipv_4prefix_sets.validate()
        if self.ipv_6prefix_sets:
            self.ipv_6prefix_sets.validate()
        if self.ipv_6sets:
            self.ipv_6sets.validate()
        if self.network_interface_traffic_config:
            self.network_interface_traffic_config.validate()
        if self.private_ip_sets:
            self.private_ip_sets.validate()
        if self.qo_sconfig:
            self.qo_sconfig.validate()
        if self.security_group_ids:
            self.security_group_ids.validate()
        if self.slave_interface_specification:
            self.slave_interface_specification.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_public_ip is not None:
            result['AssociatedPublicIp'] = self.associated_public_ip.to_map()

        if self.attachment is not None:
            result['Attachment'] = self.attachment.to_map()

        if self.bond_interface_specification is not None:
            result['BondInterfaceSpecification'] = self.bond_interface_specification.to_map()

        if self.connection_tracking_configuration is not None:
            result['ConnectionTrackingConfiguration'] = self.connection_tracking_configuration.to_map()

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.delete_on_release is not None:
            result['DeleteOnRelease'] = self.delete_on_release

        if self.description is not None:
            result['Description'] = self.description

        if self.enhanced_network is not None:
            result['EnhancedNetwork'] = self.enhanced_network.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ipv_4prefix_sets is not None:
            result['Ipv4PrefixSets'] = self.ipv_4prefix_sets.to_map()

        if self.ipv_6prefix_sets is not None:
            result['Ipv6PrefixSets'] = self.ipv_6prefix_sets.to_map()

        if self.ipv_6sets is not None:
            result['Ipv6Sets'] = self.ipv_6sets.to_map()

        if self.mac_address is not None:
            result['MacAddress'] = self.mac_address

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.network_interface_name is not None:
            result['NetworkInterfaceName'] = self.network_interface_name

        if self.network_interface_traffic_config is not None:
            result['NetworkInterfaceTrafficConfig'] = self.network_interface_traffic_config.to_map()

        if self.network_interface_traffic_mode is not None:
            result['NetworkInterfaceTrafficMode'] = self.network_interface_traffic_mode

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.private_ip_sets is not None:
            result['PrivateIpSets'] = self.private_ip_sets.to_map()

        if self.qo_sconfig is not None:
            result['QoSConfig'] = self.qo_sconfig.to_map()

        if self.queue_number is not None:
            result['QueueNumber'] = self.queue_number

        if self.queue_pair_number is not None:
            result['QueuePairNumber'] = self.queue_pair_number

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids.to_map()

        if self.service_id is not None:
            result['ServiceID'] = self.service_id

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        if self.slave_interface_specification is not None:
            result['SlaveInterfaceSpecification'] = self.slave_interface_specification.to_map()

        if self.source_dest_check is not None:
            result['SourceDestCheck'] = self.source_dest_check

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.tcp_option_address_enabled is not None:
            result['TcpOptionAddressEnabled'] = self.tcp_option_address_enabled

        if self.type is not None:
            result['Type'] = self.type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedPublicIp') is not None:
            temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyAssociatedPublicIp()
            self.associated_public_ip = temp_model.from_map(m.get('AssociatedPublicIp'))

        if m.get('Attachment') is not None:
            temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyAttachment()
            self.attachment = temp_model.from_map(m.get('Attachment'))

        if m.get('BondInterfaceSpecification') is not None:
            temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyBondInterfaceSpecification()
            self.bond_interface_specification = temp_model.from_map(m.get('BondInterfaceSpecification'))

        if m.get('ConnectionTrackingConfiguration') is not None:
            temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyConnectionTrackingConfiguration()
            self.connection_tracking_configuration = temp_model.from_map(m.get('ConnectionTrackingConfiguration'))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DeleteOnRelease') is not None:
            self.delete_on_release = m.get('DeleteOnRelease')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnhancedNetwork') is not None:
            temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyEnhancedNetwork()
            self.enhanced_network = temp_model.from_map(m.get('EnhancedNetwork'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ipv4PrefixSets') is not None:
            temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyIpv4PrefixSets()
            self.ipv_4prefix_sets = temp_model.from_map(m.get('Ipv4PrefixSets'))

        if m.get('Ipv6PrefixSets') is not None:
            temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyIpv6PrefixSets()
            self.ipv_6prefix_sets = temp_model.from_map(m.get('Ipv6PrefixSets'))

        if m.get('Ipv6Sets') is not None:
            temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyIpv6Sets()
            self.ipv_6sets = temp_model.from_map(m.get('Ipv6Sets'))

        if m.get('MacAddress') is not None:
            self.mac_address = m.get('MacAddress')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('NetworkInterfaceName') is not None:
            self.network_interface_name = m.get('NetworkInterfaceName')

        if m.get('NetworkInterfaceTrafficConfig') is not None:
            temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyNetworkInterfaceTrafficConfig()
            self.network_interface_traffic_config = temp_model.from_map(m.get('NetworkInterfaceTrafficConfig'))

        if m.get('NetworkInterfaceTrafficMode') is not None:
            self.network_interface_traffic_mode = m.get('NetworkInterfaceTrafficMode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('PrivateIpSets') is not None:
            temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyPrivateIpSets()
            self.private_ip_sets = temp_model.from_map(m.get('PrivateIpSets'))

        if m.get('QoSConfig') is not None:
            temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyQoSConfig()
            self.qo_sconfig = temp_model.from_map(m.get('QoSConfig'))

        if m.get('QueueNumber') is not None:
            self.queue_number = m.get('QueueNumber')

        if m.get('QueuePairNumber') is not None:
            self.queue_pair_number = m.get('QueuePairNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupIds') is not None:
            temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodySecurityGroupIds()
            self.security_group_ids = temp_model.from_map(m.get('SecurityGroupIds'))

        if m.get('ServiceID') is not None:
            self.service_id = m.get('ServiceID')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        if m.get('SlaveInterfaceSpecification') is not None:
            temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodySlaveInterfaceSpecification()
            self.slave_interface_specification = temp_model.from_map(m.get('SlaveInterfaceSpecification'))

        if m.get('SourceDestCheck') is not None:
            self.source_dest_check = m.get('SourceDestCheck')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TcpOptionAddressEnabled') is not None:
            self.tcp_option_address_enabled = m.get('TcpOptionAddressEnabled')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeNetworkInterfaceAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeNetworkInterfaceAttributeResponseBodyTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeNetworkInterfaceAttributeResponseBodyTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeNetworkInterfaceAttributeResponseBodySlaveInterfaceSpecification(DaraModel):
    def __init__(
        self,
        bond_network_interface_id: str = None,
        slave_network_interface_id: str = None,
        work_state: str = None,
    ):
        # > This parameter is in invitational preview and is not publicly available.
        self.bond_network_interface_id = bond_network_interface_id
        # > This parameter is in invitational preview and is not publicly available.
        self.slave_network_interface_id = slave_network_interface_id
        # > This parameter is in invitational preview and is not publicly available.
        self.work_state = work_state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bond_network_interface_id is not None:
            result['BondNetworkInterfaceId'] = self.bond_network_interface_id

        if self.slave_network_interface_id is not None:
            result['SlaveNetworkInterfaceId'] = self.slave_network_interface_id

        if self.work_state is not None:
            result['WorkState'] = self.work_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BondNetworkInterfaceId') is not None:
            self.bond_network_interface_id = m.get('BondNetworkInterfaceId')

        if m.get('SlaveNetworkInterfaceId') is not None:
            self.slave_network_interface_id = m.get('SlaveNetworkInterfaceId')

        if m.get('WorkState') is not None:
            self.work_state = m.get('WorkState')

        return self

class DescribeNetworkInterfaceAttributeResponseBodySecurityGroupIds(DaraModel):
    def __init__(
        self,
        security_group_id: List[str] = None,
    ):
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        return self

class DescribeNetworkInterfaceAttributeResponseBodyQoSConfig(DaraModel):
    def __init__(
        self,
        enable_qo_s: bool = None,
        qo_s: main_models.DescribeNetworkInterfaceAttributeResponseBodyQoSConfigQoS = None,
    ):
        # Indicates whether QoS is enabled.
        self.enable_qo_s = enable_qo_s
        # The QoS settings.
        self.qo_s = qo_s

    def validate(self):
        if self.qo_s:
            self.qo_s.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_qo_s is not None:
            result['EnableQoS'] = self.enable_qo_s

        if self.qo_s is not None:
            result['QoS'] = self.qo_s.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableQoS') is not None:
            self.enable_qo_s = m.get('EnableQoS')

        if m.get('QoS') is not None:
            temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyQoSConfigQoS()
            self.qo_s = temp_model.from_map(m.get('QoS'))

        return self

class DescribeNetworkInterfaceAttributeResponseBodyQoSConfigQoS(DaraModel):
    def __init__(
        self,
        bandwidth_rx: int = None,
        bandwidth_tx: int = None,
        concurrent_connections: int = None,
        pps_rx: int = None,
        pps_tx: int = None,
    ):
        # The maximum inbound bandwidth on the internal network.
        self.bandwidth_rx = bandwidth_rx
        # The maximum outbound bandwidth on the internal network.
        self.bandwidth_tx = bandwidth_tx
        # The maximum number of connections.
        self.concurrent_connections = concurrent_connections
        # The inbound packet transmission rate on the internal network. Unit: packets per second (pps).
        self.pps_rx = pps_rx
        # The outbound packet transmission rate on the internal network. Unit: packets per second (pps).
        self.pps_tx = pps_tx

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_rx is not None:
            result['BandwidthRx'] = self.bandwidth_rx

        if self.bandwidth_tx is not None:
            result['BandwidthTx'] = self.bandwidth_tx

        if self.concurrent_connections is not None:
            result['ConcurrentConnections'] = self.concurrent_connections

        if self.pps_rx is not None:
            result['PpsRx'] = self.pps_rx

        if self.pps_tx is not None:
            result['PpsTx'] = self.pps_tx

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthRx') is not None:
            self.bandwidth_rx = m.get('BandwidthRx')

        if m.get('BandwidthTx') is not None:
            self.bandwidth_tx = m.get('BandwidthTx')

        if m.get('ConcurrentConnections') is not None:
            self.concurrent_connections = m.get('ConcurrentConnections')

        if m.get('PpsRx') is not None:
            self.pps_rx = m.get('PpsRx')

        if m.get('PpsTx') is not None:
            self.pps_tx = m.get('PpsTx')

        return self

class DescribeNetworkInterfaceAttributeResponseBodyPrivateIpSets(DaraModel):
    def __init__(
        self,
        private_ip_set: List[main_models.DescribeNetworkInterfaceAttributeResponseBodyPrivateIpSetsPrivateIpSet] = None,
    ):
        self.private_ip_set = private_ip_set

    def validate(self):
        if self.private_ip_set:
            for v1 in self.private_ip_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PrivateIpSet'] = []
        if self.private_ip_set is not None:
            for k1 in self.private_ip_set:
                result['PrivateIpSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.private_ip_set = []
        if m.get('PrivateIpSet') is not None:
            for k1 in m.get('PrivateIpSet'):
                temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyPrivateIpSetsPrivateIpSet()
                self.private_ip_set.append(temp_model.from_map(k1))

        return self

class DescribeNetworkInterfaceAttributeResponseBodyPrivateIpSetsPrivateIpSet(DaraModel):
    def __init__(
        self,
        associated_public_ip: main_models.DescribeNetworkInterfaceAttributeResponseBodyPrivateIpSetsPrivateIpSetAssociatedPublicIp = None,
        primary: bool = None,
        private_ip_address: str = None,
    ):
        self.associated_public_ip = associated_public_ip
        self.primary = primary
        self.private_ip_address = private_ip_address

    def validate(self):
        if self.associated_public_ip:
            self.associated_public_ip.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_public_ip is not None:
            result['AssociatedPublicIp'] = self.associated_public_ip.to_map()

        if self.primary is not None:
            result['Primary'] = self.primary

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedPublicIp') is not None:
            temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyPrivateIpSetsPrivateIpSetAssociatedPublicIp()
            self.associated_public_ip = temp_model.from_map(m.get('AssociatedPublicIp'))

        if m.get('Primary') is not None:
            self.primary = m.get('Primary')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        return self

class DescribeNetworkInterfaceAttributeResponseBodyPrivateIpSetsPrivateIpSetAssociatedPublicIp(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        public_ip_address: str = None,
    ):
        self.allocation_id = allocation_id
        self.public_ip_address = public_ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')

        return self

class DescribeNetworkInterfaceAttributeResponseBodyNetworkInterfaceTrafficConfig(DaraModel):
    def __init__(
        self,
        network_interface_traffic_mode: str = None,
        queue_number: int = None,
        queue_pair_number: int = None,
    ):
        # The communication mode of the elastic network interface.
        self.network_interface_traffic_mode = network_interface_traffic_mode
        # The number of queues for the elastic network interface.
        self.queue_number = queue_number
        # The number of queue pairs for the RDMA-enabled elastic network interface.
        self.queue_pair_number = queue_pair_number

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkInterfaceTrafficMode') is not None:
            self.network_interface_traffic_mode = m.get('NetworkInterfaceTrafficMode')

        if m.get('QueueNumber') is not None:
            self.queue_number = m.get('QueueNumber')

        if m.get('QueuePairNumber') is not None:
            self.queue_pair_number = m.get('QueuePairNumber')

        return self

class DescribeNetworkInterfaceAttributeResponseBodyIpv6Sets(DaraModel):
    def __init__(
        self,
        ipv_6set: List[main_models.DescribeNetworkInterfaceAttributeResponseBodyIpv6SetsIpv6Set] = None,
    ):
        self.ipv_6set = ipv_6set

    def validate(self):
        if self.ipv_6set:
            for v1 in self.ipv_6set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv6Set'] = []
        if self.ipv_6set is not None:
            for k1 in self.ipv_6set:
                result['Ipv6Set'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6set = []
        if m.get('Ipv6Set') is not None:
            for k1 in m.get('Ipv6Set'):
                temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyIpv6SetsIpv6Set()
                self.ipv_6set.append(temp_model.from_map(k1))

        return self

class DescribeNetworkInterfaceAttributeResponseBodyIpv6SetsIpv6Set(DaraModel):
    def __init__(
        self,
        ipv_6address: str = None,
    ):
        self.ipv_6address = ipv_6address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        return self

class DescribeNetworkInterfaceAttributeResponseBodyIpv6PrefixSets(DaraModel):
    def __init__(
        self,
        ipv_6prefix_set: List[main_models.DescribeNetworkInterfaceAttributeResponseBodyIpv6PrefixSetsIpv6PrefixSet] = None,
    ):
        self.ipv_6prefix_set = ipv_6prefix_set

    def validate(self):
        if self.ipv_6prefix_set:
            for v1 in self.ipv_6prefix_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv6PrefixSet'] = []
        if self.ipv_6prefix_set is not None:
            for k1 in self.ipv_6prefix_set:
                result['Ipv6PrefixSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6prefix_set = []
        if m.get('Ipv6PrefixSet') is not None:
            for k1 in m.get('Ipv6PrefixSet'):
                temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyIpv6PrefixSetsIpv6PrefixSet()
                self.ipv_6prefix_set.append(temp_model.from_map(k1))

        return self

class DescribeNetworkInterfaceAttributeResponseBodyIpv6PrefixSetsIpv6PrefixSet(DaraModel):
    def __init__(
        self,
        ipv_6prefix: str = None,
    ):
        self.ipv_6prefix = ipv_6prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6prefix is not None:
            result['Ipv6Prefix'] = self.ipv_6prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6Prefix') is not None:
            self.ipv_6prefix = m.get('Ipv6Prefix')

        return self

class DescribeNetworkInterfaceAttributeResponseBodyIpv4PrefixSets(DaraModel):
    def __init__(
        self,
        ipv_4prefix_set: List[main_models.DescribeNetworkInterfaceAttributeResponseBodyIpv4PrefixSetsIpv4PrefixSet] = None,
    ):
        self.ipv_4prefix_set = ipv_4prefix_set

    def validate(self):
        if self.ipv_4prefix_set:
            for v1 in self.ipv_4prefix_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv4PrefixSet'] = []
        if self.ipv_4prefix_set is not None:
            for k1 in self.ipv_4prefix_set:
                result['Ipv4PrefixSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_4prefix_set = []
        if m.get('Ipv4PrefixSet') is not None:
            for k1 in m.get('Ipv4PrefixSet'):
                temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyIpv4PrefixSetsIpv4PrefixSet()
                self.ipv_4prefix_set.append(temp_model.from_map(k1))

        return self

class DescribeNetworkInterfaceAttributeResponseBodyIpv4PrefixSetsIpv4PrefixSet(DaraModel):
    def __init__(
        self,
        ipv_4prefix: str = None,
    ):
        self.ipv_4prefix = ipv_4prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4prefix is not None:
            result['Ipv4Prefix'] = self.ipv_4prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv4Prefix') is not None:
            self.ipv_4prefix = m.get('Ipv4Prefix')

        return self

class DescribeNetworkInterfaceAttributeResponseBodyEnhancedNetwork(DaraModel):
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

class DescribeNetworkInterfaceAttributeResponseBodyConnectionTrackingConfiguration(DaraModel):
    def __init__(
        self,
        tcp_closed_and_time_wait_timeout: int = None,
        tcp_established_timeout: int = None,
        udp_timeout: int = None,
    ):
        # The timeout period for TCP connections in the `TIME_WAIT` and `FIN-WAIT-2` states. Unit: seconds. Valid values: an integer from 3 to 15.
        # 
        # > For ECS instances used with a Network Load Balancer (NLB) or Classic Load Balancer (CLB), the default timeout for connections in the `TIME_WAIT` state is 15 seconds.
        self.tcp_closed_and_time_wait_timeout = tcp_closed_and_time_wait_timeout
        # The timeout period for established TCP connections. Unit: seconds. Valid values: 30, 60, 80, 100, 200, 300, 500, 700, and 910.
        self.tcp_established_timeout = tcp_established_timeout
        # The timeout period for UDP streams. Unit: seconds. Valid values: 10, 20, 30, 60, 80, and 100.
        # 
        # > For ECS instances used with a Network Load Balancer (NLB) or Classic Load Balancer (CLB), the default UDP timeout is 100 seconds.
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

class DescribeNetworkInterfaceAttributeResponseBodyBondInterfaceSpecification(DaraModel):
    def __init__(
        self,
        bond_mode: str = None,
        slave_interface_specification: main_models.DescribeNetworkInterfaceAttributeResponseBodyBondInterfaceSpecificationSlaveInterfaceSpecification = None,
    ):
        # > This parameter is in invitational preview and is not publicly available.
        self.bond_mode = bond_mode
        self.slave_interface_specification = slave_interface_specification

    def validate(self):
        if self.slave_interface_specification:
            self.slave_interface_specification.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bond_mode is not None:
            result['BondMode'] = self.bond_mode

        if self.slave_interface_specification is not None:
            result['SlaveInterfaceSpecification'] = self.slave_interface_specification.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BondMode') is not None:
            self.bond_mode = m.get('BondMode')

        if m.get('SlaveInterfaceSpecification') is not None:
            temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyBondInterfaceSpecificationSlaveInterfaceSpecification()
            self.slave_interface_specification = temp_model.from_map(m.get('SlaveInterfaceSpecification'))

        return self

class DescribeNetworkInterfaceAttributeResponseBodyBondInterfaceSpecificationSlaveInterfaceSpecification(DaraModel):
    def __init__(
        self,
        slave_interface_specification_set: List[main_models.DescribeNetworkInterfaceAttributeResponseBodyBondInterfaceSpecificationSlaveInterfaceSpecificationSlaveInterfaceSpecificationSet] = None,
    ):
        self.slave_interface_specification_set = slave_interface_specification_set

    def validate(self):
        if self.slave_interface_specification_set:
            for v1 in self.slave_interface_specification_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SlaveInterfaceSpecificationSet'] = []
        if self.slave_interface_specification_set is not None:
            for k1 in self.slave_interface_specification_set:
                result['SlaveInterfaceSpecificationSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.slave_interface_specification_set = []
        if m.get('SlaveInterfaceSpecificationSet') is not None:
            for k1 in m.get('SlaveInterfaceSpecificationSet'):
                temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyBondInterfaceSpecificationSlaveInterfaceSpecificationSlaveInterfaceSpecificationSet()
                self.slave_interface_specification_set.append(temp_model.from_map(k1))

        return self

class DescribeNetworkInterfaceAttributeResponseBodyBondInterfaceSpecificationSlaveInterfaceSpecificationSlaveInterfaceSpecificationSet(DaraModel):
    def __init__(
        self,
        bond_network_interface_id: str = None,
        slave_network_interface_id: str = None,
        work_state: str = None,
    ):
        self.bond_network_interface_id = bond_network_interface_id
        self.slave_network_interface_id = slave_network_interface_id
        self.work_state = work_state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bond_network_interface_id is not None:
            result['BondNetworkInterfaceId'] = self.bond_network_interface_id

        if self.slave_network_interface_id is not None:
            result['SlaveNetworkInterfaceId'] = self.slave_network_interface_id

        if self.work_state is not None:
            result['WorkState'] = self.work_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BondNetworkInterfaceId') is not None:
            self.bond_network_interface_id = m.get('BondNetworkInterfaceId')

        if m.get('SlaveNetworkInterfaceId') is not None:
            self.slave_network_interface_id = m.get('SlaveNetworkInterfaceId')

        if m.get('WorkState') is not None:
            self.work_state = m.get('WorkState')

        return self

class DescribeNetworkInterfaceAttributeResponseBodyAttachment(DaraModel):
    def __init__(
        self,
        device_index: int = None,
        instance_id: str = None,
        member_network_interface_ids: main_models.DescribeNetworkInterfaceAttributeResponseBodyAttachmentMemberNetworkInterfaceIds = None,
        network_card_index: int = None,
        trunk_network_interface_id: str = None,
    ):
        # > This parameter is in invitational preview and is not publicly available.
        self.device_index = device_index
        # > This parameter is in invitational preview and is not publicly available.
        self.instance_id = instance_id
        self.member_network_interface_ids = member_network_interface_ids
        # The index of the physical network card to which the elastic network interface is attached.
        # 
        # - This parameter is not returned if the elastic network interface is `Available`, or if no index was specified during attachment.
        # 
        # - If the elastic network interface is `InUse` and an index was specified during attachment, this parameter returns the index of the physical network card.
        self.network_card_index = network_card_index
        # > This parameter is in invitational preview and is not publicly available.
        self.trunk_network_interface_id = trunk_network_interface_id

    def validate(self):
        if self.member_network_interface_ids:
            self.member_network_interface_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_index is not None:
            result['DeviceIndex'] = self.device_index

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.member_network_interface_ids is not None:
            result['MemberNetworkInterfaceIds'] = self.member_network_interface_ids.to_map()

        if self.network_card_index is not None:
            result['NetworkCardIndex'] = self.network_card_index

        if self.trunk_network_interface_id is not None:
            result['TrunkNetworkInterfaceId'] = self.trunk_network_interface_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceIndex') is not None:
            self.device_index = m.get('DeviceIndex')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MemberNetworkInterfaceIds') is not None:
            temp_model = main_models.DescribeNetworkInterfaceAttributeResponseBodyAttachmentMemberNetworkInterfaceIds()
            self.member_network_interface_ids = temp_model.from_map(m.get('MemberNetworkInterfaceIds'))

        if m.get('NetworkCardIndex') is not None:
            self.network_card_index = m.get('NetworkCardIndex')

        if m.get('TrunkNetworkInterfaceId') is not None:
            self.trunk_network_interface_id = m.get('TrunkNetworkInterfaceId')

        return self

class DescribeNetworkInterfaceAttributeResponseBodyAttachmentMemberNetworkInterfaceIds(DaraModel):
    def __init__(
        self,
        member_network_interface_id: List[str] = None,
    ):
        self.member_network_interface_id = member_network_interface_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_network_interface_id is not None:
            result['MemberNetworkInterfaceId'] = self.member_network_interface_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberNetworkInterfaceId') is not None:
            self.member_network_interface_id = m.get('MemberNetworkInterfaceId')

        return self

class DescribeNetworkInterfaceAttributeResponseBodyAssociatedPublicIp(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        public_ip_address: str = None,
    ):
        # The ID of the elastic IP address.
        self.allocation_id = allocation_id
        # The public IP address.
        self.public_ip_address = public_ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')

        return self

