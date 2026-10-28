# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListOncallContactsResponseBody(DaraModel):
    def __init__(
        self,
        contact_ids: List[str] = None,
        request_id: str = None,
    ):
        # The IDs of the contacts.
        self.contact_ids = contact_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_ids is not None:
            result['contactIds'] = self.contact_ids

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contactIds') is not None:
            self.contact_ids = m.get('contactIds')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

