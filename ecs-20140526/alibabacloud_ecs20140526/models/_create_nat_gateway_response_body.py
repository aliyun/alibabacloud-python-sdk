# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreateNatGatewayResponseBody(DaraModel):
    def __init__(
        self,
        bandwidth_package_ids: main_models.CreateNatGatewayResponseBodyBandwidthPackageIds = None,
        forward_table_ids: main_models.CreateNatGatewayResponseBodyForwardTableIds = None,
        nat_gateway_id: str = None,
        request_id: str = None,
    ):
        self.bandwidth_package_ids = bandwidth_package_ids
        self.forward_table_ids = forward_table_ids
        self.nat_gateway_id = nat_gateway_id
        self.request_id = request_id

    def validate(self):
        if self.bandwidth_package_ids:
            self.bandwidth_package_ids.validate()
        if self.forward_table_ids:
            self.forward_table_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_package_ids is not None:
            result['BandwidthPackageIds'] = self.bandwidth_package_ids.to_map()

        if self.forward_table_ids is not None:
            result['ForwardTableIds'] = self.forward_table_ids.to_map()

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackageIds') is not None:
            temp_model = main_models.CreateNatGatewayResponseBodyBandwidthPackageIds()
            self.bandwidth_package_ids = temp_model.from_map(m.get('BandwidthPackageIds'))

        if m.get('ForwardTableIds') is not None:
            temp_model = main_models.CreateNatGatewayResponseBodyForwardTableIds()
            self.forward_table_ids = temp_model.from_map(m.get('ForwardTableIds'))

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

class CreateNatGatewayResponseBodyBandwidthPackageIds(DaraModel):
    def __init__(
        self,
        bandwidth_package_id: List[str] = None,
    ):
        self.bandwidth_package_id = bandwidth_package_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        return self

