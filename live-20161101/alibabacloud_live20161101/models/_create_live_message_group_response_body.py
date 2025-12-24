# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLiveMessageGroupResponseBody(DaraModel):
    def __init__(
        self,
        already_delete: bool = None,
        already_exists: bool = None,
        group_id: str = None,
        request_id: str = None,
    ):
        # Indicates whether the group is deleted. If the group existed and is deleted, the group ID is unavailable. We recommend that you create a new group.
        self.already_delete = already_delete
        # Indicates whether the group already exists.
        self.already_exists = already_exists
        # The ID of the group created.
        self.group_id = group_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.already_delete is not None:
            result['AlreadyDelete'] = self.already_delete

        if self.already_exists is not None:
            result['AlreadyExists'] = self.already_exists

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlreadyDelete') is not None:
            self.already_delete = m.get('AlreadyDelete')

        if m.get('AlreadyExists') is not None:
            self.already_exists = m.get('AlreadyExists')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

