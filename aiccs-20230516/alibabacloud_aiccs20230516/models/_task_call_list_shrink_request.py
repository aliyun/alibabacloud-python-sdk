# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TaskCallListShrinkRequest(DaraModel):
    def __init__(
        self,
        batch_id: str = None,
        call_date: str = None,
        end_call_date: str = None,
        intent_tags_shrink: str = None,
        numbers_shrink: str = None,
        owner_id: int = None,
        page: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: int = None,
    ):
        # 导入号码时返回的批次号
        self.batch_id = batch_id
        # 开始外呼时间
        # 
        # This parameter is required.
        self.call_date = call_date
        # 结束外呼时间
        # 
        # This parameter is required.
        self.end_call_date = end_call_date
        # 意向标签
        self.intent_tags_shrink = intent_tags_shrink
        # 号码列表
        self.numbers_shrink = numbers_shrink
        self.owner_id = owner_id
        # 页数
        # 
        # This parameter is required.
        self.page = page
        # 每页外呼记录数,正整数，默认10000
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 任务ID
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

        if self.call_date is not None:
            result['CallDate'] = self.call_date

        if self.end_call_date is not None:
            result['EndCallDate'] = self.end_call_date

        if self.intent_tags_shrink is not None:
            result['IntentTags'] = self.intent_tags_shrink

        if self.numbers_shrink is not None:
            result['Numbers'] = self.numbers_shrink

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        if m.get('CallDate') is not None:
            self.call_date = m.get('CallDate')

        if m.get('EndCallDate') is not None:
            self.end_call_date = m.get('EndCallDate')

        if m.get('IntentTags') is not None:
            self.intent_tags_shrink = m.get('IntentTags')

        if m.get('Numbers') is not None:
            self.numbers_shrink = m.get('Numbers')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

