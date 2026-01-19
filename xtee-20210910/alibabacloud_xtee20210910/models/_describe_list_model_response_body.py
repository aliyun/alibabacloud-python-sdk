# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeListModelResponseBody(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        page_size: str = None,
        request_id: str = None,
        result_object: List[main_models.DescribeListModelResponseBodyResultObject] = None,
        total_item: str = None,
        total_page: str = None,
    ):
        # Current page number.
        self.current_page = current_page
        # Number of items per page.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Returned data.
        self.result_object = result_object
        # Total number of records.
        self.total_item = total_item
        # Total number of pages.
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['ResultObject'].append(k1.to_map() if k1 else None)

        if self.total_item is not None:
            result['TotalItem'] = self.total_item

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_object = []
        if m.get('ResultObject') is not None:
            for k1 in m.get('ResultObject'):
                temp_model = main_models.DescribeListModelResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('TotalItem') is not None:
            self.total_item = m.get('TotalItem')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeListModelResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        buc_id: str = None,
        create_time: str = None,
        model_code: str = None,
        model_id: str = None,
        model_name: str = None,
        model_scene: str = None,
        model_status: str = None,
        task_id: str = None,
        update_time: str = None,
        user_id: str = None,
        user_local_file_name: str = None,
    ):
        # Uploader ID.
        self.buc_id = buc_id
        # Creation time.
        self.create_time = create_time
        # Model code.
        self.model_code = model_code
        # Unique identifier of the model in use.
        self.model_id = model_id
        # Model name.
        self.model_name = model_name
        # Model scenario.
        self.model_scene = model_scene
        # Model status, values: -**ENABLED**: Enabled-**DISABLED**: Disabled
        self.model_status = model_status
        # Task ID.
        self.task_id = task_id
        # Last update time of the model.
        self.update_time = update_time
        # User ID.
        self.user_id = user_id
        # File name.
        self.user_local_file_name = user_local_file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buc_id is not None:
            result['bucId'] = self.buc_id

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.model_code is not None:
            result['modelCode'] = self.model_code

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.model_scene is not None:
            result['modelScene'] = self.model_scene

        if self.model_status is not None:
            result['modelStatus'] = self.model_status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.user_local_file_name is not None:
            result['userLocalFileName'] = self.user_local_file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucId') is not None:
            self.buc_id = m.get('bucId')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('modelCode') is not None:
            self.model_code = m.get('modelCode')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('modelScene') is not None:
            self.model_scene = m.get('modelScene')

        if m.get('modelStatus') is not None:
            self.model_status = m.get('modelStatus')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('userLocalFileName') is not None:
            self.user_local_file_name = m.get('userLocalFileName')

        return self

