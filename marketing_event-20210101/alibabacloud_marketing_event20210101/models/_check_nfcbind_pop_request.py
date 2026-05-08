# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckNFCBindPopRequest(DaraModel):
    def __init__(
        self,
        activity_id: int = None,
        nfc_id: str = None,
    ):
        # This parameter is required.
        self.activity_id = activity_id
        # This parameter is required.
        self.nfc_id = nfc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.nfc_id is not None:
            result['NfcId'] = self.nfc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('NfcId') is not None:
            self.nfc_id = m.get('NfcId')

        return self

