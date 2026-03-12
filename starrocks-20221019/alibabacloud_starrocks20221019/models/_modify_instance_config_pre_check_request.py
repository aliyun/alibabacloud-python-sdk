# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class ModifyInstanceConfigPreCheckRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        configs_to_add: List[main_models.InstanceConfigDto] = None,
        configs_to_delete: List[main_models.InstanceConfigDto] = None,
        configs_to_update: List[main_models.InstanceConfigDto] = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.configs_to_add = configs_to_add
        self.configs_to_delete = configs_to_delete
        self.configs_to_update = configs_to_update

    def validate(self):
        if self.configs_to_add:
            for v1 in self.configs_to_add:
                 if v1:
                    v1.validate()
        if self.configs_to_delete:
            for v1 in self.configs_to_delete:
                 if v1:
                    v1.validate()
        if self.configs_to_update:
            for v1 in self.configs_to_update:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['configsToAdd'] = []
        if self.configs_to_add is not None:
            for k1 in self.configs_to_add:
                result['configsToAdd'].append(k1.to_map() if k1 else None)

        result['configsToDelete'] = []
        if self.configs_to_delete is not None:
            for k1 in self.configs_to_delete:
                result['configsToDelete'].append(k1.to_map() if k1 else None)

        result['configsToUpdate'] = []
        if self.configs_to_update is not None:
            for k1 in self.configs_to_update:
                result['configsToUpdate'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.configs_to_add = []
        if m.get('configsToAdd') is not None:
            for k1 in m.get('configsToAdd'):
                temp_model = main_models.InstanceConfigDto()
                self.configs_to_add.append(temp_model.from_map(k1))

        self.configs_to_delete = []
        if m.get('configsToDelete') is not None:
            for k1 in m.get('configsToDelete'):
                temp_model = main_models.InstanceConfigDto()
                self.configs_to_delete.append(temp_model.from_map(k1))

        self.configs_to_update = []
        if m.get('configsToUpdate') is not None:
            for k1 in m.get('configsToUpdate'):
                temp_model = main_models.InstanceConfigDto()
                self.configs_to_update.append(temp_model.from_map(k1))

        return self

