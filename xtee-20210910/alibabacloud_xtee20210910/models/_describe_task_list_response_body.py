# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeTaskListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        current_page: int = None,
        page_size: int = None,
        result_object: List[main_models.DescribeTaskListResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Current page number.
        self.current_page = current_page
        # Page size, with a default value of 10
        self.page_size = page_size
        # Returned object
        self.result_object = result_object
        # Total number of items
        self.total_item = total_item
        # Total number of pages
        self.total_page = total_page

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        if self.total_item is not None:
            result['totalItem'] = self.total_item

        if self.total_page is not None:
            result['totalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeTaskListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeTaskListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        completion_time: int = None,
        create_time: int = None,
        id: int = None,
        mark: int = None,
        remark: str = None,
        scene_name: str = None,
        status: str = None,
        task_log_id: int = None,
        task_type: str = None,
    ):
        # Completion time, in milliseconds.
        self.completion_time = completion_time
        # Creation time.
        self.create_time = create_time
        # Task ID.
        self.id = id
        # Total number of mark information.
        self.mark = mark
        # Remark.
        self.remark = remark
        # Scene name
        self.scene_name = scene_name
        # Data status.
        # 
        # -1: Failed
        # 0: Deleted
        # 1: Pending
        # 2: Success
        self.status = status
        # Task ID.
        self.task_log_id = task_log_id
        # Task type
        # 1: Data upload
        # 2: Supplemental upload
        # 3: Labeling
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completion_time is not None:
            result['completionTime'] = self.completion_time

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.id is not None:
            result['id'] = self.id

        if self.mark is not None:
            result['mark'] = self.mark

        if self.remark is not None:
            result['remark'] = self.remark

        if self.scene_name is not None:
            result['sceneName'] = self.scene_name

        if self.status is not None:
            result['status'] = self.status

        if self.task_log_id is not None:
            result['taskLogId'] = self.task_log_id

        if self.task_type is not None:
            result['taskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completionTime') is not None:
            self.completion_time = m.get('completionTime')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('mark') is not None:
            self.mark = m.get('mark')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('sceneName') is not None:
            self.scene_name = m.get('sceneName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskLogId') is not None:
            self.task_log_id = m.get('taskLogId')

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        return self

