# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMessageGroupUserByIdShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        group_id: str = None,
        user_id_list_shrink: str = None,
    ):
        # The ID of the interactive messaging application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the message group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The list of users.
        # 
        # This parameter is required.
        self.user_id_list_shrink = user_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.user_id_list_shrink is not None:
            result['UserIdList'] = self.user_id_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('UserIdList') is not None:
            self.user_id_list_shrink = m.get('UserIdList')

        return self

