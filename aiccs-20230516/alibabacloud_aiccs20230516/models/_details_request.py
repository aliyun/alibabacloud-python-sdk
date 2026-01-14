# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DetailsRequest(DaraModel):
    def __init__(
        self,
        batch_id: int = None,
        end_time: str = None,
        number_status: int = None,
        numbers: List[str] = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        task_id: int = None,
    ):
        # 批次id
        self.batch_id = batch_id
        # 结束导入时间
        self.end_time = end_time
        # 号码状态
        self.number_status = number_status
        # 号码列表
        self.numbers = numbers
        self.owner_id = owner_id
        # 页数
        self.page_no = page_no
        # 每页条数
        # 
        # This parameter is required.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 开始导入时间
        self.start_time = start_time
        # 任务id
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.number_status is not None:
            result['NumberStatus'] = self.number_status

        if self.numbers is not None:
            result['Numbers'] = self.numbers

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('NumberStatus') is not None:
            self.number_status = m.get('NumberStatus')

        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

