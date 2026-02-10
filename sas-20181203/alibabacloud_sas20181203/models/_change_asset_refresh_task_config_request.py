# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ChangeAssetRefreshTaskConfigRequest(DaraModel):
    def __init__(
        self,
        asset_refresh_configs: List[main_models.ChangeAssetRefreshTaskConfigRequestAssetRefreshConfigs] = None,
        region_id: str = None,
    ):
        # The asset synchronization configuration.
        self.asset_refresh_configs = asset_refresh_configs
        # The region in which your Security Center service resides.
        self.region_id = region_id

    def validate(self):
        if self.asset_refresh_configs:
            for v1 in self.asset_refresh_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssetRefreshConfigs'] = []
        if self.asset_refresh_configs is not None:
            for k1 in self.asset_refresh_configs:
                result['AssetRefreshConfigs'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asset_refresh_configs = []
        if m.get('AssetRefreshConfigs') is not None:
            for k1 in m.get('AssetRefreshConfigs'):
                temp_model = main_models.ChangeAssetRefreshTaskConfigRequestAssetRefreshConfigs()
                self.asset_refresh_configs.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ChangeAssetRefreshTaskConfigRequestAssetRefreshConfigs(DaraModel):
    def __init__(
        self,
        refresh_config_type: int = None,
        schedule_period: int = None,
        status: int = None,
        target_id: int = None,
        vendor: int = None,
    ):
        # The type of the configuration. Valid values:
        # 
        # *   **0**: server synchronization task
        # *   **1**: cloud service synchronization task
        # *   **2**: scheduled AccessKey pair verification task
        self.refresh_config_type = refresh_config_type
        # The synchronization cycle. Valid values:
        # 
        # *   **60**: 60 minutes
        # *   **180**: 3 hours
        # *   **360**: 6 hours
        # *   **720**: 12 hours
        # *   **1440**: 1 day
        # *   **10080**: 7 days
        self.schedule_period = schedule_period
        # The status of the configuration. Valid values:
        # 
        # *   **1**: enabled
        # *   **0**: disabled
        self.status = status
        # The ID of the data entry containing the AccessKey pair that you specify when you configure the scheduled AccessKey pair verification task.
        self.target_id = target_id
        # The service provider of the cloud asset. Valid values:
        # 
        # *   **3**: Tencent Cloud
        # *   **4**: Huawei Cloud
        # *   **7**: Amazon Web Services (AWS) Cloud
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.refresh_config_type is not None:
            result['RefreshConfigType'] = self.refresh_config_type

        if self.schedule_period is not None:
            result['SchedulePeriod'] = self.schedule_period

        if self.status is not None:
            result['Status'] = self.status

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefreshConfigType') is not None:
            self.refresh_config_type = m.get('RefreshConfigType')

        if m.get('SchedulePeriod') is not None:
            self.schedule_period = m.get('SchedulePeriod')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

