# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListOfflineTaskRequest(DaraModel):
    def __init__(
        self,
        labels: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        task_name: str = None,
        task_status: List[str] = None,
    ):
        # The list of task labels.
        self.labels = labels
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id
        # The task name.
        self.task_name = task_name
        # The task status.
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.labels is not None:
            result['labels'] = self.labels

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.task_name is not None:
            result['taskName'] = self.task_name

        if self.task_status is not None:
            result['taskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')

        return self

