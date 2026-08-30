# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BindSaseUserTagRequest(DaraModel):
    def __init__(
        self,
        sase_user_ids: List[str] = None,
        tag_ids: List[str] = None,
    ):
        # The collection of user IDs.
        self.sase_user_ids = sase_user_ids
        # The collection of user label IDs.
        self.tag_ids = tag_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sase_user_ids is not None:
            result['SaseUserIds'] = self.sase_user_ids

        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SaseUserIds') is not None:
            self.sase_user_ids = m.get('SaseUserIds')

        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')

        return self

