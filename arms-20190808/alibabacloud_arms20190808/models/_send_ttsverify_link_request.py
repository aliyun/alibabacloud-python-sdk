# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendTTSVerifyLinkRequest(DaraModel):
    def __init__(
        self,
        contact_id: int = None,
        phone: str = None,
    ):
        # The ID of the alert contact.
        # 
        # This parameter is required.
        self.contact_id = contact_id
        # The mobile number of the alert contact.
        # 
        # This parameter is required.
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.phone is not None:
            result['Phone'] = self.phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        return self

