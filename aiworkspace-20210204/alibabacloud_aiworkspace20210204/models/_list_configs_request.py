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
        options: str = None,
        verbose: str = None,
    ):
        # The categorization of the configuration item. Valid values:
        # - CommonResourceConfig: general resource configuration
        # - DLCAutoRecycle: automatic DLC revoke
        # - DLCPriorityConfig: DLC priority settings
        # - DSWPriorityConfig: DSW priority settings
        # - QuotaMaximumDuration: maximum runtime configuration of DLC nodes for a quota
        # - CommonTagConfig: label settings
        self.category_name = category_name
        # The keys of the configuration items. Valid values:
        # - tempStoragePath: Temporary storage path. This key is allowed only when CategoryName is set to CommonResourceConfig.
        # - isAutoRecycle: Automatic revoke configuration. This key is allowed only when CategoryName is set to DLCAutoRecycle.
        # - priorityConfig: Priority configuration. This key is allowed only when CategoryName is set to DLCPriorityConfig or DSWPriorityConfig.
        # - quotaMaximumDuration: Maximum runtime configuration of DLC nodes for a quota. This key is allowed only when CategoryName is set to QuotaMaximumDuration.
        # - predefinedTags: Preset labels for the workspace. Resources created must have these labels.
        self.config_keys = config_keys
        # The labels used as filter conditions. Separate multiple conditions with commas. These conditions are combined by using the AND operator.
        self.labels = labels
        # The additional options. Currently, only ThrowExceptionOnError is supported, which indicates that an error is thrown when an exception occurs.
        self.options = options
        # Specifies whether to display label information. Valid values:
        # - true: Displays label information.
        # - false: Does not display label information.
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

        if self.options is not None:
            result['Options'] = self.options

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

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')

        return self

