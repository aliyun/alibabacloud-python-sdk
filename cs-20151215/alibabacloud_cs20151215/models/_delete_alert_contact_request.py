# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteAlertContactRequest(DaraModel):
    def __init__(
        self,
        contact_ids: List[int] = None,
    ):
        # The list of alert contact IDs.
        # 
        # This parameter is required.
        self.contact_ids = contact_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_ids is not None:
            result['contact_ids'] = self.contact_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contact_ids') is not None:
            self.contact_ids = m.get('contact_ids')

        return self

