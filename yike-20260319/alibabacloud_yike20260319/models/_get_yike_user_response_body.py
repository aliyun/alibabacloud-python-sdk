# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yike20260319 import models as main_models
from darabonba.model import DaraModel

class GetYikeUserResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_info: main_models.GetYikeUserResponseBodyUserInfo = None,
    ):
        # RequestId
        self.request_id = request_id
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserInfo') is not None:
            temp_model = main_models.GetYikeUserResponseBodyUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class GetYikeUserResponseBodyUserInfo(DaraModel):
    def __init__(
        self,
        nickname: str = None,
        user_name: str = None,
        workspace_id: str = None,
        yike_user_id: str = None,
    ):
        self.nickname = nickname
        self.user_name = user_name
        self.workspace_id = workspace_id
        self.yike_user_id = yike_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nickname is not None:
            result['Nickname'] = self.nickname

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.yike_user_id is not None:
            result['YikeUserId'] = self.yike_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nickname') is not None:
            self.nickname = m.get('Nickname')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('YikeUserId') is not None:
            self.yike_user_id = m.get('YikeUserId')

        return self

