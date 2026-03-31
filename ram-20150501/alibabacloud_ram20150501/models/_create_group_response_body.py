# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ram20150501 import models as main_models
from darabonba.model import DaraModel

class CreateGroupResponseBody(DaraModel):
    def __init__(
        self,
        group: main_models.CreateGroupResponseBodyGroup = None,
        request_id: str = None,
    ):
        # The information about the group.
        self.group = group
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group is not None:
            result['Group'] = self.group.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            temp_model = main_models.CreateGroupResponseBodyGroup()
            self.group = temp_model.from_map(m.get('Group'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateGroupResponseBodyGroup(DaraModel):
    def __init__(
        self,
        comments: str = None,
        create_date: str = None,
        group_id: str = None,
        group_name: str = None,
    ):
        # The description.
        self.comments = comments
        # The creation time.
        self.create_date = create_date
        # The ID of the user group.
        self.group_id = group_id
        # The name of the user group.
        self.group_name = group_name

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

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

