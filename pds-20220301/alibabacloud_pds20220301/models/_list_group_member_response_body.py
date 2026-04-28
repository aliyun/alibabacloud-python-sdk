# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class ListGroupMemberResponseBody(DaraModel):
    def __init__(
        self,
        group_items: List[main_models.Group] = None,
        next_marker: str = None,
        user_items: List[main_models.User] = None,
    ):
        # The information about the groups.
        self.group_items = group_items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker
        # The information about the users.
        self.user_items = user_items

    def validate(self):
        if self.group_items:
            for v1 in self.group_items:
                 if v1:
                    v1.validate()
        if self.user_items:
            for v1 in self.user_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['group_items'] = []
        if self.group_items is not None:
            for k1 in self.group_items:
                result['group_items'].append(k1.to_map() if k1 else None)

        if self.next_marker is not None:
            result['next_marker'] = self.next_marker

        result['user_items'] = []
        if self.user_items is not None:
            for k1 in self.user_items:
                result['user_items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group_items = []
        if m.get('group_items') is not None:
            for k1 in m.get('group_items'):
                temp_model = main_models.Group()
                self.group_items.append(temp_model.from_map(k1))

        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')

        self.user_items = []
        if m.get('user_items') is not None:
            for k1 in m.get('user_items'):
                temp_model = main_models.User()
                self.user_items.append(temp_model.from_map(k1))

        return self

