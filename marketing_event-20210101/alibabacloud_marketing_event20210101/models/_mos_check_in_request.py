# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MosCheckInRequest(DaraModel):
    def __init__(
        self,
        activity_id: str = None,
        ext_param: str = None,
        qr_code: str = None,
    ):
        self.activity_id = activity_id
        self.ext_param = ext_param
        self.qr_code = qr_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.ext_param is not None:
            result['ExtParam'] = self.ext_param

        if self.qr_code is not None:
            result['QrCode'] = self.qr_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('ExtParam') is not None:
            self.ext_param = m.get('ExtParam')

        if m.get('QrCode') is not None:
            self.qr_code = m.get('QrCode')

        return self

