# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAssetSelectionSelectedTargetRequest(DaraModel):
    def __init__(
        self,
        selection_key: str = None,
        target_list: List[str] = None,
    ):
        # The unique ID of the asset.
        # 
        # This parameter is required.
        self.selection_key = selection_key
        # The details of queries.
        self.target_list = target_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.selection_key is not None:
            result['SelectionKey'] = self.selection_key

        if self.target_list is not None:
            result['TargetList'] = self.target_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SelectionKey') is not None:
            self.selection_key = m.get('SelectionKey')

        if m.get('TargetList') is not None:
            self.target_list = m.get('TargetList')

        return self

