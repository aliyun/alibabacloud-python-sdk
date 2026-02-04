# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMessageContactRequest(DaraModel):
    def __init__(
        self,
        contact_id: str = None,
        retain_contact_in_members: bool = None,
    ):
        # The ID of the contact.
        # 
        # This parameter is required.
        self.contact_id = contact_id
        # Specifies whether to retain the contact for members. Valid values:
        # 
        # *   true (default): retains the contact for members. In this case, the contact can still receive messages for the members.
        # *   false: does not retain the contact for members. In this case, the contact can no longer receive messages for the members. If you set this parameter to false, the response is asynchronously returned. You can call [GetMessageContactDeletionStatus](~~GetMessageContactDeletionStatus~~) to obtain the deletion result.
        self.retain_contact_in_members = retain_contact_in_members

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.retain_contact_in_members is not None:
            result['RetainContactInMembers'] = self.retain_contact_in_members

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('RetainContactInMembers') is not None:
            self.retain_contact_in_members = m.get('RetainContactInMembers')

        return self

