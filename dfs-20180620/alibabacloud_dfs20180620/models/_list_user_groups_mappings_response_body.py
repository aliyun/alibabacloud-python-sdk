# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dfs20180620 import models as main_models
from darabonba.model import DaraModel

class ListUserGroupsMappingsResponseBody(DaraModel):
    def __init__(
        self,
        has_more: bool = None,
        next_token: str = None,
        request_id: str = None,
        user_groups_mappings: List[main_models.ListUserGroupsMappingsResponseBodyUserGroupsMappings] = None,
    ):
        self.has_more = has_more
        self.next_token = next_token
        self.request_id = request_id
        self.user_groups_mappings = user_groups_mappings

    def validate(self):
        if self.user_groups_mappings:
            for v1 in self.user_groups_mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_more is not None:
            result['HasMore'] = self.has_more

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UserGroupsMappings'] = []
        if self.user_groups_mappings is not None:
            for k1 in self.user_groups_mappings:
                result['UserGroupsMappings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.user_groups_mappings = []
        if m.get('UserGroupsMappings') is not None:
            for k1 in m.get('UserGroupsMappings'):
                temp_model = main_models.ListUserGroupsMappingsResponseBodyUserGroupsMappings()
                self.user_groups_mappings.append(temp_model.from_map(k1))

        return self

class ListUserGroupsMappingsResponseBodyUserGroupsMappings(DaraModel):
    def __init__(
        self,
        group_names: List[str] = None,
        user_name: str = None,
    ):
        self.group_names = group_names
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_names is not None:
            result['GroupNames'] = self.group_names

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupNames') is not None:
            self.group_names = m.get('GroupNames')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

