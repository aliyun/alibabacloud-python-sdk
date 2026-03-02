# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MonitorContactGroupUpdateCmd(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        contact_ids: List[int] = None,
        id: int = None,
        name: str = None,
    ):
        self.account_id = account_id
        self.contact_ids = contact_ids
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.contact_ids is not None:
            result['contactIds'] = self.contact_ids

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('contactIds') is not None:
            self.contact_ids = m.get('contactIds')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

