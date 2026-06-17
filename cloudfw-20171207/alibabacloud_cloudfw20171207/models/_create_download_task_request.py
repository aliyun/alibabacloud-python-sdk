# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDownloadTaskRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        task_data: str = None,
        task_type: str = None,
        time_zone: str = None,
    ):
        # The language of the response message.
        # 
        # Valid values:
        # 
        # - **zh**: Chinese (default)
        # 
        # - **en**: English
        self.lang = lang
        # The query conditions for the download task.
        self.task_data = task_data
        # The type of the task. For a list of valid values, see the API for querying file download task types.
        self.task_type = task_type
        # The time zone of the time information in the downloaded file. The value is an IANA time zone identifier. The default value is Asia/Shanghai, which corresponds to UTC+8.
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.task_data is not None:
            result['TaskData'] = self.task_data

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('TaskData') is not None:
            self.task_data = m.get('TaskData')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

