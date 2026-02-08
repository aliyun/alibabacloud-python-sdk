# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AppMaterialTask(DaraModel):
    def __init__(
        self,
        complete_time: str = None,
        complete_time_format: str = None,
        fail_reason: str = None,
        final_file_urls: List[str] = None,
        status: str = None,
        sub_status: str = None,
        submit_time: str = None,
        task_id: str = None,
        task_param: str = None,
        task_type: str = None,
    ):
        self.complete_time = complete_time
        self.complete_time_format = complete_time_format
        self.fail_reason = fail_reason
        self.final_file_urls = final_file_urls
        self.status = status
        self.sub_status = sub_status
        self.submit_time = submit_time
        self.task_id = task_id
        self.task_param = task_param
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.complete_time_format is not None:
            result['CompleteTimeFormat'] = self.complete_time_format

        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason

        if self.final_file_urls is not None:
            result['FinalFileUrls'] = self.final_file_urls

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status

        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_param is not None:
            result['TaskParam'] = self.task_param

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CompleteTimeFormat') is not None:
            self.complete_time_format = m.get('CompleteTimeFormat')

        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')

        if m.get('FinalFileUrls') is not None:
            self.final_file_urls = m.get('FinalFileUrls')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')

        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskParam') is not None:
            self.task_param = m.get('TaskParam')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

