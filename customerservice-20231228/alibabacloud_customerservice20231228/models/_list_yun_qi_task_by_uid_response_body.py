# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_customerservice20231228 import models as main_models
from darabonba.model import DaraModel

class ListYunQiTaskByUidResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListYunQiTaskByUidResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListYunQiTaskByUidResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListYunQiTaskByUidResponseBodyData(DaraModel):
    def __init__(
        self,
        extend: Any = None,
        list: List[main_models.ListYunQiTaskByUidResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.extend = extend
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extend is not None:
            result['extend'] = self.extend

        result['list'] = []
        if self.list is not None:
            for k1 in self.list:
                result['list'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['pageNum'] = self.page_num

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extend') is not None:
            self.extend = m.get('extend')

        self.list = []
        if m.get('list') is not None:
            for k1 in m.get('list'):
                temp_model = main_models.ListYunQiTaskByUidResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListYunQiTaskByUidResponseBodyDataList(DaraModel):
    def __init__(
        self,
        chat_id: str = None,
        create_time: int = None,
        creator_name: str = None,
        end_time: int = None,
        evaluation_star: int = None,
        important: str = None,
        main_ding_department_id: str = None,
        main_ding_group_id: str = None,
        main_ding_group_name: str = None,
        product_name: str = None,
        record_id: str = None,
        status: str = None,
        sub_ding_department_id: str = None,
        sub_ding_group_id: str = None,
        sub_ding_group_name: str = None,
        title: str = None,
    ):
        self.chat_id = chat_id
        self.create_time = create_time
        self.creator_name = creator_name
        self.end_time = end_time
        self.evaluation_star = evaluation_star
        self.important = important
        self.main_ding_department_id = main_ding_department_id
        self.main_ding_group_id = main_ding_group_id
        self.main_ding_group_name = main_ding_group_name
        self.product_name = product_name
        self.record_id = record_id
        self.status = status
        self.sub_ding_department_id = sub_ding_department_id
        self.sub_ding_group_id = sub_ding_group_id
        self.sub_ding_group_name = sub_ding_group_name
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_id is not None:
            result['chatId'] = self.chat_id

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.creator_name is not None:
            result['creatorName'] = self.creator_name

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.evaluation_star is not None:
            result['evaluationStar'] = self.evaluation_star

        if self.important is not None:
            result['important'] = self.important

        if self.main_ding_department_id is not None:
            result['mainDingDepartmentId'] = self.main_ding_department_id

        if self.main_ding_group_id is not None:
            result['mainDingGroupId'] = self.main_ding_group_id

        if self.main_ding_group_name is not None:
            result['mainDingGroupName'] = self.main_ding_group_name

        if self.product_name is not None:
            result['productName'] = self.product_name

        if self.record_id is not None:
            result['recordId'] = self.record_id

        if self.status is not None:
            result['status'] = self.status

        if self.sub_ding_department_id is not None:
            result['subDingDepartmentId'] = self.sub_ding_department_id

        if self.sub_ding_group_id is not None:
            result['subDingGroupId'] = self.sub_ding_group_id

        if self.sub_ding_group_name is not None:
            result['subDingGroupName'] = self.sub_ding_group_name

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('evaluationStar') is not None:
            self.evaluation_star = m.get('evaluationStar')

        if m.get('important') is not None:
            self.important = m.get('important')

        if m.get('mainDingDepartmentId') is not None:
            self.main_ding_department_id = m.get('mainDingDepartmentId')

        if m.get('mainDingGroupId') is not None:
            self.main_ding_group_id = m.get('mainDingGroupId')

        if m.get('mainDingGroupName') is not None:
            self.main_ding_group_name = m.get('mainDingGroupName')

        if m.get('productName') is not None:
            self.product_name = m.get('productName')

        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('subDingDepartmentId') is not None:
            self.sub_ding_department_id = m.get('subDingDepartmentId')

        if m.get('subDingGroupId') is not None:
            self.sub_ding_group_id = m.get('subDingGroupId')

        if m.get('subDingGroupName') is not None:
            self.sub_ding_group_name = m.get('subDingGroupName')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

