# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateNatGatewayResponseBody(DaraModel):
    def __init__(
        self,
        forward_table_ids: main_models.CreateNatGatewayResponseBodyForwardTableIds = None,
        full_nat_table_ids: main_models.CreateNatGatewayResponseBodyFullNatTableIds = None,
        nat_gateway_id: str = None,
        request_id: str = None,
        snat_table_ids: main_models.CreateNatGatewayResponseBodySnatTableIds = None,
    ):
        # A list of DNAT entries.
        self.forward_table_ids = forward_table_ids
        # A list of FULLNAT entries.
        self.full_nat_table_ids = full_nat_table_ids
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id
        # The request ID.
        self.request_id = request_id
        # A list of SNAT entries.
        self.snat_table_ids = snat_table_ids

    def validate(self):
        if self.forward_table_ids:
            self.forward_table_ids.validate()
        if self.full_nat_table_ids:
            self.full_nat_table_ids.validate()
        if self.snat_table_ids:
            self.snat_table_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_table_ids is not None:
            result['ForwardTableIds'] = self.forward_table_ids.to_map()

        if self.full_nat_table_ids is not None:
            result['FullNatTableIds'] = self.full_nat_table_ids.to_map()

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.snat_table_ids is not None:
            result['SnatTableIds'] = self.snat_table_ids.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardTableIds') is not None:
            temp_model = main_models.CreateNatGatewayResponseBodyForwardTableIds()
            self.forward_table_ids = temp_model.from_map(m.get('ForwardTableIds'))

        if m.get('FullNatTableIds') is not None:
            temp_model = main_models.CreateNatGatewayResponseBodyFullNatTableIds()
            self.full_nat_table_ids = temp_model.from_map(m.get('FullNatTableIds'))

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SnatTableIds') is not None:
            temp_model = main_models.CreateNatGatewayResponseBodySnatTableIds()
            self.snat_table_ids = temp_model.from_map(m.get('SnatTableIds'))

        return self

class CreateNatGatewayResponseBodySnatTableIds(DaraModel):
    def __init__(
        self,
        snat_table_id: List[str] = None,
    ):
        self.snat_table_id = snat_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.snat_table_id is not None:
            result['SnatTableId'] = self.snat_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SnatTableId') is not None:
            self.snat_table_id = m.get('SnatTableId')

        return self

class CreateNatGatewayResponseBodyFullNatTableIds(DaraModel):
    def __init__(
        self,
        full_nat_table_id: List[str] = None,
    ):
        self.full_nat_table_id = full_nat_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.full_nat_table_id is not None:
            result['FullNatTableId'] = self.full_nat_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FullNatTableId') is not None:
            self.full_nat_table_id = m.get('FullNatTableId')

        return self

class CreateNatGatewayResponseBodyForwardTableIds(DaraModel):
    def __init__(
        self,
        forward_table_id: List[str] = None,
    ):
        self.forward_table_id = forward_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_table_id is not None:
            result['ForwardTableId'] = self.forward_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardTableId') is not None:
            self.forward_table_id = m.get('ForwardTableId')

        return self

