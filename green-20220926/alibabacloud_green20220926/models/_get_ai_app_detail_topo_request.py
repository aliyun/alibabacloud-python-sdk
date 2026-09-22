# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetAiAppDetailTopoRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        region_id: str = None,
        time_query: main_models.GetAiAppDetailTopoRequestTimeQuery = None,
    ):
        # The application ID that identifies a specific AI application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The region ID.
        self.region_id = region_id
        # The time query.
        self.time_query = time_query

    def validate(self):
        if self.time_query:
            self.time_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.time_query is not None:
            result['TimeQuery'] = self.time_query.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TimeQuery') is not None:
            temp_model = main_models.GetAiAppDetailTopoRequestTimeQuery()
            self.time_query = temp_model.from_map(m.get('TimeQuery'))

        return self

class GetAiAppDetailTopoRequestTimeQuery(DaraModel):
    def __init__(
        self,
        dimension: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The dimension.
        self.dimension = dimension
        # The end time. Format: YYYY-MM-DD HH:mm:ss.
        self.end_time = end_time
        # The start time. Format: YYYY-MM-DD HH:mm:ss.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

