# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AssociateMembersRequest(DaraModel):
    def __init__(
        self,
        contact_id: str = None,
        members: List[str] = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The IDs of objects to which you want to bind the contact.
        self.members = members

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.members is not None:
            result['Members'] = self.members

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('Members') is not None:
            self.members = m.get('Members')

        return self

