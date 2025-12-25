# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class CreateGatewayRequest(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        gateway_edition: str = None,
        gateway_type: str = None,
        log_config: main_models.CreateGatewayRequestLogConfig = None,
        name: str = None,
        network_access_config: main_models.CreateGatewayRequestNetworkAccessConfig = None,
        resource_group_id: str = None,
        spec: str = None,
        tag: List[main_models.CreateGatewayRequestTag] = None,
        vpc_id: str = None,
        zone_config: main_models.CreateGatewayRequestZoneConfig = None,
    ):
        # The billing method.
        # 
        # Valid values:
        # 
        # *   POSTPAY
        # *   PREPAY
        self.charge_type = charge_type
        # The gateway edition.
        self.gateway_edition = gateway_edition
        # The type of the gateway.
        # 
        # Valid values:
        # 
        # *   AI
        # *   API
        self.gateway_type = gateway_type
        # The logging configurations.
        self.log_config = log_config
        # The name of the gateway instance.
        self.name = name
        # The network access configuration.
        self.network_access_config = network_access_config
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The specifications of the node.
        self.spec = spec
        # The tags.
        self.tag = tag
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The zone settings.
        self.zone_config = zone_config

    def validate(self):
        if self.log_config:
            self.log_config.validate()
        if self.network_access_config:
            self.network_access_config.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()
        if self.zone_config:
            self.zone_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type

        if self.gateway_edition is not None:
            result['gatewayEdition'] = self.gateway_edition

        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.network_access_config is not None:
            result['networkAccessConfig'] = self.network_access_config.to_map()

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.spec is not None:
            result['spec'] = self.spec

        result['tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['tag'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.zone_config is not None:
            result['zoneConfig'] = self.zone_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')

        if m.get('gatewayEdition') is not None:
            self.gateway_edition = m.get('gatewayEdition')

        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

        if m.get('logConfig') is not None:
            temp_model = main_models.CreateGatewayRequestLogConfig()
            self.log_config = temp_model.from_map(m.get('logConfig'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networkAccessConfig') is not None:
            temp_model = main_models.CreateGatewayRequestNetworkAccessConfig()
            self.network_access_config = temp_model.from_map(m.get('networkAccessConfig'))

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        self.tag = []
        if m.get('tag') is not None:
            for k1 in m.get('tag'):
                temp_model = main_models.CreateGatewayRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('zoneConfig') is not None:
            temp_model = main_models.CreateGatewayRequestZoneConfig()
            self.zone_config = temp_model.from_map(m.get('zoneConfig'))

        return self

class CreateGatewayRequestZoneConfig(DaraModel):
    def __init__(
        self,
        select_option: str = None,
        v_switch_id: str = None,
        zones: List[main_models.CreateGatewayRequestZoneConfigZones] = None,
    ):
        # The option for selecting the zone.
        # 
        # Valid values:
        # 
        # *   Auto
        # *   Manual
        self.select_option = select_option
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The supported zones.
        self.zones = zones

    def validate(self):
        if self.zones:
            for v1 in self.zones:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.select_option is not None:
            result['selectOption'] = self.select_option

        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id

        result['zones'] = []
        if self.zones is not None:
            for k1 in self.zones:
                result['zones'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('selectOption') is not None:
            self.select_option = m.get('selectOption')

        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')

        self.zones = []
        if m.get('zones') is not None:
            for k1 in m.get('zones'):
                temp_model = main_models.CreateGatewayRequestZoneConfigZones()
                self.zones.append(temp_model.from_map(k1))

        return self

class CreateGatewayRequestZoneConfigZones(DaraModel):
    def __init__(
        self,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

class CreateGatewayRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class CreateGatewayRequestNetworkAccessConfig(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The network access type.
        # 
        # Valid values:
        # 
        # *   InternetAndIntranet
        # *   Intranet
        # *   Internet
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateGatewayRequestLogConfig(DaraModel):
    def __init__(
        self,
        sls: main_models.CreateGatewayRequestLogConfigSls = None,
    ):
        # The Simple Log Service configurations.
        self.sls = sls

    def validate(self):
        if self.sls:
            self.sls.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sls is not None:
            result['sls'] = self.sls.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sls') is not None:
            temp_model = main_models.CreateGatewayRequestLogConfigSls()
            self.sls = temp_model.from_map(m.get('sls'))

        return self

class CreateGatewayRequestLogConfigSls(DaraModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        # Indicates if enabled.
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        return self

