# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetStandardStatisticsRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        statistics_query: main_models.GetStandardStatisticsRequestStatisticsQuery = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.statistics_query = statistics_query

    def validate(self):
        if self.statistics_query:
            self.statistics_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.statistics_query is not None:
            result['StatisticsQuery'] = self.statistics_query.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('StatisticsQuery') is not None:
            temp_model = main_models.GetStandardStatisticsRequestStatisticsQuery()
            self.statistics_query = temp_model.from_map(m.get('StatisticsQuery'))

        return self

class GetStandardStatisticsRequestStatisticsQuery(DaraModel):
    def __init__(
        self,
        create_time_period: main_models.GetStandardStatisticsRequestStatisticsQueryCreateTimePeriod = None,
        directory: str = None,
        standard_stage_list: List[str] = None,
    ):
        self.create_time_period = create_time_period
        # This parameter is required.
        self.directory = directory
        self.standard_stage_list = standard_stage_list

    def validate(self):
        if self.create_time_period:
            self.create_time_period.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time_period is not None:
            result['CreateTimePeriod'] = self.create_time_period.to_map()

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.standard_stage_list is not None:
            result['StandardStageList'] = self.standard_stage_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimePeriod') is not None:
            temp_model = main_models.GetStandardStatisticsRequestStatisticsQueryCreateTimePeriod()
            self.create_time_period = temp_model.from_map(m.get('CreateTimePeriod'))

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('StandardStageList') is not None:
            self.standard_stage_list = m.get('StandardStageList')

        return self

class GetStandardStatisticsRequestStatisticsQueryCreateTimePeriod(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        include_end_time: bool = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.include_end_time = include_end_time
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

        if self.include_end_time is not None:
            result['IncludeEndTime'] = self.include_end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IncludeEndTime') is not None:
            self.include_end_time = m.get('IncludeEndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

