# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAlarmEventRequest(DaraModel):
    def __init__(
        self,
        alarm_channel: str = None,
        alarm_status: str = None,
        alarm_type: str = None,
        app_name: str = None,
        cluster_id: str = None,
        end_time: int = None,
        job_name: str = None,
        page_num: str = None,
        page_size: str = None,
        reverse: bool = None,
        start_time: int = None,
    ):
        self.alarm_channel = alarm_channel
        self.alarm_status = alarm_status
        self.alarm_type = alarm_type
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.end_time = end_time
        self.job_name = job_name
        self.page_num = page_num
        self.page_size = page_size
        self.reverse = reverse
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_channel is not None:
            result['AlarmChannel'] = self.alarm_channel

        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status

        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.reverse is not None:
            result['Reverse'] = self.reverse

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmChannel') is not None:
            self.alarm_channel = m.get('AlarmChannel')

        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')

        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

