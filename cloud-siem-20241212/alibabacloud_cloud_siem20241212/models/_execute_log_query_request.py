# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteLogQueryRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        extend_content_packed: str = None,
        lang: str = None,
        log_project_name: str = None,
        log_query: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        log_user_id: int = None,
        normalization_schema_id: str = None,
        region_id: str = None,
        role_for: int = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.extend_content_packed = extend_content_packed
        self.lang = lang
        self.log_project_name = log_project_name
        self.log_query = log_query
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name
        self.log_user_id = log_user_id
        self.normalization_schema_id = normalization_schema_id
        self.region_id = region_id
        self.role_for = role_for
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.extend_content_packed is not None:
            result['ExtendContentPacked'] = self.extend_content_packed

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name

        if self.log_query is not None:
            result['LogQuery'] = self.log_query

        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id

        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExtendContentPacked') is not None:
            self.extend_content_packed = m.get('ExtendContentPacked')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')

        if m.get('LogQuery') is not None:
            self.log_query = m.get('LogQuery')

        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')

        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

