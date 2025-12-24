# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class AssignIpv6AddressesResponseBody(DaraModel):
    def __init__(
        self,
        ipv_6prefix_sets: main_models.AssignIpv6AddressesResponseBodyIpv6PrefixSets = None,
        ipv_6sets: main_models.AssignIpv6AddressesResponseBodyIpv6Sets = None,
        network_interface_id: str = None,
        request_id: str = None,
    ):
        # The IPv6 prefixes of the ENI.
        self.ipv_6prefix_sets = ipv_6prefix_sets
        # The IPv6 addresses assigned to the ENI.
        self.ipv_6sets = ipv_6sets
        # The ENI ID.
        self.network_interface_id = network_interface_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.ipv_6prefix_sets:
            self.ipv_6prefix_sets.validate()
        if self.ipv_6sets:
            self.ipv_6sets.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6prefix_sets is not None:
            result['Ipv6PrefixSets'] = self.ipv_6prefix_sets.to_map()

        if self.ipv_6sets is not None:
            result['Ipv6Sets'] = self.ipv_6sets.to_map()

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6PrefixSets') is not None:
            temp_model = main_models.AssignIpv6AddressesResponseBodyIpv6PrefixSets()
            self.ipv_6prefix_sets = temp_model.from_map(m.get('Ipv6PrefixSets'))

        if m.get('Ipv6Sets') is not None:
            temp_model = main_models.AssignIpv6AddressesResponseBodyIpv6Sets()
            self.ipv_6sets = temp_model.from_map(m.get('Ipv6Sets'))

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AssignIpv6AddressesResponseBodyIpv6Sets(DaraModel):
    def __init__(
        self,
        ipv_6address: List[str] = None,
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

class AssignIpv6AddressesResponseBodyIpv6PrefixSets(DaraModel):
    def __init__(
        self,
        ipv_6prefix: List[str] = None,
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

