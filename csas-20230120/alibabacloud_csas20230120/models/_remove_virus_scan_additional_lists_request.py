# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RemoveVirusScanAdditionalListsRequest(DaraModel):
    def __init__(
        self,
        list_ids: List[str] = None,
    ):
        # The collection of entry IDs to remove. At least one entry ID must be specified.
        # 
        # This parameter is required.
        self.list_ids = list_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_ids is not None:
            result['ListIds'] = self.list_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListIds') is not None:
            self.list_ids = m.get('ListIds')

        return self

