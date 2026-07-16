# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConfigRequest(DaraModel):
    def __init__(
        self,
        category_name: str = None,
        config_key: str = None,
        verbose: str = None,
    ):
        # The classification of the configuration item. The following classifications are supported:
        # 
        # - CommonResourceConfig: common resource configurations
        # 
        # - DLCAutoRecycle: automatic DLC resource recycling
        # 
        # - DLCPriorityConfig: DLC priority settings
        # 
        # - DSWPriorityConfig: DSW priority settings
        # 
        # - QuotaMaximumDuration: the maximum runtime of a DLC task for a quota
        # 
        # - CommonTagConfig: tag settings
        self.category_name = category_name
        # The key of the configuration item. The following keys are supported:
        # 
        # - tempStoragePath: the temporary storage path. This key applies only when CategoryName is set to CommonResourceConfig.
        # 
        # - isAutoRecycle: the automatic recycling configuration. This key applies only when CategoryName is set to DLCAutoRecycle.
        # 
        # - priorityConfig: the priority configuration. This key applies only when CategoryName is set to DLCPriorityConfig or DSWPriorityConfig.
        # 
        # - quotaMaximumDuration: the maximum runtime of a DLC task for a quota. This key applies only when CategoryName is set to QuotaMaximumDuration.
        # 
        # - predefinedTags: the predefined tags for the workspace. Resources that you create must have tags.
        self.config_key = config_key
        # The value of the configuration item.
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

        if self.config_key is not None:
            result['ConfigKey'] = self.config_key

        if self.verbose is not None:
            result['Verbose'] = self.verbose

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')

        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')

        return self

