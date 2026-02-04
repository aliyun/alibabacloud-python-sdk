# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class DisassociateMembersResponseBody(DaraModel):
    def __init__(
        self,
        members: List[main_models.DisassociateMembersResponseBodyMembers] = None,
        request_id: str = None,
    ):
        # The time when the contact was unbound from the object.
        self.members = members
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.members:
            for v1 in self.members:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Members'] = []
        if self.members is not None:
            for k1 in self.members:
                result['Members'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k1 in m.get('Members'):
                temp_model = main_models.DisassociateMembersResponseBodyMembers()
                self.members.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DisassociateMembersResponseBodyMembers(DaraModel):
    def __init__(
        self,
        contact_id: str = None,
        member_id: str = None,
        modify_date: str = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The ID of the object. Valid values:
        # 
        # - ID of the resource directory
        # - ID of the folder
        # - ID of the member
        self.member_id = member_id
        # The time when the contact was unbound from the object.
        self.modify_date = modify_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.modify_date is not None:
            result['ModifyDate'] = self.modify_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('ModifyDate') is not None:
            self.modify_date = m.get('ModifyDate')

        return self

