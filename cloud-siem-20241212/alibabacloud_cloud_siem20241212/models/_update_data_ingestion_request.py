# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataIngestionRequest(DaraModel):
    def __init__(
        self,
        data_ingestion_id: str = None,
        data_ingestion_mode: str = None,
        data_source_id: str = None,
        lang: str = None,
        normalization_rule_id: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # The data ingestion ID.
        self.data_ingestion_id = data_ingestion_id
        # The data ingestion mode. Valid values:
        # 
        # - realtime
        # 
        # - scan
        self.data_ingestion_mode = data_ingestion_mode
        # The data source ID.
        self.data_source_id = data_source_id
        # The language of the response messages. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The normalization rule ID.
        self.normalization_rule_id = normalization_rule_id
        # The region of the Data Management center for threat analysis. Select the region where your assets are located. Valid values:
        # 
        # - cn-hangzhou: The assets are in the Chinese mainland.
        # 
        # - ap-southeast-1: The assets are in a region outside China.
        self.region_id = region_id
        # The user ID of a member. An administrator can perform operations on behalf of this member.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_ingestion_id is not None:
            result['DataIngestionId'] = self.data_ingestion_id

        if self.data_ingestion_mode is not None:
            result['DataIngestionMode'] = self.data_ingestion_mode

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIngestionId') is not None:
            self.data_ingestion_id = m.get('DataIngestionId')

        if m.get('DataIngestionMode') is not None:
            self.data_ingestion_mode = m.get('DataIngestionMode')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

