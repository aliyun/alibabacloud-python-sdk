# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAlertContactShrinkRequest(DaraModel):
    def __init__(
        self,
        contact_ids_shrink: str = None,
    ):
        # The list of alert contact IDs.
        # 
        # This parameter is required.
        self.contact_ids_shrink = contact_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_ids_shrink is not None:
            result['contact_ids'] = self.contact_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contact_ids') is not None:
            self.contact_ids_shrink = m.get('contact_ids')

        return self

