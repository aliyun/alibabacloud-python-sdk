# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteAlertContactGroupRequest(DaraModel):
    def __init__(
        self,
        contact_group_ids: List[int] = None,
    ):
        # The list of alert contact group IDs.
        # 
        # This parameter is required.
        self.contact_group_ids = contact_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group_ids is not None:
            result['contact_group_ids'] = self.contact_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contact_group_ids') is not None:
            self.contact_group_ids = m.get('contact_group_ids')

        return self

