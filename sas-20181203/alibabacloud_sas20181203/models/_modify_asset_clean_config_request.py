# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ModifyAssetCleanConfigRequest(DaraModel):
    def __init__(
        self,
        asset_clean_configs: List[main_models.ModifyAssetCleanConfigRequestAssetCleanConfigs] = None,
    ):
        # The list of asset cleanup configurations.
        self.asset_clean_configs = asset_clean_configs

    def validate(self):
        if self.asset_clean_configs:
            for v1 in self.asset_clean_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssetCleanConfigs'] = []
        if self.asset_clean_configs is not None:
            for k1 in self.asset_clean_configs:
                result['AssetCleanConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asset_clean_configs = []
        if m.get('AssetCleanConfigs') is not None:
            for k1 in m.get('AssetCleanConfigs'):
                temp_model = main_models.ModifyAssetCleanConfigRequestAssetCleanConfigs()
                self.asset_clean_configs.append(temp_model.from_map(k1))

        return self

class ModifyAssetCleanConfigRequestAssetCleanConfigs(DaraModel):
    def __init__(
        self,
        clean_days: int = None,
        status: int = None,
        type: int = None,
    ):
        # The number of offline days after which non-Alibaba Cloud hosts are automatically cleaned up. Valid values: integers from 1 to 30.
        self.clean_days = clean_days
        # Specifies whether to enable automatic cleanup of offline non-Alibaba Cloud hosts. Valid values:
        # 
        # - **0**: Disabled.
        # - **1**: Enabled.
        self.status = status
        # The type of host to clean up. Valid values:
        # 
        # - **1**: non-Alibaba Cloud host.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clean_days is not None:
            result['CleanDays'] = self.clean_days

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CleanDays') is not None:
            self.clean_days = m.get('CleanDays')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

