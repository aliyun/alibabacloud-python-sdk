# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeVirtualBorderRoutersForPhysicalConnectionResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        virtual_border_router_for_physical_connection_set: main_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponseBodyVirtualBorderRouterForPhysicalConnectionSet = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.virtual_border_router_for_physical_connection_set = virtual_border_router_for_physical_connection_set

    def validate(self):
        if self.virtual_border_router_for_physical_connection_set:
            self.virtual_border_router_for_physical_connection_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.virtual_border_router_for_physical_connection_set is not None:
            result['VirtualBorderRouterForPhysicalConnectionSet'] = self.virtual_border_router_for_physical_connection_set.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('VirtualBorderRouterForPhysicalConnectionSet') is not None:
            temp_model = main_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponseBodyVirtualBorderRouterForPhysicalConnectionSet()
            self.virtual_border_router_for_physical_connection_set = temp_model.from_map(m.get('VirtualBorderRouterForPhysicalConnectionSet'))

        return self

class DescribeVirtualBorderRoutersForPhysicalConnectionResponseBodyVirtualBorderRouterForPhysicalConnectionSet(DaraModel):
    def __init__(
        self,
        virtual_border_router_for_physical_connection_type: List[main_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponseBodyVirtualBorderRouterForPhysicalConnectionSetVirtualBorderRouterForPhysicalConnectionType] = None,
    ):
        self.virtual_border_router_for_physical_connection_type = virtual_border_router_for_physical_connection_type

    def validate(self):
        if self.virtual_border_router_for_physical_connection_type:
            for v1 in self.virtual_border_router_for_physical_connection_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VirtualBorderRouterForPhysicalConnectionType'] = []
        if self.virtual_border_router_for_physical_connection_type is not None:
            for k1 in self.virtual_border_router_for_physical_connection_type:
                result['VirtualBorderRouterForPhysicalConnectionType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.virtual_border_router_for_physical_connection_type = []
        if m.get('VirtualBorderRouterForPhysicalConnectionType') is not None:
            for k1 in m.get('VirtualBorderRouterForPhysicalConnectionType'):
                temp_model = main_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponseBodyVirtualBorderRouterForPhysicalConnectionSetVirtualBorderRouterForPhysicalConnectionType()
                self.virtual_border_router_for_physical_connection_type.append(temp_model.from_map(k1))

        return self

class DescribeVirtualBorderRoutersForPhysicalConnectionResponseBodyVirtualBorderRouterForPhysicalConnectionSetVirtualBorderRouterForPhysicalConnectionType(DaraModel):
    def __init__(
        self,
        activation_time: str = None,
        circuit_code: str = None,
        creation_time: str = None,
        recovery_time: str = None,
        termination_time: str = None,
        vbr_id: str = None,
        vbr_owner_uid: int = None,
        vlan_id: int = None,
    ):
        self.activation_time = activation_time
        self.circuit_code = circuit_code
        self.creation_time = creation_time
        self.recovery_time = recovery_time
        self.termination_time = termination_time
        self.vbr_id = vbr_id
        self.vbr_owner_uid = vbr_owner_uid
        self.vlan_id = vlan_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activation_time is not None:
            result['ActivationTime'] = self.activation_time

        if self.circuit_code is not None:
            result['CircuitCode'] = self.circuit_code

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.recovery_time is not None:
            result['RecoveryTime'] = self.recovery_time

        if self.termination_time is not None:
            result['TerminationTime'] = self.termination_time

        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id

        if self.vbr_owner_uid is not None:
            result['VbrOwnerUid'] = self.vbr_owner_uid

        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivationTime') is not None:
            self.activation_time = m.get('ActivationTime')

        if m.get('CircuitCode') is not None:
            self.circuit_code = m.get('CircuitCode')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('RecoveryTime') is not None:
            self.recovery_time = m.get('RecoveryTime')

        if m.get('TerminationTime') is not None:
            self.termination_time = m.get('TerminationTime')

        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')

        if m.get('VbrOwnerUid') is not None:
            self.vbr_owner_uid = m.get('VbrOwnerUid')

        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')

        return self

