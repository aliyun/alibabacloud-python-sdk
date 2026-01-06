# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class UpdateConfigsRequest(DaraModel):
    def __init__(
        self,
        configs: List[main_models.UpdateConfigsRequestConfigs] = None,
    ):
        # The list of workspace configurations to update or add.
        self.configs = configs

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.UpdateConfigsRequestConfigs()
                self.configs.append(temp_model.from_map(k1))

        return self

class UpdateConfigsRequestConfigs(DaraModel):
    def __init__(
        self,
        category_name: str = None,
        config_key: str = None,
        config_value: str = None,
        labels: List[main_models.UpdateConfigsRequestConfigsLabels] = None,
    ):
        # The category of the configuration item. Supported categories:
        # 
        # *   CommonResourceConfig
        # *   DLCAutoRecycle
        # *   DLCPriorityConfig
        # *   DSWPriorityConfig
        # *   QuotaMaximumDuration
        # *   CommonTagConfig
        self.category_name = category_name
        # The key of the configuration item. Supported keys:
        # 
        # *   tempStoragePath: Temporary storage path. This key can be used only when CategoryName is set to CommonResourceConfig.
        # *   isAutoRecycle: Automatic recycle configuration. This key can be used only when CategoryName is set to DLCAutoRecycle.
        # *   tempStoragePath: Temporary storage path. This key can be used only when CategoryName is set to CommonResourceConfig.
        # *   quotaMaximumDuration: Maximum run time of DLC jobs for a quota. This key can be used only when CategoryName is set to QuotaMaximumDuration.
        # *   predefinedTags: The predefined tags of the workspace. All created resources must have tags.
        self.config_key = config_key
        # The value of the configuration item.
        # 
        # *   When ConfigKey is predefinedTags, the ConfigValue follows this format: [{"Type":"Tag","Key":"Key1","Value":"{"Products":"DLC,DSW,EAS","Values":"value1,value2,value3"}"}]. "Products" indicates the products that use the predefined tags.
        self.config_value = config_value
        # The tags of the configuration item.
        self.labels = labels

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.config_key is not None:
            result['ConfigKey'] = self.config_key

        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')

        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.UpdateConfigsRequestConfigsLabels()
                self.labels.append(temp_model.from_map(k1))

        return self

class UpdateConfigsRequestConfigsLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

