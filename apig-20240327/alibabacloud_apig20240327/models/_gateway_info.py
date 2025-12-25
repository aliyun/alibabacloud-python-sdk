# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GatewayInfo(DaraModel):
    def __init__(
        self,
        engine_version: str = None,
        gateway_id: str = None,
        name: str = None,
        vpc_info: main_models.GatewayInfoVpcInfo = None,
    ):
        self.engine_version = engine_version
        self.gateway_id = gateway_id
        self.name = name
        self.vpc_info = vpc_info

    def validate(self):
        if self.vpc_info:
            self.vpc_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.name is not None:
            result['name'] = self.name

        if self.vpc_info is not None:
            result['vpcInfo'] = self.vpc_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('vpcInfo') is not None:
            temp_model = main_models.GatewayInfoVpcInfo()
            self.vpc_info = temp_model.from_map(m.get('vpcInfo'))

        return self

class GatewayInfoVpcInfo(DaraModel):
    def __init__(
        self,
        name: str = None,
        vpc_id: str = None,
    ):
        self.name = name
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

