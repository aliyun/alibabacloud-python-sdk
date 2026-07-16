# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataBatchIngestionShrinkRequest(DaraModel):
    def __init__(
        self,
        auto_scan_new: str = None,
        data_batch_ingestion_mode: str = None,
        data_ingestion_ids_shrink: str = None,
        data_source_recognize_enabled: bool = None,
        lang: str = None,
        log_user_ids_shrink: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # Specifies whether to automatically discover new users.
        # 
        # - enabled: Enables the feature.
        # 
        # - disabled: Disables the feature.
        self.auto_scan_new = auto_scan_new
        # The mode for batch data ingestion. Valid values:
        # 
        # - full
        # 
        # - increment
        self.data_batch_ingestion_mode = data_batch_ingestion_mode
        # The list of ingestion policy IDs.
        self.data_ingestion_ids_shrink = data_ingestion_ids_shrink
        # Specifies whether to automatically discover new Logstores.
        self.data_source_recognize_enabled = data_source_recognize_enabled
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The list of user IDs for batch data ingestion.
        self.log_user_ids_shrink = log_user_ids_shrink
        # The region of the Data Management hub for threat analysis. Select a region for the management hub based on the region of your assets. Valid values:
        # 
        # - cn-hangzhou: Your assets are in the Chinese mainland.
        # 
        # - ap-southeast-1: Your assets are in a region outside China.
        self.region_id = region_id
        # The user ID of the member whose perspective the administrator wants to switch to.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_scan_new is not None:
            result['AutoScanNew'] = self.auto_scan_new

        if self.data_batch_ingestion_mode is not None:
            result['DataBatchIngestionMode'] = self.data_batch_ingestion_mode

        if self.data_ingestion_ids_shrink is not None:
            result['DataIngestionIds'] = self.data_ingestion_ids_shrink

        if self.data_source_recognize_enabled is not None:
            result['DataSourceRecognizeEnabled'] = self.data_source_recognize_enabled

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.log_user_ids_shrink is not None:
            result['LogUserIds'] = self.log_user_ids_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoScanNew') is not None:
            self.auto_scan_new = m.get('AutoScanNew')

        if m.get('DataBatchIngestionMode') is not None:
            self.data_batch_ingestion_mode = m.get('DataBatchIngestionMode')

        if m.get('DataIngestionIds') is not None:
            self.data_ingestion_ids_shrink = m.get('DataIngestionIds')

        if m.get('DataSourceRecognizeEnabled') is not None:
            self.data_source_recognize_enabled = m.get('DataSourceRecognizeEnabled')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LogUserIds') is not None:
            self.log_user_ids_shrink = m.get('LogUserIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

