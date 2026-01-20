# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ReadOutboundTaskCallListRequest(DaraModel):
    def __init__(
        self,
        current: int = None,
        customer_name_or_phone: str = None,
        display_status_list: List[str] = None,
        label_tags: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        size: int = None,
        task_id: str = None,
        user_id: str = None,
    ):
        self.current = current
        self.customer_name_or_phone = customer_name_or_phone
        self.display_status_list = display_status_list
        self.label_tags = label_tags
        self.max_results = max_results
        # nextToken
        self.next_token = next_token
        self.size = size
        self.task_id = task_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current is not None:
            result['Current'] = self.current

        if self.customer_name_or_phone is not None:
            result['CustomerNameOrPhone'] = self.customer_name_or_phone

        if self.display_status_list is not None:
            result['DisplayStatusList'] = self.display_status_list

        if self.label_tags is not None:
            result['LabelTags'] = self.label_tags

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.size is not None:
            result['Size'] = self.size

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('CustomerNameOrPhone') is not None:
            self.customer_name_or_phone = m.get('CustomerNameOrPhone')

        if m.get('DisplayStatusList') is not None:
            self.display_status_list = m.get('DisplayStatusList')

        if m.get('LabelTags') is not None:
            self.label_tags = m.get('LabelTags')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

