# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServiceMetricsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        env: str = None,
        group_id: int = None,
        interval_in_sec: int = None,
        ip: str = None,
        measures: str = None,
        service_group_id: int = None,
        start_time: str = None,
        topic_id: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.env = env
        self.group_id = group_id
        # This parameter is required.
        self.interval_in_sec = interval_in_sec
        self.ip = ip
        self.measures = measures
        self.service_group_id = service_group_id
        # This parameter is required.
        self.start_time = start_time
        self.topic_id = topic_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.env is not None:
            result['env'] = self.env

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.interval_in_sec is not None:
            result['intervalInSec'] = self.interval_in_sec

        if self.ip is not None:
            result['ip'] = self.ip

        if self.measures is not None:
            result['measures'] = self.measures

        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.topic_id is not None:
            result['topicId'] = self.topic_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('intervalInSec') is not None:
            self.interval_in_sec = m.get('intervalInSec')

        if m.get('ip') is not None:
            self.ip = m.get('ip')

        if m.get('measures') is not None:
            self.measures = m.get('measures')

        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('topicId') is not None:
            self.topic_id = m.get('topicId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

