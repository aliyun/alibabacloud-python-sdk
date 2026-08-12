# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class InitSasModuleRuleRequest(DaraModel):
    def __init__(
        self,
        auto_bind: int = None,
        instances: List[main_models.InitSasModuleRuleRequestInstances] = None,
        is_trial: bool = None,
        region_id: str = None,
    ):
        # Specifies whether to enable automatic binding. Valid values:
        # 
        # - **0**: Disabled.
        # - **1**: Enabled.
        self.auto_bind = auto_bind
        # The list of instances.
        self.instances = instances
        # Specifies whether to use the trial version.
        self.is_trial = is_trial
        # The region ID of the access control instance.
        self.region_id = region_id

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_bind is not None:
            result['AutoBind'] = self.auto_bind

        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.is_trial is not None:
            result['IsTrial'] = self.is_trial

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoBind') is not None:
            self.auto_bind = m.get('AutoBind')

        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.InitSasModuleRuleRequestInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('IsTrial') is not None:
            self.is_trial = m.get('IsTrial')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class InitSasModuleRuleRequestInstances(DaraModel):
    def __init__(
        self,
        cores: str = None,
        instance_id: str = None,
        region_id: str = None,
        uuid: str = None,
    ):
        # The number of CPU cores of the asset.
        self.cores = cores
        # The instance ID.
        self.instance_id = instance_id
        # The region of the cloud phone.
        self.region_id = region_id
        # The UUID of the instance.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cores is not None:
            result['Cores'] = self.cores

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

