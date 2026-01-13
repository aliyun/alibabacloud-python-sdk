# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class CreateRecallManagementConfigRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        network_configs: List[main_models.CreateRecallManagementConfigRequestNetworkConfigs] = None,
        password: str = None,
        user_name: str = None,
    ):
        self.instance_id = instance_id
        self.network_configs = network_configs
        self.password = password
        self.user_name = user_name

    def validate(self):
        if self.network_configs:
            for v1 in self.network_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['NetworkConfigs'] = []
        if self.network_configs is not None:
            for k1 in self.network_configs:
                result['NetworkConfigs'].append(k1.to_map() if k1 else None)

        if self.password is not None:
            result['Password'] = self.password

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.network_configs = []
        if m.get('NetworkConfigs') is not None:
            for k1 in m.get('NetworkConfigs'):
                temp_model = main_models.CreateRecallManagementConfigRequestNetworkConfigs()
                self.network_configs.append(temp_model.from_map(k1))

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class CreateRecallManagementConfigRequestNetworkConfigs(DaraModel):
    def __init__(
        self,
        v_switch_ids: Dict[str, str] = None,
        vpc_id: str = None,
    ):
        self.v_switch_ids = v_switch_ids
        # Vpc id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

