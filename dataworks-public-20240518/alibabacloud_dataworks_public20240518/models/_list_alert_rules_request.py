# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAlertRulesRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        receiver: str = None,
        task_ids: List[int] = None,
        types: List[str] = None,
    ):
        # The name of the rule.
        self.name = name
        # The ID of the Alibaba Cloud account used by the owner of the rule.
        self.owner = owner
        # The page number. Pages start from page 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the Alibaba Cloud account used by the alert recipient.
        self.receiver = receiver
        # The IDs of the scheduling tasks.
        self.task_ids = task_ids
        # The alert triggering condition.
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.receiver is not None:
            result['Receiver'] = self.receiver

        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        if self.types is not None:
            result['Types'] = self.types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Receiver') is not None:
            self.receiver = m.get('Receiver')

        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        if m.get('Types') is not None:
            self.types = m.get('Types')

        return self

