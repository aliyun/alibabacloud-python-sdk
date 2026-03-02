# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class ListGroupsResponseBody(DaraModel):
    def __init__(
        self,
        groups: main_models.ListGroupsResponseBodyGroups = None,
        is_truncated: bool = None,
        marker: str = None,
        request_id: str = None,
    ):
        self.groups = groups
        # Indicates whether the response is truncated. Valid values:
        # 
        # - true
        # 
        # - false
        self.is_truncated = is_truncated
        # The `marker`. This parameter is returned only if the value of `IsTruncated` is `true`. If the parameter is returned, you can call this operation again and set this parameter to obtain the truncated part.
        self.marker = marker
        # The request ID.
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

        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Groups') is not None:
            temp_model = main_models.ListGroupsResponseBodyGroups()
            self.groups = temp_model.from_map(m.get('Groups'))

        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListGroupsResponseBodyGroups(DaraModel):
    def __init__(
        self,
        group: List[main_models.ListGroupsResponseBodyGroupsGroup] = None,
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
                temp_model = main_models.ListGroupsResponseBodyGroupsGroup()
                self.group.append(temp_model.from_map(k1))

        return self

class ListGroupsResponseBodyGroupsGroup(DaraModel):
    def __init__(
        self,
        comments: str = None,
        create_date: str = None,
        display_name: str = None,
        group_id: str = None,
        group_name: str = None,
        update_date: str = None,
    ):
        self.comments = comments
        self.create_date = create_date
        self.display_name = display_name
        self.group_id = group_id
        self.group_name = group_name
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comments is not None:
            result['Comments'] = self.comments

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

