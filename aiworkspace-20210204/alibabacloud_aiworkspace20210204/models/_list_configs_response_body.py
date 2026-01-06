# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class ListConfigsResponseBody(DaraModel):
    def __init__(
        self,
        configs: List[main_models.ListConfigsResponseBodyConfigs] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The configuration items.
        self.configs = configs
        # The request ID.
        self.request_id = request_id
        # The number of items returned.
        self.total_count = total_count

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.ListConfigsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListConfigsResponseBodyConfigs(DaraModel):
    def __init__(
        self,
        config_key: str = None,
        config_value: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        labels: List[main_models.ListConfigsResponseBodyConfigsLabels] = None,
    ):
        # The key of the configuration item. Supported keys:
        # 
        # *   tempStoragePath: Temporary storage path. This key can be used only when CategoryName is set to CommonResourceConfig.
        # *   isAutoRecycle: Automatic recycle configuration. This key can be used only when CategoryName is set to DLCAutoRecycle.
        # *   tempStoragePath: Temporary storage path. This key can be used only when CategoryName is set to CommonResourceConfig.
        # *   quotaMaximumDuration: Maximum run time of DLC jobs for a quota. This key can be used only when CategoryName is set to QuotaMaximumDuration.
        # *   predefinedTags: The predefined tags of the workspace. All created resources must have tags
        self.config_key = config_key
        # The value of the configuration item.
        self.config_value = config_value
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
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
        if self.config_key is not None:
            result['ConfigKey'] = self.config_key

        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')

        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.ListConfigsResponseBodyConfigsLabels()
                self.labels.append(temp_model.from_map(k1))

        return self

class ListConfigsResponseBodyConfigsLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

