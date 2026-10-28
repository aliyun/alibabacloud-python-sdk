# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateContactGroupRequest(DaraModel):
    def __init__(
        self,
        contacts: List[str] = None,
        name: str = None,
    ):
        # The ID of the contact.
        self.contacts = contacts
        # The name of the contact.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contacts is not None:
            result['contacts'] = self.contacts

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contacts') is not None:
            self.contacts = m.get('contacts')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

