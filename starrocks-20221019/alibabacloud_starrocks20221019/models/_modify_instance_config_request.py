# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class ModifyInstanceConfigRequest(DaraModel):
    def __init__(
        self,
        add_config_list: str = None,
        config_list: str = None,
        delete_config_list: str = None,
        instance_id: str = None,
        reason: str = None,
        configs_to_add: List[main_models.InstanceConfigDto] = None,
        configs_to_delete: List[main_models.InstanceConfigDto] = None,
        configs_to_update: List[main_models.InstanceConfigDto] = None,
        fast_mode: bool = None,
        restart: bool = None,
    ):
        self.add_config_list = add_config_list
        self.config_list = config_list
        self.delete_config_list = delete_config_list
        # This parameter is required.
        self.instance_id = instance_id
        self.reason = reason
        self.configs_to_add = configs_to_add
        self.configs_to_delete = configs_to_delete
        self.configs_to_update = configs_to_update
        self.fast_mode = fast_mode
        self.restart = restart

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
        if self.add_config_list is not None:
            result['AddConfigList'] = self.add_config_list

        if self.config_list is not None:
            result['ConfigList'] = self.config_list

        if self.delete_config_list is not None:
            result['DeleteConfigList'] = self.delete_config_list

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.reason is not None:
            result['Reason'] = self.reason

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

        if self.fast_mode is not None:
            result['fastMode'] = self.fast_mode

        if self.restart is not None:
            result['restart'] = self.restart

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddConfigList') is not None:
            self.add_config_list = m.get('AddConfigList')

        if m.get('ConfigList') is not None:
            self.config_list = m.get('ConfigList')

        if m.get('DeleteConfigList') is not None:
            self.delete_config_list = m.get('DeleteConfigList')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

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

        if m.get('fastMode') is not None:
            self.fast_mode = m.get('fastMode')

        if m.get('restart') is not None:
            self.restart = m.get('restart')

        return self

