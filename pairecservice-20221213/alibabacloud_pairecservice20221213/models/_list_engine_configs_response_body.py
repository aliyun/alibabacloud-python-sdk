# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListEngineConfigsResponseBody(DaraModel):
    def __init__(
        self,
        engine_configs: List[main_models.ListEngineConfigsResponseBodyEngineConfigs] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.engine_configs = engine_configs
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.engine_configs:
            for v1 in self.engine_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EngineConfigs'] = []
        if self.engine_configs is not None:
            for k1 in self.engine_configs:
                result['EngineConfigs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.engine_configs = []
        if m.get('EngineConfigs') is not None:
            for k1 in m.get('EngineConfigs'):
                temp_model = main_models.ListEngineConfigsResponseBodyEngineConfigs()
                self.engine_configs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListEngineConfigsResponseBodyEngineConfigs(DaraModel):
    def __init__(
        self,
        config_value: str = None,
        description: str = None,
        engine_config_id: str = None,
        environment: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        gmt_released_time: str = None,
        name: str = None,
        status: str = None,
        version: str = None,
    ):
        self.config_value = config_value
        self.description = description
        self.engine_config_id = engine_config_id
        self.environment = environment
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.gmt_released_time = gmt_released_time
        self.name = name
        self.status = status
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        if self.description is not None:
            result['Description'] = self.description

        if self.engine_config_id is not None:
            result['EngineConfigId'] = self.engine_config_id

        if self.environment is not None:
            result['Environment'] = self.environment

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.gmt_released_time is not None:
            result['GmtReleasedTime'] = self.gmt_released_time

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EngineConfigId') is not None:
            self.engine_config_id = m.get('EngineConfigId')

        if m.get('Environment') is not None:
            self.environment = m.get('Environment')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('GmtReleasedTime') is not None:
            self.gmt_released_time = m.get('GmtReleasedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

