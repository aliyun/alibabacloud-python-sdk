# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeGroupPageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        current_page: int = None,
        page_size: int = None,
        result_object: List[main_models.DescribeGroupPageResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Current page number.
        self.current_page = current_page
        # Page size, with a default value of 10.
        self.page_size = page_size
        # Returned object.
        self.result_object = result_object
        # Total number of items.
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
                temp_model = main_models.DescribeGroupPageResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeGroupPageResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        community_no: str = None,
        create_time: int = None,
        group_risk: str = None,
        group_scale: str = None,
        id: int = None,
        scene_name: str = None,
        task_id: int = None,
        user_id: str = None,
    ):
        # Community number.
        self.community_no = community_no
        # Creation time.
        self.create_time = create_time
        # Group risk concentration.
        self.group_risk = group_risk
        # Group scale.
        self.group_scale = group_scale
        # Primary key ID.
        self.id = id
        # Scene name.
        self.scene_name = scene_name
        # Task ID.
        self.task_id = task_id
        # User UID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.community_no is not None:
            result['communityNo'] = self.community_no

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.group_risk is not None:
            result['groupRisk'] = self.group_risk

        if self.group_scale is not None:
            result['groupScale'] = self.group_scale

        if self.id is not None:
            result['id'] = self.id

        if self.scene_name is not None:
            result['sceneName'] = self.scene_name

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('communityNo') is not None:
            self.community_no = m.get('communityNo')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('groupRisk') is not None:
            self.group_risk = m.get('groupRisk')

        if m.get('groupScale') is not None:
            self.group_scale = m.get('groupScale')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('sceneName') is not None:
            self.scene_name = m.get('sceneName')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

