# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListVirusScanTaskSummaryResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tasks: List[main_models.ListVirusScanTaskSummaryResponseBodyTasks] = None,
    ):
        self.request_id = request_id
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.ListVirusScanTaskSummaryResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        return self

class ListVirusScanTaskSummaryResponseBodyTasks(DaraModel):
    def __init__(
        self,
        task_id: str = None,
        virus_file_count: int = None,
    ):
        self.task_id = task_id
        self.virus_file_count = virus_file_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.virus_file_count is not None:
            result['VirusFileCount'] = self.virus_file_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('VirusFileCount') is not None:
            self.virus_file_count = m.get('VirusFileCount')

        return self

