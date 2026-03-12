# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20160511 import models as main_models
from darabonba.model import DaraModel

class QueryBatchTaskDetailListResponseBody(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: main_models.QueryBatchTaskDetailListResponseBodyData = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.next_page is not None:
            result['NextPage'] = self.next_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pre_page is not None:
            result['PrePage'] = self.pre_page

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')

        if m.get('Data') is not None:
            temp_model = main_models.QueryBatchTaskDetailListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class QueryBatchTaskDetailListResponseBodyData(DaraModel):
    def __init__(
        self,
        task_detail: List[main_models.QueryBatchTaskDetailListResponseBodyDataTaskDetail] = None,
    ):
        self.task_detail = task_detail

    def validate(self):
        if self.task_detail:
            for v1 in self.task_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TaskDetail'] = []
        if self.task_detail is not None:
            for k1 in self.task_detail:
                result['TaskDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_detail = []
        if m.get('TaskDetail') is not None:
            for k1 in m.get('TaskDetail'):
                temp_model = main_models.QueryBatchTaskDetailListResponseBodyDataTaskDetail()
                self.task_detail.append(temp_model.from_map(k1))

        return self



class QueryBatchTaskDetailListResponseBodyDataTaskDetail(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        error_msg: str = None,
        task_no: str = None,
        task_status: str = None,
        task_type: str = None,
        try_count: int = None,
        update_time: str = None,
    ):
        self.domain_name = domain_name
        self.error_msg = error_msg
        self.task_no = task_no
        self.task_status = task_status
        self.task_type = task_type
        self.try_count = try_count
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.task_no is not None:
            result['TaskNo'] = self.task_no

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.try_count is not None:
            result['TryCount'] = self.try_count

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TryCount') is not None:
            self.try_count = m.get('TryCount')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

