# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfirmReceiptCmd(DaraModel):
    def __init__(
        self,
        dispute_id: str = None,
    ):
        self.dispute_id = dispute_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dispute_id is not None:
            result['disputeId'] = self.dispute_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disputeId') is not None:
            self.dispute_id = m.get('disputeId')

        return self

