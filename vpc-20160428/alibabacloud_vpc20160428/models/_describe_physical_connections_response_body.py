# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribePhysicalConnectionsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        physical_connection_set: main_models.DescribePhysicalConnectionsResponseBodyPhysicalConnectionSet = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: **10**. Valid values: **1** to **50**.
        self.page_size = page_size
        # The list of Express Connect circuits.
        self.physical_connection_set = physical_connection_set
        # The request ID.
        self.request_id = request_id
        # The number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.physical_connection_set:
            self.physical_connection_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.physical_connection_set is not None:
            result['PhysicalConnectionSet'] = self.physical_connection_set.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PhysicalConnectionSet') is not None:
            temp_model = main_models.DescribePhysicalConnectionsResponseBodyPhysicalConnectionSet()
            self.physical_connection_set = temp_model.from_map(m.get('PhysicalConnectionSet'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribePhysicalConnectionsResponseBodyPhysicalConnectionSet(DaraModel):
    def __init__(
        self,
        physical_connection_type: List[main_models.DescribePhysicalConnectionsResponseBodyPhysicalConnectionSetPhysicalConnectionType] = None,
    ):
        self.physical_connection_type = physical_connection_type

    def validate(self):
        if self.physical_connection_type:
            for v1 in self.physical_connection_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PhysicalConnectionType'] = []
        if self.physical_connection_type is not None:
            for k1 in self.physical_connection_type:
                result['PhysicalConnectionType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.physical_connection_type = []
        if m.get('PhysicalConnectionType') is not None:
            for k1 in m.get('PhysicalConnectionType'):
                temp_model = main_models.DescribePhysicalConnectionsResponseBodyPhysicalConnectionSetPhysicalConnectionType()
                self.physical_connection_type.append(temp_model.from_map(k1))

        return self

class DescribePhysicalConnectionsResponseBodyPhysicalConnectionSetPhysicalConnectionType(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        access_point_type: str = None,
        ad_detail_location: str = None,
        ad_location: str = None,
        bandwidth: int = None,
        business_status: str = None,
        charge_type: str = None,
        circuit_code: str = None,
        creation_time: str = None,
        description: str = None,
        enabled_time: str = None,
        end_time: str = None,
        expect_spec: str = None,
        has_reservation_data: str = None,
        line_operator: str = None,
        loa_status: str = None,
        name: str = None,
        optical_module_model: str = None,
        order_mode: str = None,
        parent_physical_connection_ali_uid: int = None,
        parent_physical_connection_id: str = None,
        peer_location: str = None,
        physical_connection_id: str = None,
        port_number: str = None,
        port_type: str = None,
        product_type: str = None,
        qos_id: str = None,
        redundant_physical_connection_id: str = None,
        reservation_active_time: str = None,
        reservation_internet_charge_type: str = None,
        reservation_order_type: str = None,
        resource_group_id: str = None,
        spec: str = None,
        status: str = None,
        tags: main_models.DescribePhysicalConnectionsResponseBodyPhysicalConnectionSetPhysicalConnectionTypeTags = None,
        type: str = None,
        virtual_physical_connection_count: int = None,
        vlan_id: str = None,
        vpconn_status: str = None,
    ):
        # The ID of the Express Connect circuit.
        self.access_point_id = access_point_id
        # The type of the access point.
        self.access_point_type = access_point_type
        # The information about the data center and rack.
        self.ad_detail_location = ad_detail_location
        # The location of the access point.
        self.ad_location = ad_location
        # The maximum bandwidth of the Express Connect circuit.
        # 
        # Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The status of the Express Connect circuit. Valid values:
        # 
        # *   **Normal**: enabled
        # *   **FinancialLocked**: locked due to overdue payments
        # *   **SecurityLocked**: locked for security reasons
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
        # The time when the Express Connect circuit was enabled.
        self.enabled_time = enabled_time
        # The time when the Express Connect circuit expires.
        self.end_time = end_time
        # The estimated maximum bandwidth of the shared Express Connect circuit. The estimated bandwidth takes effect after you complete the payment.
        # 
        # Unit: **M** (Mbit/s) and **G** (Gbit/s).
        self.expect_spec = expect_spec
        # Indicates whether the data about pending orders is returned. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.has_reservation_data = has_reservation_data
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
        # *   **Applying**: The LOA is pending for approval.
        # *   **Accept**: The LOA is approved.
        # *   **Available**: The LOA is available.
        # *   **Rejected**: The LOA is rejected.
        # *   **Completing**: The Express Connect circuit is under construction.
        # *   **Complete**: The Express Connect circuit is installed.
        # *   **Deleted**: The LOA is deleted.
        self.loa_status = loa_status
        # The name of the Express Connect circuit.
        self.name = name
        self.optical_module_model = optical_module_model
        # The payer for the hosted connection. Valid values:
        # 
        # *   **PayByPhysicalConnectionOwner**: The partner pays for the shared Express Connect circuit.
        # *   **PayByVirtualPhysicalConnectionOwner**: The tenant pays for the shared Express Connect circuit.
        self.order_mode = order_mode
        # The ID of the Alibaba Cloud account to which the parent Express Connect circuit belongs.
        self.parent_physical_connection_ali_uid = parent_physical_connection_ali_uid
        # The ID of the parent Express Connect circuit.
        self.parent_physical_connection_id = parent_physical_connection_id
        # The geographical location of the data center.
        self.peer_location = peer_location
        # The ID of the Express Connect circuit.
        self.physical_connection_id = physical_connection_id
        # The ID of the port on the access device.
        self.port_number = port_number
        # The port type of the Express Connect circuit. Valid values:
        # 
        # *   **100Base-T**: 100 Mbit/s copper Ethernet port
        # *   **1000Base-T**: 1,000 Mbit/s copper Ethernet port
        # *   **1000Base-LX**: 1,000 Mbit/s single-mode optical port (10 km)
        # *   **10GBase-T**: 10,000 Mbit/s copper Ethernet port
        # *   **10GBase-LR**: 10,000 Mbit/s single-mode optical port (10 km)
        # *   **40GBase-LR**: 40,000 Mbit/s single-mode optical port
        # *   **100GBase-LR**: 100,000 Mbit/s single-mode optical port
        # 
        # > Whether 40GBase-LR and 100GBase-LR ports can be created depends on resource supplies. For more information, contact your account manager.
        self.port_type = port_type
        # The type of the Express Connect circuit. Valid values:
        # 
        # *   **VirtualPhysicalConnection**: shared Express Connect circuit
        # *   **PhysicalConnection**: dedicated Express Connect circuit
        self.product_type = product_type
        # The ID of the QoS policy.
        self.qos_id = qos_id
        # The ID of the standby Express Connect circuit.
        self.redundant_physical_connection_id = redundant_physical_connection_id
        # The time when the pending order takes effect.
        self.reservation_active_time = reservation_active_time
        # The billing method of the pending order.
        # 
        # If **PayByBandwidth** is returned, it indicates that the Express Connect circuit is billed on a pay-by-bandwidth basis.
        self.reservation_internet_charge_type = reservation_internet_charge_type
        # The type of the pending order.
        # 
        # If the value is **RENEW**, it indicates that the order is placed for service renewal.
        self.reservation_order_type = reservation_order_type
        # The resource group ID to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The specification of the Express Connect circuit.
        # 
        # Unit: **G** (Gbit/s).
        self.spec = spec
        # The status of the Express Connect circuit. Valid values:
        # 
        # *   **Initial**
        # *   **Approved**
        # *   **Allocating**
        # *   **Allocated**
        # *   **Confirmed**
        # *   **Enabled**
        # *   **Rejected**
        # *   **Canceled**
        # *   **Allocation Failed**
        # *   **Terminating**
        # *   **Terminated**
        self.status = status
        # The tags that are added to the cluster.
        self.tags = tags
        # The type of resource to which the Express Connect circuit is connected. Only **VPC** may be returned.
        self.type = type
        # The number of Express Connect circuits that are established.
        self.virtual_physical_connection_count = virtual_physical_connection_count
        # The VLAN ID of the shared Express Connect circuit.
        self.vlan_id = vlan_id
        # The status of the shared Express Connect circuit. Valid values:
        # 
        # *   **Confirmed**
        # *   **UnConfirmed**
        # *   **Deleted**
        self.vpconn_status = vpconn_status

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.access_point_type is not None:
            result['AccessPointType'] = self.access_point_type

        if self.ad_detail_location is not None:
            result['AdDetailLocation'] = self.ad_detail_location

        if self.ad_location is not None:
            result['AdLocation'] = self.ad_location

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

        if self.has_reservation_data is not None:
            result['HasReservationData'] = self.has_reservation_data

        if self.line_operator is not None:
            result['LineOperator'] = self.line_operator

        if self.loa_status is not None:
            result['LoaStatus'] = self.loa_status

        if self.name is not None:
            result['Name'] = self.name

        if self.optical_module_model is not None:
            result['OpticalModuleModel'] = self.optical_module_model

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

        if self.qos_id is not None:
            result['QosId'] = self.qos_id

        if self.redundant_physical_connection_id is not None:
            result['RedundantPhysicalConnectionId'] = self.redundant_physical_connection_id

        if self.reservation_active_time is not None:
            result['ReservationActiveTime'] = self.reservation_active_time

        if self.reservation_internet_charge_type is not None:
            result['ReservationInternetChargeType'] = self.reservation_internet_charge_type

        if self.reservation_order_type is not None:
            result['ReservationOrderType'] = self.reservation_order_type

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.type is not None:
            result['Type'] = self.type

        if self.virtual_physical_connection_count is not None:
            result['VirtualPhysicalConnectionCount'] = self.virtual_physical_connection_count

        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id

        if self.vpconn_status is not None:
            result['VpconnStatus'] = self.vpconn_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('AccessPointType') is not None:
            self.access_point_type = m.get('AccessPointType')

        if m.get('AdDetailLocation') is not None:
            self.ad_detail_location = m.get('AdDetailLocation')

        if m.get('AdLocation') is not None:
            self.ad_location = m.get('AdLocation')

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

        if m.get('HasReservationData') is not None:
            self.has_reservation_data = m.get('HasReservationData')

        if m.get('LineOperator') is not None:
            self.line_operator = m.get('LineOperator')

        if m.get('LoaStatus') is not None:
            self.loa_status = m.get('LoaStatus')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OpticalModuleModel') is not None:
            self.optical_module_model = m.get('OpticalModuleModel')

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

        if m.get('QosId') is not None:
            self.qos_id = m.get('QosId')

        if m.get('RedundantPhysicalConnectionId') is not None:
            self.redundant_physical_connection_id = m.get('RedundantPhysicalConnectionId')

        if m.get('ReservationActiveTime') is not None:
            self.reservation_active_time = m.get('ReservationActiveTime')

        if m.get('ReservationInternetChargeType') is not None:
            self.reservation_internet_charge_type = m.get('ReservationInternetChargeType')

        if m.get('ReservationOrderType') is not None:
            self.reservation_order_type = m.get('ReservationOrderType')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribePhysicalConnectionsResponseBodyPhysicalConnectionSetPhysicalConnectionTypeTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VirtualPhysicalConnectionCount') is not None:
            self.virtual_physical_connection_count = m.get('VirtualPhysicalConnectionCount')

        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')

        if m.get('VpconnStatus') is not None:
            self.vpconn_status = m.get('VpconnStatus')

        return self

class DescribePhysicalConnectionsResponseBodyPhysicalConnectionSetPhysicalConnectionTypeTags(DaraModel):
    def __init__(
        self,
        tags: List[main_models.DescribePhysicalConnectionsResponseBodyPhysicalConnectionSetPhysicalConnectionTypeTagsTags] = None,
    ):
        self.tags = tags

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
        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.DescribePhysicalConnectionsResponseBodyPhysicalConnectionSetPhysicalConnectionTypeTagsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribePhysicalConnectionsResponseBodyPhysicalConnectionSetPhysicalConnectionTypeTagsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N added to the resource. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The value of tag N added to the resource. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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

