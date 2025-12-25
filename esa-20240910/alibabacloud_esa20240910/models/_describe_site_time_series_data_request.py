# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class DescribeSiteTimeSeriesDataRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        fields: List[main_models.DescribeSiteTimeSeriesDataRequestFields] = None,
        interval: str = None,
        site_id: str = None,
        start_time: str = None,
    ):
        # The end time for obtaining data.
        # 
        # The date format follows ISO8601 notation and uses UTC+0 time, in the format yyyy-MM-ddTHH:mm:ssZ.
        # 
        # > The end time must be later than the start time.
        self.end_time = end_time
        # Query metrics.
        # 
        # This parameter is required.
        self.fields = fields
        # The time granularity for querying data, in seconds.
        # 
        # Depending on the maximum time span of a single query, this parameter supports values of 60 (1 minute), 300 (5 minutes), 3600 (1 hour), and 86400 (1 day). For details, see the **Supported Query Time Granularities**.
        self.interval = interval
        # Site ID. Obtain the site ID by calling the [ListSites](~~ListSites~~) interface.
        # 
        # If this parameter is empty, user-level data will be queried.
        self.site_id = site_id
        # The start time for obtaining data.
        # 
        # The date format follows ISO8601 notation and uses UTC+0 time, in the format yyyy-MM-ddTHH:mm:ssZ.
        self.start_time = start_time

    def validate(self):
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.DescribeSiteTimeSeriesDataRequestFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeSiteTimeSeriesDataRequestFields(DaraModel):
    def __init__(
        self,
        dimension: List[str] = None,
        field_name: str = None,
    ):
        # Query dimension.
        self.dimension = dimension
        # Query metric value.
        # 
        # > For specific dimensions, see [Data Analysis Field Description](https://help.aliyun.com/document_detail/2878520.html).
        self.field_name = field_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        return self

