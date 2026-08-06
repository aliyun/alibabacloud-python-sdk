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
        # - CommonResourceConfig: common resource configuration.
        # - DLCAutoRecycle: DLC automatic recycling.
        # - DLCPriorityConfig: DLC priority settings.
        # - DSWPriorityConfig: DSW priority settings.
        # - QuotaMaximumDuration: maximum runtime duration configuration for DLC jobs in a quota.
        # - CommonTagConfig: tag settings.
        self.category_name = category_name
        # The keys of the configuration items. The following keys are supported:
        # 
        # - tempStoragePath: the temporary storage path. This ConfigKey can be used only when CategoryName is set to CommonResourceConfig.
        # - isAutoRecycle: the automatic recycling configuration. This ConfigKey can be used only when CategoryName is set to DLCAutoRecycle.
        # - priorityConfig: the priority configuration. This ConfigKey can be used only when CategoryName is set to DLCPriorityConfig or DSWPriorityConfig.
        # - quotaMaximumDuration: the maximum runtime duration configuration for DLC jobs in a quota. This ConfigKey can be used only when CategoryName is set to QuotaMaximumDuration.
        # - predefinedTags: the preset tags for the workspace. Resources that are created must include these tags.
        self.config_keys = config_keys
        # The labels used as filter conditions. Separate multiple conditions with commas. These conditions are evaluated using a logical AND.
        self.labels = labels
        # Specifies whether to display label information. Valid values:
        # 
        # - true: Display label information.
        # - false: Do not display label information.
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

