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
        # The language in which messages are received. Valid values:
        # 
        # - **zh**: Chinese. This is the default value.
        # - **en**: English.
        self.lang = lang
        # The query conditions for the download task. This parameter is required. If you do not specify this parameter, the API returns error code -340408 (download task TaskData invalid).
        self.task_data = task_data
        # The task type. For valid values, refer to the API operation that queries file download task types.
        self.task_type = task_type
        # The time zone of the time information in the downloaded file, specified by using an IANA time zone identity. The default value is UTC+8, which is Asia/Shanghai.
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

