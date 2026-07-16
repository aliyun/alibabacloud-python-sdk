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
        # The number of entries returned in this request.
        self.count = count
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # - If **NextToken** is not returned, no more results are available.
        # 
        # - If a value is returned for **NextToken**, use it in the next request to retrieve the subsequent page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count
        # A list of virtual physical connections.
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
        # The ID of the access point.
        self.access_point_id = access_point_id
        # The physical location of the access device for the physical connection.
        self.ad_location = ad_location
        # The ID of the Alibaba Cloud account that owns the virtual physical connection.
        self.ali_uid = ali_uid
        # The bandwidth of the physical connection. Unit: Mbps.
        self.bandwidth = bandwidth
        # The business status of the physical connection. Valid values:
        # 
        # - **Normal**: The connection is running as expected.
        # 
        # - **FinancialLocked**: The connection is locked due to an overdue payment.
        # 
        # - **SecurityLocked**: The connection is locked for security reasons.
        self.business_status = business_status
        # The billing method of the physical connection.
        # 
        # The only valid value is **Prepaid**, which corresponds to the subscription billing method.
        self.charge_type = charge_type
        # The circuit code of the physical connection, which is provided by the carrier.
        self.circuit_code = circuit_code
        # The time the physical connection was created.
        self.creation_time = creation_time
        # The description of the physical connection.
        self.description = description
        # The time the physical connection was enabled.
        self.enabled_time = enabled_time
        # The expiration time of the virtual physical connection.
        # 
        # The time is in UTC and follows the `YYYY-MM-DDThh:mm:ssZ` format (ISO 8601).
        self.end_time = end_time
        # The expected bandwidth for the virtual physical connection. This bandwidth is applied after the payment is completed.
        # 
        # **M** indicates Mbps, and **G** indicates Gbps.
        self.expect_spec = expect_spec
        # The carrier that provides the physical connection. Valid values include:
        # 
        # - **CT**: China Telecom.
        # 
        # - **CU**: China Unicom.
        # 
        # - **CM**: China Mobile.
        # 
        # - **CO**: other Chinese carriers.
        # 
        # - **Equinix**: Equinix.
        # 
        # - **Other**: other carriers outside China.
        self.line_operator = line_operator
        # The status of the Letter of Authorization (LOA). Valid values:
        # 
        # - **Applying**: The LOA request is being processed.
        # 
        # - **Accept**: The LOA application is approved.
        # 
        # - **Available**: The LOA is generated and ready for use.
        # 
        # - **Rejected**: The LOA request is rejected.
        # 
        # - **Completing**: The physical connection is being provisioned.
        # 
        # - **Complete**: Provisioning is complete.
        # 
        # - **Deleted**: The LOA is deleted.
        self.loa_status = loa_status
        # The name of the physical connection.
        self.name = name
        # The billing method of the virtual physical connection. Valid values:
        # 
        # - **PayByPhysicalConnectionOwner**: The owner of the parent physical connection pays.
        # 
        # - **PayByVirtualPhysicalConnectionOwner**: The owner of the virtual physical connection pays.
        self.order_mode = order_mode
        # The ID of the Alibaba Cloud account that owns the parent physical connection.
        self.parent_physical_connection_ali_uid = parent_physical_connection_ali_uid
        # The ID of the parent physical connection.
        self.parent_physical_connection_id = parent_physical_connection_id
        # The location of the on-premises data center.
        self.peer_location = peer_location
        # The ID of the virtual physical connection.
        self.physical_connection_id = physical_connection_id
        # The port number of the access device for the physical connection.
        self.port_number = port_number
        # The port type of the physical connection access point. Valid values:
        # 
        # - **100Base-T**: 100 Mbps copper port.
        # 
        # - **1000Base-T**: 1 Gbps copper port.
        # 
        # - **1000Base-LX**: 1 Gbps single-mode optical port (10 km).
        # 
        # - **10GBase-T**: 10 Gbps copper port.
        # 
        # - **10GBase-LR**: 10 Gbps single-mode optical port (10 km).
        # 
        # - **40GBase-LR**: 40 Gbps single-mode optical port.
        # 
        # - **100GBase-LR**: 100 Gbps single-mode optical port.
        self.port_type = port_type
        # The type of the physical connection. Valid values:
        # 
        # - **VirtualPhysicalConnection**: a virtual physical connection.
        # 
        # - **PhysicalConnection**: a dedicated physical connection.
        self.product_type = product_type
        # The ID of the redundant physical connection.
        self.redundant_physical_connection_id = redundant_physical_connection_id
        # The ID of the resource group to which the virtual physical connection belongs.
        self.resource_group_id = resource_group_id
        # The bandwidth of the virtual physical connection.
        # 
        # M indicates Mbps, and G indicates Gbps.
        self.spec = spec
        # The status of the physical connection. Valid values:
        # 
        # - **Initial**: The application is under review.
        # 
        # - **Approved**: The application is approved.
        # 
        # - **Allocating**: Resources are being allocated.
        # 
        # - **Allocated**: The connection is ready for provisioning.
        # 
        # - **Confirmed**: Awaiting user confirmation.
        # 
        # - **Enabled**: The connection is enabled.
        # 
        # - **Rejected**: The application is rejected.
        # 
        # - **Canceled**: The application is canceled.
        # 
        # - **Allocation Failed**: Resource allocation failed.
        # 
        # - **Terminated**: The connection is terminated.
        self.status = status
        # A list of tags.
        self.tags = tags
        # The type of the physical connection. The default value is **VPC**.
        self.type = type
        # The business status of the virtual physical connection. Valid values:
        # 
        # - **Confirmed**: The virtual physical connection has been accepted by the recipient.
        # 
        # - **UnConfirmed**: The virtual physical connection is awaiting acceptance.
        # 
        # - **Deleted**: The virtual physical connection is deleted.
        self.virtual_physical_connection_status = virtual_physical_connection_status
        # The VLAN ID of the virtual physical connection.
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
        # The tag key, which cannot be an empty string. You can specify up to 20 tag keys.
        # 
        # The key can be up to 64 characters in length and can contain digits, periods (.), underscores (_), and hyphens (-). The key cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The value can be up to 128 characters in length. It can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
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

