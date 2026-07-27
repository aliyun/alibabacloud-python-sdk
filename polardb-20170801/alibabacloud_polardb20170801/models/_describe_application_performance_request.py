# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApplicationPerformanceRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        consumer: str = None,
        consumer_group: str = None,
        downsample: str = None,
        end_step: int = None,
        end_time: str = None,
        interval: str = None,
        key: str = None,
        max_points: int = None,
        model_service: str = None,
        start_step: int = None,
        start_time: str = None,
    ):
        # The application cluster ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The user.
        self.consumer = consumer
        # The user group.
        self.consumer_group = consumer_group
        # The downsampling policy.
        self.downsample = downsample
        # The end step number.
        self.end_step = end_step
        # The end of the time range to query. Specify the time in the yyyy-MM-ddTHH:mmZ format (UTC).
        # 
        # This parameter is required.
        self.end_time = end_time
        # The data granularity of performance data. Valid values:
        # - 5
        # - 30
        # - 60
        # - 600
        # - 1800
        # - 3600
        # - 86400
        self.interval = interval
        # The performance metrics to query. Separate multiple values with commas (,).
        # 
        # > **Note** You can specify up to 5 performance metrics.
        # 
        # This parameter is required.
        self.key = key
        # The maximum number of data points to return.
        self.max_points = max_points
        # The model service.
        self.model_service = model_service
        # The start step number.
        self.start_step = start_step
        # The beginning of the time range to query. Specify the time in the yyyy-MM-ddTHH:mmZ format (UTC).
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.consumer is not None:
            result['Consumer'] = self.consumer

        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group

        if self.downsample is not None:
            result['Downsample'] = self.downsample

        if self.end_step is not None:
            result['EndStep'] = self.end_step

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.key is not None:
            result['Key'] = self.key

        if self.max_points is not None:
            result['MaxPoints'] = self.max_points

        if self.model_service is not None:
            result['ModelService'] = self.model_service

        if self.start_step is not None:
            result['StartStep'] = self.start_step

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Consumer') is not None:
            self.consumer = m.get('Consumer')

        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')

        if m.get('Downsample') is not None:
            self.downsample = m.get('Downsample')

        if m.get('EndStep') is not None:
            self.end_step = m.get('EndStep')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('MaxPoints') is not None:
            self.max_points = m.get('MaxPoints')

        if m.get('ModelService') is not None:
            self.model_service = m.get('ModelService')

        if m.get('StartStep') is not None:
            self.start_step = m.get('StartStep')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

