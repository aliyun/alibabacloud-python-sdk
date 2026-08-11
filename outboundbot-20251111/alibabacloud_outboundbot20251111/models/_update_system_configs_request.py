# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class UpdateSystemConfigsRequest(DaraModel):
    def __init__(
        self,
        configs: List[main_models.UpdateSystemConfigsRequestConfigs] = None,
        object_id: str = None,
        object_type: str = None,
    ):
        # The list of configurations.
        self.configs = configs
        # The configuration type ID. If ObjectType is set to INSTANCE, this parameter specifies the instance ID. If ObjectType is set to TENANT, this parameter specifies the tenant ID.
        self.object_id = object_id
        # The configuration type. Valid values:
        # - INSTANCE: instance level.
        # - TENANT: tenant level.
        self.object_type = object_type

    def validate(self):
        if self.configs:
            for v1 in self.configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Configs'] = []
        if self.configs is not None:
            for k1 in self.configs:
                result['Configs'].append(k1.to_map() if k1 else None)

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.UpdateSystemConfigsRequestConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        return self

class UpdateSystemConfigsRequestConfigs(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The system configuration name. Valid values:
        # - callableTime: the outbound job window.
        # - calleeDailyAttemptLimit: the maximum number of daily calls to a single callee number.
        self.name = name
        # The configuration value.
        # 
        # - If Name is set to callableTime, a sample Value is [{"beginTime":"09:00:00","endTime":"12:00:00"},{"beginTime":"14:00:00","endTime":"18:00:00"}].
        # 
        # - If Name is set to calleeDailyAttemptLimit, the Value is an integer from 1 to 50.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

