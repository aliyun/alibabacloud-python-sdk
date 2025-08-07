# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 
from typing import List


class AlterShareReceiversRequest(DaraModel):
    def __init__(
        self,
        added_receivers: List[str] = None,
        removed_receivers: List[str] = None,
    ):
        self.added_receivers = added_receivers
        self.removed_receivers = removed_receivers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.added_receivers is not None:
            result['addedReceivers'] = self.added_receivers

        if self.removed_receivers is not None:
            result['removedReceivers'] = self.removed_receivers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addedReceivers') is not None:
            self.added_receivers = m.get('addedReceivers')

        if m.get('removedReceivers') is not None:
            self.removed_receivers = m.get('removedReceivers')

        return self

