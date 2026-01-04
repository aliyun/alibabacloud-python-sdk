# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListVirtualPhysicalConnectionsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        virtual_physical_connections: List[main_models.ListVirtualPhysicalConnectionsResponseBodyVirtualPhysicalConnections] = None,
    ):
        # The number of entries returned in this query.
        self.count = count
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If the value of **NextToken** is not returned, it indicates that no next query is to be sent.
        # *   If **NextToken** was returned in the previous query, specify the value to obtain the next set of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The list of hosted connections returned.
        self.virtual_physical_connections = virtual_physical_connections

    def validate(self):
        if self.virtual_physical_connections:
            for v1 in self.virtual_physical_connections:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VirtualPhysicalConnections'] = []
        if self.virtual_physical_connections is not None:
            for k1 in self.virtual_physical_connections:
                result['VirtualPhysicalConnections'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.virtual_physical_connections = []
        if m.get('VirtualPhysicalConnections') is not None:
            for k1 in m.get('VirtualPhysicalConnections'):
                temp_model = main_models.ListVirtualPhysicalConnectionsResponseBodyVirtualPhysicalConnections()
                self.virtual_physical_connections.append(temp_model.from_map(k1))

        return self

class ListVirtualPhysicalConnectionsResponseBodyVirtualPhysicalConnections(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        ad_location: str = None,
        ali_uid: str = None,
        bandwidth: int = None,
        business_status: str = None,
        charge_type: str = None,
        circuit_code: str = None,
        creation_time: str = None,
        description: str = None,
        enabled_time: str = None,
        end_time: str = None,
        expect_spec: str = None,
        line_operator: str = None,
        loa_status: str = None,
        name: str = None,
        order_mode: str = None,
        parent_physical_connection_ali_uid: str = None,
        parent_physical_connection_id: str = None,
        peer_location: str = None,
        physical_connection_id: str = None,
        port_number: str = None,
        port_type: str = None,
        product_type: str = None,
        redundant_physical_connection_id: str = None,
        resource_group_id: str = None,
        spec: str = None,
        status: str = None,
        tags: List[main_models.ListVirtualPhysicalConnectionsResponseBodyVirtualPhysicalConnectionsTags] = None,
        type: str = None,
        virtual_physical_connection_status: str = None,
        vlan_id: str = None,
    ):
        # The ID of the access point that is associated with the Express Connect circuit.
        self.access_point_id = access_point_id
        # The geographical location of the access device.
        self.ad_location = ad_location
        # The Alibaba Cloud account ID of the hosted connection owner.
        self.ali_uid = ali_uid
        # The bandwidth of the Express Connect circuit. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The status of the Express Connect circuit. Valid values:
        # 
        # *   **Normal**
        # *   **FinancialLocked**
        # *   **SecurityLocked**
        self.business_status = business_status
        # The billing method of the Express Connect circuit.
        # 
        # If **Prepaid** is returned, it indicates that the Express Connect circuit is billed on a subscription basis.
        self.charge_type = charge_type
        # The circuit code of the Express Connect circuit. The circuit code is provided by the connectivity provider.
        self.circuit_code = circuit_code
        # The time when the Express Connect circuit was created.
        self.creation_time = creation_time
        # The description of the Express Connect circuit.
        self.description = description
        # The time when the Express Connect circuit is enabled.
        self.enabled_time = enabled_time
        # The expiration date of the hosted connection.
        # 
        # The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.end_time = end_time
        # The estimated maximum bandwidth of the shared Express Connect circuit. The estimated bandwidth takes effect after you complete the payment.
        # 
        # **M** indicates Mbit/s and **G** indicates Gbit/s.
        self.expect_spec = expect_spec
        # The connectivity provider of the Express Connect circuit. Valid values:
        # 
        # *   **CT**: China Telecom.
        # *   **CU**: China Unicom.
        # *   **CM**: China Mobile.
        # *   **CO**: other connectivity providers in the Chinese mainland.
        # *   **Equinix**: Equinix.
        # *   **Other**: other connectivity providers outside the Chinese mainland.
        self.line_operator = line_operator
        # The status of the letter of authorization (LOA). Valid values:
        # 
        # *   **Applying**
        # *   **Accept**
        # *   **Available**
        # *   **Rejected**
        # *   **Completing**
        # *   **Complete**
        # *   **Deleted**
        self.loa_status = loa_status
        # The name of the Express Connect circuit.
        self.name = name
        # The payer for the shared Express Connect circuit. Valid values:
        # 
        # *   **PayByPhysicalConnectionOwner**: the owner of the shared Express Connect circuit
        # *   **PayByVirtualPhysicalConnectionOwner**: the owner of the hosted connection
        self.order_mode = order_mode
        # The ID of the Alibaba Cloud account to which the Express Connect circuit belongs.
        self.parent_physical_connection_ali_uid = parent_physical_connection_ali_uid
        # The ID of the Express Connect circuit.
        self.parent_physical_connection_id = parent_physical_connection_id
        # The geographical location of the data center.
        self.peer_location = peer_location
        # The ID of the hosted connection.
        self.physical_connection_id = physical_connection_id
        # The ID of the port on the access device.
        self.port_number = port_number
        # The port type. Valid values:
        # 
        # *   **100Base-T**: 100 Mbit/s copper Ethernet port
        # *   **1000Base-T**: 1,000 Mbit/s copper Ethernet port
        # *   **1000Base-LX**: 1,000 Mbit/s single-mode optical port (10 km)
        # *   **10GBase-T**: 10,000 Mbit/s copper Ethernet port
        # *   **10GBase-LR**: 10,000 Mbit/s single-mode optical port (10 km)
        # *   **40GBase-LR**: 40,000 Mbit/s single-mode optical port
        # *   **100GBase-LR**: 100,000 Mbit/s single-mode optical port
        self.port_type = port_type
        # The type of the Express Connect circuit. Valid values:
        # 
        # *   **VirtualPhysicalConnection**: shared Express Connect circuit
        # *   **PhysicalConnection**: dedicated Express Connect circuit
        self.product_type = product_type
        # The ID of the redundant Express Connect circuit.
        self.redundant_physical_connection_id = redundant_physical_connection_id
        # The ID of the resource group to which the hosted connection belongs.
        self.resource_group_id = resource_group_id
        # The bandwidth value of the hosted connection.
        # 
        # **M** indicates Mbit/s and **G** indicates Gbit/s.
        self.spec = spec
        # The status of the Express Connect circuit. Valid values:
        # 
        # *   **Initial**: The application is under review.
        # *   **Approved**: The application is approved.
        # *   **Allocating**: The system is allocating resources.
        # *   **Allocated**: The Express Connect circuit is under construction.
        # *   **Confirmed**: The Express Connect circuit is pending for user confirmation.
        # *   **Enabled**: The Express Connect circuit is enabled.
        # *   **Rejected**: The application is rejected.
        # *   **Canceled**: The application is canceled.
        # *   **Allocation Failed**: The system failed to allocate resources.
        # *   **Terminated**: The Express Connect circuit is disabled.
        self.status = status
        # The tag list.
        self.tags = tags
        # The type of Express Connect circuit. Default value: **VPC**.
        self.type = type
        # The status of the hosted connection. Valid values:
        # 
        # *   **Confirmed**
        # *   **UnConfirmed**
        # *   **Deleted**
        self.virtual_physical_connection_status = virtual_physical_connection_status
        # The VLAN ID of the hosted connection.
        self.vlan_id = vlan_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.ad_location is not None:
            result['AdLocation'] = self.ad_location

        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.circuit_code is not None:
            result['CircuitCode'] = self.circuit_code

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled_time is not None:
            result['EnabledTime'] = self.enabled_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.expect_spec is not None:
            result['ExpectSpec'] = self.expect_spec

        if self.line_operator is not None:
            result['LineOperator'] = self.line_operator

        if self.loa_status is not None:
            result['LoaStatus'] = self.loa_status

        if self.name is not None:
            result['Name'] = self.name

        if self.order_mode is not None:
            result['OrderMode'] = self.order_mode

        if self.parent_physical_connection_ali_uid is not None:
            result['ParentPhysicalConnectionAliUid'] = self.parent_physical_connection_ali_uid

        if self.parent_physical_connection_id is not None:
            result['ParentPhysicalConnectionId'] = self.parent_physical_connection_id

        if self.peer_location is not None:
            result['PeerLocation'] = self.peer_location

        if self.physical_connection_id is not None:
            result['PhysicalConnectionId'] = self.physical_connection_id

        if self.port_number is not None:
            result['PortNumber'] = self.port_number

        if self.port_type is not None:
            result['PortType'] = self.port_type

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.redundant_physical_connection_id is not None:
            result['RedundantPhysicalConnectionId'] = self.redundant_physical_connection_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.virtual_physical_connection_status is not None:
            result['VirtualPhysicalConnectionStatus'] = self.virtual_physical_connection_status

        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('AdLocation') is not None:
            self.ad_location = m.get('AdLocation')

        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CircuitCode') is not None:
            self.circuit_code = m.get('CircuitCode')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnabledTime') is not None:
            self.enabled_time = m.get('EnabledTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExpectSpec') is not None:
            self.expect_spec = m.get('ExpectSpec')

        if m.get('LineOperator') is not None:
            self.line_operator = m.get('LineOperator')

        if m.get('LoaStatus') is not None:
            self.loa_status = m.get('LoaStatus')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrderMode') is not None:
            self.order_mode = m.get('OrderMode')

        if m.get('ParentPhysicalConnectionAliUid') is not None:
            self.parent_physical_connection_ali_uid = m.get('ParentPhysicalConnectionAliUid')

        if m.get('ParentPhysicalConnectionId') is not None:
            self.parent_physical_connection_id = m.get('ParentPhysicalConnectionId')

        if m.get('PeerLocation') is not None:
            self.peer_location = m.get('PeerLocation')

        if m.get('PhysicalConnectionId') is not None:
            self.physical_connection_id = m.get('PhysicalConnectionId')

        if m.get('PortNumber') is not None:
            self.port_number = m.get('PortNumber')

        if m.get('PortType') is not None:
            self.port_type = m.get('PortType')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RedundantPhysicalConnectionId') is not None:
            self.redundant_physical_connection_id = m.get('RedundantPhysicalConnectionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListVirtualPhysicalConnectionsResponseBodyVirtualPhysicalConnectionsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VirtualPhysicalConnectionStatus') is not None:
            self.virtual_physical_connection_status = m.get('VirtualPhysicalConnectionStatus')

        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')

        return self

class ListVirtualPhysicalConnectionsResponseBodyVirtualPhysicalConnectionsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N that is added to the resource. You can specify at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # It can be up to 64 characters in length and can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The value of tag N that is added to the resource. You can specify at most 20 tag values. The tag value can be an empty string.
        # 
        # It can be up to 128 characters in length and can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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

