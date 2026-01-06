# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMembersRequest(DaraModel):
    def __init__(
        self,
        member_ids: str = None,
    ):
        # The list of member IDs. Separate multiple member IDs with commas (,). You can call [ListMembers](https://help.aliyun.com/document_detail/449135.html) to obtain the member ID.
        # 
        # This parameter is required.
        self.member_ids = member_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_ids is not None:
            result['MemberIds'] = self.member_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberIds') is not None:
            self.member_ids = m.get('MemberIds')

        return self

