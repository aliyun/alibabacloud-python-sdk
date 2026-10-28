# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateContactGroupRequest(DaraModel):
    def __init__(
        self,
        contact_group_id: str = None,
        contacts: List[str] = None,
        name: str = None,
        workspace: str = None,
    ):
        # The unique identifier of the contact group.
        self.contact_group_id = contact_group_id
        # The IDs of the contacts.
        self.contacts = contacts
        # The name of the contact.
        self.name = name
        # The name of the workspace.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group_id is not None:
            result['contactGroupId'] = self.contact_group_id

        if self.contacts is not None:
            result['contacts'] = self.contacts

        if self.name is not None:
            result['name'] = self.name

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contactGroupId') is not None:
            self.contact_group_id = m.get('contactGroupId')

        if m.get('contacts') is not None:
            self.contacts = m.get('contacts')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

