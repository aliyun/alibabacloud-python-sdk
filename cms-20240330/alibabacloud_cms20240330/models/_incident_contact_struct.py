# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class IncidentContactStruct(DaraModel):
    def __init__(
        self,
        channel: List[str] = None,
        contact_id: str = None,
        contact_type: str = None,
    ):
        self.channel = channel
        self.contact_id = contact_id
        self.contact_type = contact_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['channel'] = self.channel

        if self.contact_id is not None:
            result['contactId'] = self.contact_id

        if self.contact_type is not None:
            result['contactType'] = self.contact_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')

        if m.get('contactId') is not None:
            self.contact_id = m.get('contactId')

        if m.get('contactType') is not None:
            self.contact_type = m.get('contactType')

        return self

