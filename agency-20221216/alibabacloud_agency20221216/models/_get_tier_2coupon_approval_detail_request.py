# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTier2CouponApprovalDetailRequest(DaraModel):
    def __init__(
        self,
        application_sheet_id: str = None,
    ):
        self.application_sheet_id = application_sheet_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_sheet_id is not None:
            result['ApplicationSheetId'] = self.application_sheet_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationSheetId') is not None:
            self.application_sheet_id = m.get('ApplicationSheetId')

        return self

