# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeRecordFilesResponseBody(DaraModel):
    def __init__(
        self,
        record_files: List[main_models.DescribeRecordFilesResponseBodyRecordFiles] = None,
        request_id: str = None,
        total_num: int = None,
        total_page: int = None,
    ):
        self.record_files = record_files
        self.request_id = request_id
        self.total_num = total_num
        self.total_page = total_page

    def validate(self):
        if self.record_files:
            for v1 in self.record_files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RecordFiles'] = []
        if self.record_files is not None:
            for k1 in self.record_files:
                result['RecordFiles'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_files = []
        if m.get('RecordFiles') is not None:
            for k1 in m.get('RecordFiles'):
                temp_model = main_models.DescribeRecordFilesResponseBodyRecordFiles()
                self.record_files.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeRecordFilesResponseBodyRecordFiles(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        create_time: str = None,
        duration: float = None,
        start_time: str = None,
        stop_time: str = None,
        task_id: str = None,
        url: str = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.create_time = create_time
        self.duration = duration
        self.start_time = start_time
        self.stop_time = stop_time
        self.task_id = task_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stop_time is not None:
            result['StopTime'] = self.stop_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

