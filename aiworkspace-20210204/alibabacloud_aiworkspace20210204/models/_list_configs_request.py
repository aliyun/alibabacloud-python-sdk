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
        # The category of the configuration item. The following categories are supported:
        # 
        # - CommonResourceConfig: The common resource configuration.
        # 
        # - DLCAutoRecycle: The automatic recycling configuration for DLC.
        # 
        # - DLCPriorityConfig: The priority configuration for DLC.
        # 
        # - DSWPriorityConfig: The priority configuration for DSW.
        # 
        # - QuotaMaximumDuration: The configuration for the maximum runtime of a DLC task in a quota.
        # 
        # - CommonTagConfig: The label configuration.
        self.category_name = category_name
        # The key of the configuration item. The following keys are supported:
        # 
        # - tempStoragePath: The path for temporary storage. This key is valid only when CategoryName is set to CommonResourceConfig.
        # 
        # - isAutoRecycle: The automatic recycling configuration. This key is valid only when CategoryName is set to DLCAutoRecycle.
        # 
        # - priorityConfig: The priority configuration. This key is valid only when CategoryName is set to DLCPriorityConfig or DSWPriorityConfig.
        # 
        # - quotaMaximumDuration: The configuration for the maximum runtime of a DLC task in a quota. This key is valid only when CategoryName is set to QuotaMaximumDuration.
        # 
        # - predefinedTags: The predefined labels for the workspace. Resources that you create must have these labels.
        self.config_keys = config_keys
        # The labels to use as filter conditions. Separate multiple labels with commas. A logical AND operation is performed on these labels.
        self.labels = labels
        # Specifies whether to return label information.
        # 
        # - true: Returns label information.
        # 
        # - false: Does not return label information.
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

