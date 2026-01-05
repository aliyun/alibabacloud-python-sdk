# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CreateSlotsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        slot_ids: str = None,
        summary: Dict[str, str] = None,
    ):
        self.request_id = request_id
        self.slot_ids = slot_ids
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.slot_ids is not None:
            result['SlotIds'] = self.slot_ids

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlotIds') is not None:
            self.slot_ids = m.get('SlotIds')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

