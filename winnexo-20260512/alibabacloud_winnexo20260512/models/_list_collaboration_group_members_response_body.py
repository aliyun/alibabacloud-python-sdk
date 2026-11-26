# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListCollaborationGroupMembersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListCollaborationGroupMembersResponseBodyItems] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The common business status code.
        self.code = code
        # The list of entries on the current page.
        self.items = items
        # The common error description.
        self.message = message
        # The current page number.
        self.page = page
        # The page size.
        self.page_size = page_size
        # The request tracking ID.
        self.request_id = request_id
        # The total number of records after filtering.
        self.total = total

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListCollaborationGroupMembersResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListCollaborationGroupMembersResponseBodyItems(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        is_active: bool = None,
        role: str = None,
        user_id: str = None,
    ):
        # The display name. This field is empty if not set.
        self.display_name = display_name
        # The enabling status of the tenant account. Only active members are returned, so this value is always true. It does not represent the employment status.
        self.is_active = is_active
        # The role of the workspace member.
        self.role = role
        # The platform user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.is_active is not None:
            result['isActive'] = self.is_active

        if self.role is not None:
            result['role'] = self.role

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('isActive') is not None:
            self.is_active = m.get('isActive')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

