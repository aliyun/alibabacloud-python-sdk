# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class CreateLogstashRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        network_config: main_models.CreateLogstashRequestNetworkConfig = None,
        node_amount: int = None,
        node_spec: main_models.CreateLogstashRequestNodeSpec = None,
        payment_info: main_models.CreateLogstashRequestPaymentInfo = None,
        payment_type: str = None,
        resource_group_id: str = None,
        version: str = None,
        client_token: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.network_config = network_config
        # This parameter is required.
        self.node_amount = node_amount
        # This parameter is required.
        self.node_spec = node_spec
        self.payment_info = payment_info
        self.payment_type = payment_type
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.version = version
        self.client_token = client_token

    def validate(self):
        if self.network_config:
            self.network_config.validate()
        if self.node_spec:
            self.node_spec.validate()
        if self.payment_info:
            self.payment_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()

        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount

        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()

        if self.payment_info is not None:
            result['paymentInfo'] = self.payment_info.to_map()

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.version is not None:
            result['version'] = self.version

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('networkConfig') is not None:
            temp_model = main_models.CreateLogstashRequestNetworkConfig()
            self.network_config = temp_model.from_map(m.get('networkConfig'))

        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')

        if m.get('nodeSpec') is not None:
            temp_model = main_models.CreateLogstashRequestNodeSpec()
            self.node_spec = temp_model.from_map(m.get('nodeSpec'))

        if m.get('paymentInfo') is not None:
            temp_model = main_models.CreateLogstashRequestPaymentInfo()
            self.payment_info = temp_model.from_map(m.get('paymentInfo'))

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class CreateLogstashRequestPaymentInfo(DaraModel):
    def __init__(
        self,
        auto_renew_duration: int = None,
        duration: int = None,
        is_auto_renew: bool = None,
        pricing_cycle: str = None,
    ):
        self.auto_renew_duration = auto_renew_duration
        self.duration = duration
        self.is_auto_renew = is_auto_renew
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew_duration is not None:
            result['autoRenewDuration'] = self.auto_renew_duration

        if self.duration is not None:
            result['duration'] = self.duration

        if self.is_auto_renew is not None:
            result['isAutoRenew'] = self.is_auto_renew

        if self.pricing_cycle is not None:
            result['pricingCycle'] = self.pricing_cycle

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRenewDuration') is not None:
            self.auto_renew_duration = m.get('autoRenewDuration')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('isAutoRenew') is not None:
            self.is_auto_renew = m.get('isAutoRenew')

        if m.get('pricingCycle') is not None:
            self.pricing_cycle = m.get('pricingCycle')

        return self

class CreateLogstashRequestNodeSpec(DaraModel):
    def __init__(
        self,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.disk = disk
        self.disk_type = disk_type
        # This parameter is required.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk is not None:
            result['disk'] = self.disk

        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.spec is not None:
            result['spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disk') is not None:
            self.disk = m.get('disk')

        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        return self

class CreateLogstashRequestNetworkConfig(DaraModel):
    def __init__(
        self,
        type: str = None,
        vpc_id: str = None,
        vs_area: str = None,
        vswitch_id: str = None,
    ):
        self.type = type
        # This parameter is required.
        self.vpc_id = vpc_id
        # This parameter is required.
        self.vs_area = vs_area
        # This parameter is required.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.vs_area is not None:
            result['vsArea'] = self.vs_area

        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')

        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')

        return self

