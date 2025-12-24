# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class GetLindormEngineConfigResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        engine_configs: List[main_models.GetLindormEngineConfigResponseBodyEngineConfigs] = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.engine_configs = engine_configs
        self.request_id = request_id

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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['EngineConfigs'] = []
        if self.engine_configs is not None:
            for k1 in self.engine_configs:
                result['EngineConfigs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.engine_configs = []
        if m.get('EngineConfigs') is not None:
            for k1 in m.get('EngineConfigs'):
                temp_model = main_models.GetLindormEngineConfigResponseBodyEngineConfigs()
                self.engine_configs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetLindormEngineConfigResponseBodyEngineConfigs(DaraModel):
    def __init__(
        self,
        config_files: List[main_models.GetLindormEngineConfigResponseBodyEngineConfigsConfigFiles] = None,
        engine: str = None,
    ):
        self.config_files = config_files
        self.engine = engine

    def validate(self):
        if self.config_files:
            for v1 in self.config_files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigFiles'] = []
        if self.config_files is not None:
            for k1 in self.config_files:
                result['ConfigFiles'].append(k1.to_map() if k1 else None)

        if self.engine is not None:
            result['Engine'] = self.engine

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_files = []
        if m.get('ConfigFiles') is not None:
            for k1 in m.get('ConfigFiles'):
                temp_model = main_models.GetLindormEngineConfigResponseBodyEngineConfigsConfigFiles()
                self.config_files.append(temp_model.from_map(k1))

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        return self

class GetLindormEngineConfigResponseBodyEngineConfigsConfigFiles(DaraModel):
    def __init__(
        self,
        config_items: List[main_models.GetLindormEngineConfigResponseBodyEngineConfigsConfigFilesConfigItems] = None,
        file_name: str = None,
    ):
        self.config_items = config_items
        self.file_name = file_name

    def validate(self):
        if self.config_items:
            for v1 in self.config_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigItems'] = []
        if self.config_items is not None:
            for k1 in self.config_items:
                result['ConfigItems'].append(k1.to_map() if k1 else None)

        if self.file_name is not None:
            result['FileName'] = self.file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_items = []
        if m.get('ConfigItems') is not None:
            for k1 in m.get('ConfigItems'):
                temp_model = main_models.GetLindormEngineConfigResponseBodyEngineConfigsConfigFilesConfigItems()
                self.config_items.append(temp_model.from_map(k1))

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        return self

class GetLindormEngineConfigResponseBodyEngineConfigsConfigFilesConfigItems(DaraModel):
    def __init__(
        self,
        config_item_key: str = None,
        config_item_value: str = None,
    ):
        self.config_item_key = config_item_key
        self.config_item_value = config_item_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_item_key is not None:
            result['ConfigItemKey'] = self.config_item_key

        if self.config_item_value is not None:
            result['ConfigItemValue'] = self.config_item_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigItemKey') is not None:
            self.config_item_key = m.get('ConfigItemKey')

        if m.get('ConfigItemValue') is not None:
            self.config_item_value = m.get('ConfigItemValue')

        return self

