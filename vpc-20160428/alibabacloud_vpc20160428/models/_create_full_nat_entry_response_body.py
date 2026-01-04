# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFullNatEntryResponseBody(DaraModel):
    def __init__(
        self,
        full_nat_entry_id: str = None,
        request_id: str = None,
    ):
        # The FULLNAT entry ID.
        self.full_nat_entry_id = full_nat_entry_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.full_nat_entry_id is not None:
            result['FullNatEntryId'] = self.full_nat_entry_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FullNatEntryId') is not None:
            self.full_nat_entry_id = m.get('FullNatEntryId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

