# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class EnableKibanaPvlNetworkRequest(DaraModel):
    def __init__(
        self,
        endpoint_name: str = None,
        security_groups: List[str] = None,
        v_switch_ids_zone: List[main_models.EnableKibanaPvlNetworkRequestVSwitchIdsZone] = None,
        vpc_id: str = None,
        client_token: str = None,
    ):
        self.endpoint_name = endpoint_name
        # This parameter is required.
        self.security_groups = security_groups
        self.v_switch_ids_zone = v_switch_ids_zone
        self.vpc_id = vpc_id
        self.client_token = client_token

    def validate(self):
        if self.v_switch_ids_zone:
            for v1 in self.v_switch_ids_zone:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_name is not None:
            result['endpointName'] = self.endpoint_name

        if self.security_groups is not None:
            result['securityGroups'] = self.security_groups

        result['vSwitchIdsZone'] = []
        if self.v_switch_ids_zone is not None:
            for k1 in self.v_switch_ids_zone:
                result['vSwitchIdsZone'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpointName') is not None:
            self.endpoint_name = m.get('endpointName')

        if m.get('securityGroups') is not None:
            self.security_groups = m.get('securityGroups')

        self.v_switch_ids_zone = []
        if m.get('vSwitchIdsZone') is not None:
            for k1 in m.get('vSwitchIdsZone'):
                temp_model = main_models.EnableKibanaPvlNetworkRequestVSwitchIdsZone()
                self.v_switch_ids_zone.append(temp_model.from_map(k1))

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class EnableKibanaPvlNetworkRequestVSwitchIdsZone(DaraModel):
    def __init__(
        self,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        self.vswitch_id = vswitch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

