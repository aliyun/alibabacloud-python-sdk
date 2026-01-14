# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class TaskRecoverCallRequest(DaraModel):
    def __init__(
        self,
        begin_import_time: str = None,
        end_import_time: str = None,
        numbers: List[str] = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags: List[str] = None,
        task_id: int = None,
    ):
        # 查询开始导入时间
        self.begin_import_time = begin_import_time
        # 查询结束导入时间
        self.end_import_time = end_import_time
        # 号码列表
        self.numbers = numbers
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 用户自定义标签列表
        self.tags = tags
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
        if self.begin_import_time is not None:
            result['BeginImportTime'] = self.begin_import_time

        if self.end_import_time is not None:
            result['EndImportTime'] = self.end_import_time

        if self.numbers is not None:
            result['Numbers'] = self.numbers

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginImportTime') is not None:
            self.begin_import_time = m.get('BeginImportTime')

        if m.get('EndImportTime') is not None:
            self.end_import_time = m.get('EndImportTime')

        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

