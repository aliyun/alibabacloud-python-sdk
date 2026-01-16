# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListKibanaPvlNetworkResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListKibanaPvlNetworkResponseBodyResult] = None,
    ):
        # request id
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListKibanaPvlNetworkResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListKibanaPvlNetworkResponseBodyResult(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        endpoint_id: str = None,
        endpoint_name: str = None,
        endpoint_status: str = None,
        pvl_id: str = None,
        security_groups: List[str] = None,
        v_switch_ids_zone: List[main_models.ListKibanaPvlNetworkResponseBodyResultVSwitchIdsZone] = None,
        vpc_id: str = None,
    ):
        self.create_time = create_time
        self.endpoint_id = endpoint_id
        self.endpoint_name = endpoint_name
        self.endpoint_status = endpoint_status
        self.pvl_id = pvl_id
        self.security_groups = security_groups
        self.v_switch_ids_zone = v_switch_ids_zone
        self.vpc_id = vpc_id

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
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.endpoint_id is not None:
            result['endpointId'] = self.endpoint_id

        if self.endpoint_name is not None:
            result['endpointName'] = self.endpoint_name

        if self.endpoint_status is not None:
            result['endpointStatus'] = self.endpoint_status

        if self.pvl_id is not None:
            result['pvlId'] = self.pvl_id

        if self.security_groups is not None:
            result['securityGroups'] = self.security_groups

        result['vSwitchIdsZone'] = []
        if self.v_switch_ids_zone is not None:
            for k1 in self.v_switch_ids_zone:
                result['vSwitchIdsZone'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('endpointId') is not None:
            self.endpoint_id = m.get('endpointId')

        if m.get('endpointName') is not None:
            self.endpoint_name = m.get('endpointName')

        if m.get('endpointStatus') is not None:
            self.endpoint_status = m.get('endpointStatus')

        if m.get('pvlId') is not None:
            self.pvl_id = m.get('pvlId')

        if m.get('securityGroups') is not None:
            self.security_groups = m.get('securityGroups')

        self.v_switch_ids_zone = []
        if m.get('vSwitchIdsZone') is not None:
            for k1 in m.get('vSwitchIdsZone'):
                temp_model = main_models.ListKibanaPvlNetworkResponseBodyResultVSwitchIdsZone()
                self.v_switch_ids_zone.append(temp_model.from_map(k1))

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

class ListKibanaPvlNetworkResponseBodyResultVSwitchIdsZone(DaraModel):
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

