# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class UpdateRecallManagementConfigRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        network_configs: List[main_models.UpdateRecallManagementConfigRequestNetworkConfigs] = None,
        password: str = None,
    ):
        self.instance_id = instance_id
        self.network_configs = network_configs
        self.password = password

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.network_configs = []
        if m.get('NetworkConfigs') is not None:
            for k1 in m.get('NetworkConfigs'):
                temp_model = main_models.UpdateRecallManagementConfigRequestNetworkConfigs()
                self.network_configs.append(temp_model.from_map(k1))

        if m.get('Password') is not None:
            self.password = m.get('Password')

        return self

class UpdateRecallManagementConfigRequestNetworkConfigs(DaraModel):
    def __init__(
        self,
        vpc_id: str = None,
        vswitch_ids: Dict[str, str] = None,
    ):
        self.vpc_id = vpc_id
        self.vswitch_ids = vswitch_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_ids is not None:
            result['VswitchIds'] = self.vswitch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchIds') is not None:
            self.vswitch_ids = m.get('VswitchIds')

        return self

