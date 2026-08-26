# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MuteAllGroupUserRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        broad_cast_type: int = None,
        group_id: str = None,
        operator_user_id: str = None,
    ):
        # The application ID for interactive messages.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The system message diffusion type. Valid values:
        # 
        # - 0: No diffusion.
        # - 1: Diffusion to specified users.
        # - 2: Diffusion to the group.
        self.broad_cast_type = broad_cast_type
        # The message group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The user ID of the operator. This user must be the creator of the group.
        # 
        # This parameter is required.
        self.operator_user_id = operator_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.broad_cast_type is not None:
            result['BroadCastType'] = self.broad_cast_type

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.operator_user_id is not None:
            result['OperatorUserId'] = self.operator_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BroadCastType') is not None:
            self.broad_cast_type = m.get('BroadCastType')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('OperatorUserId') is not None:
            self.operator_user_id = m.get('OperatorUserId')

        return self

