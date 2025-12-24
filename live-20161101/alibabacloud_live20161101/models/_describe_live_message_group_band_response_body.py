# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeLiveMessageGroupBandResponseBody(DaraModel):
    def __init__(
        self,
        banned_user_list: List[str] = None,
        group_id: str = None,
        isbanned_all: bool = None,
        request_id: str = None,
        unbanned_user_list: List[str] = None,
    ):
        # The list of users that were muted separately, but not by muting the entire group.
        self.banned_user_list = banned_user_list
        # The group ID.
        self.group_id = group_id
        # Indicates whether all users in the interactive messaging group are muted.
        self.isbanned_all = isbanned_all
        # The request ID.
        self.request_id = request_id
        # The list of users who were not muted when the entire group was muted.
        self.unbanned_user_list = unbanned_user_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.banned_user_list is not None:
            result['BannedUserList'] = self.banned_user_list

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.isbanned_all is not None:
            result['IsbannedAll'] = self.isbanned_all

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.unbanned_user_list is not None:
            result['UnbannedUserList'] = self.unbanned_user_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BannedUserList') is not None:
            self.banned_user_list = m.get('BannedUserList')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('IsbannedAll') is not None:
            self.isbanned_all = m.get('IsbannedAll')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UnbannedUserList') is not None:
            self.unbanned_user_list = m.get('UnbannedUserList')

        return self

