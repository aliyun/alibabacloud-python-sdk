# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ListMessageGroupUserByIdResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.ListMessageGroupUserByIdResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.ListMessageGroupUserByIdResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class ListMessageGroupUserByIdResponseBodyResult(DaraModel):
    def __init__(
        self,
        has_more: bool = None,
        total: int = None,
        user_list: List[main_models.ListMessageGroupUserByIdResponseBodyResultUserList] = None,
    ):
        # Indicates whether the current page is followed by another page. Valid values:
        # 
        # *   true
        # *   false
        self.has_more = has_more
        # The total number of users returned.
        self.total = total
        # The list of users.
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for v1 in self.user_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_more is not None:
            result['HasMore'] = self.has_more

        if self.total is not None:
            result['Total'] = self.total

        result['UserList'] = []
        if self.user_list is not None:
            for k1 in self.user_list:
                result['UserList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        self.user_list = []
        if m.get('UserList') is not None:
            for k1 in m.get('UserList'):
                temp_model = main_models.ListMessageGroupUserByIdResponseBodyResultUserList()
                self.user_list.append(temp_model.from_map(k1))

        return self

class ListMessageGroupUserByIdResponseBodyResultUserList(DaraModel):
    def __init__(
        self,
        is_mute: bool = None,
        mute_by: List[str] = None,
        user_avatar: str = None,
        user_extension: str = None,
        user_id: str = None,
        user_nick: str = None,
    ):
        # Indicates whether the user is muted. Valid values:
        # 
        # *   true: The user is muted.
        # *   false: The user is not muted.
        self.is_mute = is_mute
        # The type of the mute. Valid values:
        # 
        # *   group: All members in the message group are muted.
        # *   user: Specific members in the message group are muted.
        self.mute_by = mute_by
        # The URL of the profile picture of the user.
        self.user_avatar = user_avatar
        # The custom information about the user.
        self.user_extension = user_extension
        # The ID of the user.
        self.user_id = user_id
        # The nickname of the user.
        self.user_nick = user_nick

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_mute is not None:
            result['IsMute'] = self.is_mute

        if self.mute_by is not None:
            result['MuteBy'] = self.mute_by

        if self.user_avatar is not None:
            result['UserAvatar'] = self.user_avatar

        if self.user_extension is not None:
            result['UserExtension'] = self.user_extension

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_nick is not None:
            result['UserNick'] = self.user_nick

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsMute') is not None:
            self.is_mute = m.get('IsMute')

        if m.get('MuteBy') is not None:
            self.mute_by = m.get('MuteBy')

        if m.get('UserAvatar') is not None:
            self.user_avatar = m.get('UserAvatar')

        if m.get('UserExtension') is not None:
            self.user_extension = m.get('UserExtension')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')

        return self

