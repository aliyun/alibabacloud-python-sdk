# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class ListGroupsForUserResponseBody(DaraModel):
    def __init__(
        self,
        groups: main_models.ListGroupsForUserResponseBodyGroups = None,
        request_id: str = None,
    ):
        self.groups = groups
        self.request_id = request_id

    def validate(self):
        if self.groups:
            self.groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.groups is not None:
            result['Groups'] = self.groups.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Groups') is not None:
            temp_model = main_models.ListGroupsForUserResponseBodyGroups()
            self.groups = temp_model.from_map(m.get('Groups'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListGroupsForUserResponseBodyGroups(DaraModel):
    def __init__(
        self,
        group: List[main_models.ListGroupsForUserResponseBodyGroupsGroup] = None,
    ):
        self.group = group

    def validate(self):
        if self.group:
            for v1 in self.group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Group'] = []
        if self.group is not None:
            for k1 in self.group:
                result['Group'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group = []
        if m.get('Group') is not None:
            for k1 in m.get('Group'):
                temp_model = main_models.ListGroupsForUserResponseBodyGroupsGroup()
                self.group.append(temp_model.from_map(k1))

        return self

class ListGroupsForUserResponseBodyGroupsGroup(DaraModel):
    def __init__(
        self,
        comments: str = None,
        display_name: str = None,
        group_id: str = None,
        group_name: str = None,
        join_date: str = None,
    ):
        self.comments = comments
        self.display_name = display_name
        self.group_id = group_id
        self.group_name = group_name
        self.join_date = join_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comments is not None:
            result['Comments'] = self.comments

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.join_date is not None:
            result['JoinDate'] = self.join_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('JoinDate') is not None:
            self.join_date = m.get('JoinDate')

        return self

