# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryTaskDetailHistoryResponseBody(DaraModel):
    def __init__(
        self,
        current_page_cursor: main_models.QueryTaskDetailHistoryResponseBodyCurrentPageCursor = None,
        next_page_cursor: main_models.QueryTaskDetailHistoryResponseBodyNextPageCursor = None,
        objects: List[main_models.QueryTaskDetailHistoryResponseBodyObjects] = None,
        page_size: int = None,
        pre_page_cursor: main_models.QueryTaskDetailHistoryResponseBodyPrePageCursor = None,
        request_id: str = None,
    ):
        self.current_page_cursor = current_page_cursor
        self.next_page_cursor = next_page_cursor
        self.objects = objects
        self.page_size = page_size
        self.pre_page_cursor = pre_page_cursor
        self.request_id = request_id

    def validate(self):
        if self.current_page_cursor:
            self.current_page_cursor.validate()
        if self.next_page_cursor:
            self.next_page_cursor.validate()
        if self.objects:
            for v1 in self.objects:
                 if v1:
                    v1.validate()
        if self.pre_page_cursor:
            self.pre_page_cursor.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page_cursor is not None:
            result['CurrentPageCursor'] = self.current_page_cursor.to_map()

        if self.next_page_cursor is not None:
            result['NextPageCursor'] = self.next_page_cursor.to_map()

        result['Objects'] = []
        if self.objects is not None:
            for k1 in self.objects:
                result['Objects'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pre_page_cursor is not None:
            result['PrePageCursor'] = self.pre_page_cursor.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageCursor') is not None:
            temp_model = main_models.QueryTaskDetailHistoryResponseBodyCurrentPageCursor()
            self.current_page_cursor = temp_model.from_map(m.get('CurrentPageCursor'))

        if m.get('NextPageCursor') is not None:
            temp_model = main_models.QueryTaskDetailHistoryResponseBodyNextPageCursor()
            self.next_page_cursor = temp_model.from_map(m.get('NextPageCursor'))

        self.objects = []
        if m.get('Objects') is not None:
            for k1 in m.get('Objects'):
                temp_model = main_models.QueryTaskDetailHistoryResponseBodyObjects()
                self.objects.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrePageCursor') is not None:
            temp_model = main_models.QueryTaskDetailHistoryResponseBodyPrePageCursor()
            self.pre_page_cursor = temp_model.from_map(m.get('PrePageCursor'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryTaskDetailHistoryResponseBodyPrePageCursor(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        domain_name: str = None,
        error_msg: str = None,
        instance_id: str = None,
        task_detail_no: str = None,
        task_no: str = None,
        task_status: str = None,
        task_status_code: int = None,
        task_type: str = None,
        task_type_description: str = None,
        try_count: int = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.domain_name = domain_name
        self.error_msg = error_msg
        self.instance_id = instance_id
        self.task_detail_no = task_detail_no
        self.task_no = task_no
        self.task_status = task_status
        self.task_status_code = task_status_code
        self.task_type = task_type
        self.task_type_description = task_type_description
        self.try_count = try_count
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.task_detail_no is not None:
            result['TaskDetailNo'] = self.task_detail_no

        if self.task_no is not None:
            result['TaskNo'] = self.task_no

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description

        if self.try_count is not None:
            result['TryCount'] = self.try_count

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TaskDetailNo') is not None:
            self.task_detail_no = m.get('TaskDetailNo')

        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')

        if m.get('TryCount') is not None:
            self.try_count = m.get('TryCount')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class QueryTaskDetailHistoryResponseBodyObjects(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        domain_name: str = None,
        error_msg: str = None,
        instance_id: str = None,
        task_detail_no: str = None,
        task_no: str = None,
        task_status: str = None,
        task_status_code: int = None,
        task_type: str = None,
        task_type_description: str = None,
        try_count: int = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.domain_name = domain_name
        self.error_msg = error_msg
        self.instance_id = instance_id
        self.task_detail_no = task_detail_no
        self.task_no = task_no
        self.task_status = task_status
        self.task_status_code = task_status_code
        self.task_type = task_type
        self.task_type_description = task_type_description
        self.try_count = try_count
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.task_detail_no is not None:
            result['TaskDetailNo'] = self.task_detail_no

        if self.task_no is not None:
            result['TaskNo'] = self.task_no

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description

        if self.try_count is not None:
            result['TryCount'] = self.try_count

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TaskDetailNo') is not None:
            self.task_detail_no = m.get('TaskDetailNo')

        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')

        if m.get('TryCount') is not None:
            self.try_count = m.get('TryCount')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class QueryTaskDetailHistoryResponseBodyNextPageCursor(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        domain_name: str = None,
        error_msg: str = None,
        instance_id: str = None,
        task_detail_no: str = None,
        task_no: str = None,
        task_status: str = None,
        task_status_code: int = None,
        task_type: str = None,
        task_type_description: str = None,
        try_count: int = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.domain_name = domain_name
        self.error_msg = error_msg
        self.instance_id = instance_id
        self.task_detail_no = task_detail_no
        self.task_no = task_no
        self.task_status = task_status
        self.task_status_code = task_status_code
        self.task_type = task_type
        self.task_type_description = task_type_description
        self.try_count = try_count
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.task_detail_no is not None:
            result['TaskDetailNo'] = self.task_detail_no

        if self.task_no is not None:
            result['TaskNo'] = self.task_no

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description

        if self.try_count is not None:
            result['TryCount'] = self.try_count

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TaskDetailNo') is not None:
            self.task_detail_no = m.get('TaskDetailNo')

        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')

        if m.get('TryCount') is not None:
            self.try_count = m.get('TryCount')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class QueryTaskDetailHistoryResponseBodyCurrentPageCursor(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        domain_name: str = None,
        error_msg: str = None,
        instance_id: str = None,
        task_detail_no: str = None,
        task_no: str = None,
        task_status: str = None,
        task_status_code: int = None,
        task_type: str = None,
        task_type_description: str = None,
        try_count: int = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.domain_name = domain_name
        self.error_msg = error_msg
        self.instance_id = instance_id
        self.task_detail_no = task_detail_no
        self.task_no = task_no
        self.task_status = task_status
        self.task_status_code = task_status_code
        self.task_type = task_type
        self.task_type_description = task_type_description
        self.try_count = try_count
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.task_detail_no is not None:
            result['TaskDetailNo'] = self.task_detail_no

        if self.task_no is not None:
            result['TaskNo'] = self.task_no

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description

        if self.try_count is not None:
            result['TryCount'] = self.try_count

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TaskDetailNo') is not None:
            self.task_detail_no = m.get('TaskDetailNo')

        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')

        if m.get('TryCount') is not None:
            self.try_count = m.get('TryCount')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

