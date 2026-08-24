# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchCreateDomainItemsRequest(DaraModel):
    def __init__(
        self,
        domain_items: List[str] = None,
        list_id: str = None,
        list_type: str = None,
    ):
        # The domain name list.
        self.domain_items = domain_items
        # The list ID. This is a unique business identifier used for policy references and add, delete, and modify operations.
        self.list_id = list_id
        # The list type (Blacklist/Whitelist).
        self.list_type = list_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_items is not None:
            result['DomainItems'] = self.domain_items

        if self.list_id is not None:
            result['ListId'] = self.list_id

        if self.list_type is not None:
            result['ListType'] = self.list_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainItems') is not None:
            self.domain_items = m.get('DomainItems')

        if m.get('ListId') is not None:
            self.list_id = m.get('ListId')

        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')

        return self

