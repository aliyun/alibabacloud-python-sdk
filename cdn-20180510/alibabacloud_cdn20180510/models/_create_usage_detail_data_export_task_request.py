# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUsageDetailDataExportTaskRequest(DaraModel):
    def __init__(
        self,
        domain_names: str = None,
        end_time: str = None,
        group: str = None,
        language: str = None,
        start_time: str = None,
        task_name: str = None,
        type: str = None,
    ):
        # The domain names. If you do not specify the Group parameter, resource usage details of these domain names are exported.
        # 
        # If you do not specify this parameter, resource usage details are exported based on accounts.
        self.domain_names = domain_names
        # The end of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > The end time must be later than the start time.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The domain name group. If you specify this parameter, the **DomainNames** parameter is ignored.
        self.group = group
        # The language in which you want to export the file. Valid values:
        # 
        # *   **zh-cn**: Chinese. This is the default value.
        # *   **en-us**: English
        self.language = language
        # The beginning of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The name of the task.
        self.task_name = task_name
        # The type of resource usage data to query. Valid values:
        # 
        # *   **flow**: traffic and bandwidth
        # *   **vas**: requests
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.group is not None:
            result['Group'] = self.group

        if self.language is not None:
            result['Language'] = self.language

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

