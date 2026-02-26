# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class DetectImageCodesResponseBody(DaraModel):
    def __init__(
        self,
        codes: List[main_models.Codes] = None,
        request_id: str = None,
    ):
        # The barcodes or QR codes.
        # 
        # This parameter is required.
        self.codes = codes
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.codes:
            for v1 in self.codes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Codes'] = []
        if self.codes is not None:
            for k1 in self.codes:
                result['Codes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.codes = []
        if m.get('Codes') is not None:
            for k1 in m.get('Codes'):
                temp_model = main_models.Codes()
                self.codes.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

