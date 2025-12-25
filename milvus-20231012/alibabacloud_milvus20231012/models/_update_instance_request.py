# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_milvus20231012 import models as main_models
from darabonba.model import DaraModel

class UpdateInstanceRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        auto_backup: bool = None,
        components: List[main_models.UpdateInstanceRequestComponents] = None,
        configuration: str = None,
        ha: bool = None,
        instance_id: str = None,
        instance_name: str = None,
        client_token: str = None,
    ):
        self.region_id = region_id
        self.auto_backup = auto_backup
        self.components = components
        self.configuration = configuration
        self.ha = ha
        # This parameter is required.
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.client_token = client_token

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.auto_backup is not None:
            result['autoBackup'] = self.auto_backup

        result['components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['components'].append(k1.to_map() if k1 else None)

        if self.configuration is not None:
            result['configuration'] = self.configuration

        if self.ha is not None:
            result['ha'] = self.ha

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_name is not None:
            result['instanceName'] = self.instance_name

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('autoBackup') is not None:
            self.auto_backup = m.get('autoBackup')

        self.components = []
        if m.get('components') is not None:
            for k1 in m.get('components'):
                temp_model = main_models.UpdateInstanceRequestComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('configuration') is not None:
            self.configuration = m.get('configuration')

        if m.get('ha') is not None:
            self.ha = m.get('ha')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class UpdateInstanceRequestComponents(DaraModel):
    def __init__(
        self,
        cu_num: int = None,
        replica: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.cu_num = cu_num
        # This parameter is required.
        self.replica = replica
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu_num is not None:
            result['cuNum'] = self.cu_num

        if self.replica is not None:
            result['replica'] = self.replica

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cuNum') is not None:
            self.cu_num = m.get('cuNum')

        if m.get('replica') is not None:
            self.replica = m.get('replica')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

