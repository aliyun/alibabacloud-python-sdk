# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddFileProtectBindMachineRequest(DaraModel):
    def __init__(
        self,
        alert_uuids: List[str] = None,
        block_uuids: List[str] = None,
        none_uuids: List[str] = None,
    ):
        self.alert_uuids = alert_uuids
        self.block_uuids = block_uuids
        self.none_uuids = none_uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_uuids is not None:
            result['AlertUuids'] = self.alert_uuids

        if self.block_uuids is not None:
            result['BlockUuids'] = self.block_uuids

        if self.none_uuids is not None:
            result['NoneUuids'] = self.none_uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertUuids') is not None:
            self.alert_uuids = m.get('AlertUuids')

        if m.get('BlockUuids') is not None:
            self.block_uuids = m.get('BlockUuids')

        if m.get('NoneUuids') is not None:
            self.none_uuids = m.get('NoneUuids')

        return self

