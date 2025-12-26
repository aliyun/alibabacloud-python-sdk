# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListOtaTaskResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        task_list: List[main_models.ListOtaTaskResponseBodyTaskList] = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries on each page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The OTA update tasks.
        self.task_list = task_list
        # The total number of OTA update tasks.
        self.total_count = total_count

    def validate(self):
        if self.task_list:
            for v1 in self.task_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TaskList'] = []
        if self.task_list is not None:
            for k1 in self.task_list:
                result['TaskList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_list = []
        if m.get('TaskList') is not None:
            for k1 in m.get('TaskList'):
                temp_model = main_models.ListOtaTaskResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOtaTaskResponseBodyTaskList(DaraModel):
    def __init__(
        self,
        ota_version: str = None,
        task_display_status: str = None,
        task_id: str = None,
        task_start_time: str = None,
    ):
        # The OTA version.
        self.ota_version = ota_version
        # The task status.
        # 
        # Valid values:
        # 
        # *   FAILED
        # *   RUNNING
        # *   TERMINATED
        # *   PART_FINISHED
        # *   STANDBY
        # *   FINISHED
        self.task_display_status = task_display_status
        # The task ID.
        self.task_id = task_id
        # The start time of the OTA update task. The time follows the ISO 8601 standard.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.task_start_time = task_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ota_version is not None:
            result['OtaVersion'] = self.ota_version

        if self.task_display_status is not None:
            result['TaskDisplayStatus'] = self.task_display_status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_start_time is not None:
            result['TaskStartTime'] = self.task_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OtaVersion') is not None:
            self.ota_version = m.get('OtaVersion')

        if m.get('TaskDisplayStatus') is not None:
            self.task_display_status = m.get('TaskDisplayStatus')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStartTime') is not None:
            self.task_start_time = m.get('TaskStartTime')

        return self

