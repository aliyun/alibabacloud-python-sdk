# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateContactResponseBody(DaraModel):
    def __init__(
        self,
        contact_id: str = None,
        request_id: str = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['contactId'] = self.contact_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contactId') is not None:
            self.contact_id = m.get('contactId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

