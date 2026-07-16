# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMemberRequest(DaraModel):
    def __init__(
        self,
        member_id: str = None,
        user_id: str = None,
    ):
        # The member UID. You must specify either UserId or MemberId. You cannot specify both.
        self.member_id = member_id
        # The user UID. For more information about how to view the user UID, see [ListWorkspaceUsers](https://help.aliyun.com/document_detail/449133.html). You must specify either UserId or MemberId. You cannot specify both.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

