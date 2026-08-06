# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class GetConfigResponseBody(DaraModel):
    def __init__(
        self,
        category_name: str = None,
        config_key: str = None,
        config_value: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        labels: List[main_models.GetConfigResponseBodyLabels] = None,
        request_id: str = None,
        workspace_id: str = None,
    ):
        # The category of the configuration item. The following categories are supported:
        # 
        # - CommonResourceConfig: common resource configuration
        # - DLCAutoRecycle: DLC automatic reclamation
        # - DLCPriorityConfig: DLC priority settings
        # - DSWPriorityConfig: DSW priority settings
        # - QuotaMaximumDuration: maximum runtime duration configuration for DLC jobs in a quota
        # - CommonTagConfig: tag settings
        self.category_name = category_name
        # The key of the configuration item. The following keys are supported:
        # 
        # - tempStoragePath: the temporary storage path. This key is valid only when CategoryName is set to CommonResourceConfig.
        # - isAutoRecycle: the automatic reclamation configuration. This key is valid only when CategoryName is set to DLCAutoRecycle.
        # - priorityConfig: the priority configuration. This key is valid only when CategoryName is set to DLCPriorityConfig or DSWPriorityConfig.
        # - quotaMaximumDuration: the maximum runtime duration configuration for DLC jobs in a quota. This key is valid only when CategoryName is set to QuotaMaximumDuration.
        # - predefinedTags: the preset tags for the workspace. Resources created in the workspace must include these tags.
        self.config_key = config_key
        # The value of the configuration item.
        self.config_value = config_value
        # The time when the configuration item was created, in UTC.
        self.gmt_create_time = gmt_create_time
        # The time when the configuration item was last modified, in UTC.
        self.gmt_modified_time = gmt_modified_time
        # The list of labels for the configuration item.
        self.labels = labels
        # The request ID.
        self.request_id = request_id
        # The workspace ID.
        self.workspace_id = workspace_id

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

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

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
                temp_model = main_models.GetConfigResponseBodyLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class GetConfigResponseBodyLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the label.
        self.key = key
        # The value of the label.
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

