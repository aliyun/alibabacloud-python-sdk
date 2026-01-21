# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class GetUserGroupResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_group: main_models.GetUserGroupResponseBodyUserGroup = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the user group returned.
        self.user_group = user_group

    def validate(self):
        if self.user_group:
            self.user_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_group is not None:
            result['UserGroup'] = self.user_group.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserGroup') is not None:
            temp_model = main_models.GetUserGroupResponseBodyUserGroup()
            self.user_group = temp_model.from_map(m.get('UserGroup'))

        return self

class GetUserGroupResponseBodyUserGroup(DaraModel):
    def __init__(
        self,
        comment: str = None,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        # The description of the user group.
        self.comment = comment
        # The ID of the group.
        self.user_group_id = user_group_id
        # The name of the user group.
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')

        return self

