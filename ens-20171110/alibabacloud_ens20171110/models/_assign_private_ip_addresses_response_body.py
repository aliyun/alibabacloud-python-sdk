# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class AssignPrivateIpAddressesResponseBody(DaraModel):
    def __init__(
        self,
        assigned_private_ip_addresses_set: main_models.AssignPrivateIpAddressesResponseBodyAssignedPrivateIpAddressesSet = None,
        request_id: str = None,
    ):
        # Details about the ENI and the secondary private IP addresses that are assigned to the ENI.
        self.assigned_private_ip_addresses_set = assigned_private_ip_addresses_set
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.assigned_private_ip_addresses_set:
            self.assigned_private_ip_addresses_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assigned_private_ip_addresses_set is not None:
            result['AssignedPrivateIpAddressesSet'] = self.assigned_private_ip_addresses_set.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignedPrivateIpAddressesSet') is not None:
            temp_model = main_models.AssignPrivateIpAddressesResponseBodyAssignedPrivateIpAddressesSet()
            self.assigned_private_ip_addresses_set = temp_model.from_map(m.get('AssignedPrivateIpAddressesSet'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AssignPrivateIpAddressesResponseBodyAssignedPrivateIpAddressesSet(DaraModel):
    def __init__(
        self,
        network_interface_id: str = None,
        private_ip_set: List[str] = None,
    ):
        # The ID of the ENI.
        self.network_interface_id = network_interface_id
        # The assigned private IP addresses.
        self.private_ip_set = private_ip_set

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.private_ip_set is not None:
            result['PrivateIpSet'] = self.private_ip_set

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('PrivateIpSet') is not None:
            self.private_ip_set = m.get('PrivateIpSet')

        return self

