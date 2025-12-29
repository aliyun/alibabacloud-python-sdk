# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryTaskListShrinkRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        owner_id: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        result_shrink: str = None,
        tag_id: int = None,
        task_id: int = None,
        task_name: str = None,
        task_type_shrink: str = None,
    ):
        self.current_page = current_page
        self.owner_id = owner_id
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.result_shrink = result_shrink
        self.tag_id = tag_id
        self.task_id = task_id
        self.task_name = task_name
        self.task_type_shrink = task_type_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.result_shrink is not None:
            result['Result'] = self.result_shrink

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type_shrink is not None:
            result['TaskType'] = self.task_type_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Result') is not None:
            self.result_shrink = m.get('Result')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type_shrink = m.get('TaskType')

        return self

