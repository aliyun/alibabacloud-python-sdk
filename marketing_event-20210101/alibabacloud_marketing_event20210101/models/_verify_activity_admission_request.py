# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyActivityAdmissionRequest(DaraModel):
    def __init__(
        self,
        activity_id: int = None,
        id_card_no: str = None,
    ):
        # This parameter is required.
        self.activity_id = activity_id
        # This parameter is required.
        self.id_card_no = id_card_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.id_card_no is not None:
            result['IdCardNo'] = self.id_card_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('IdCardNo') is not None:
            self.id_card_no = m.get('IdCardNo')

        return self

