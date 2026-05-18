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
        end_time: str = None,
        interval: str = None,
        key: str = None,
        model_service: str = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        self.consumer = consumer
        self.consumer_group = consumer_group
        # This parameter is required.
        self.end_time = end_time
        self.interval = interval
        # This parameter is required.
        self.key = key
        self.model_service = model_service
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

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.key is not None:
            result['Key'] = self.key

        if self.model_service is not None:
            result['ModelService'] = self.model_service

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

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('ModelService') is not None:
            self.model_service = m.get('ModelService')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

