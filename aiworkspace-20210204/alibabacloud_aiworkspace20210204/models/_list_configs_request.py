# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListConfigsRequest(DaraModel):
    def __init__(
        self,
        category_name: str = None,
        config_keys: str = None,
        labels: str = None,
        verbose: str = None,
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
        # *   priorityConfig: Priority configuration. This key can be used only when CategoryName is set to DLCPriorityConfig or DSWPriorityConfig.
        # *   quotaMaximumDuration: Maximum run time of DLC jobs for a quota. This key can be used only when CategoryName is set to QuotaMaximumDuration.
        # *   predefinedTags: The predefined tags of the workspace. All created resources must have tags
        self.config_keys = config_keys
        # The tags used as filter conditions. Separate multiple tags with commas (,). These conditions are in an AND relationship.
        self.labels = labels
        # Specifies whether to show the tag information.
        # 
        # *   true
        # *   false
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.config_keys is not None:
            result['ConfigKeys'] = self.config_keys

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.verbose is not None:
            result['Verbose'] = self.verbose

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('ConfigKeys') is not None:
            self.config_keys = m.get('ConfigKeys')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')

        return self

