# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class DetectImageTextsResponseBody(DaraModel):
    def __init__(
        self,
        ocrcontents: List[main_models.OCRContents] = None,
        ocrtexts: str = None,
        request_id: str = None,
    ):
        # OCR text blocks.
        self.ocrcontents = ocrcontents
        # The full Optical Character Recognition (OCR) text, which is spliced by using the content of OCRContents.
        self.ocrtexts = ocrtexts
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.ocrcontents:
            for v1 in self.ocrcontents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OCRContents'] = []
        if self.ocrcontents is not None:
            for k1 in self.ocrcontents:
                result['OCRContents'].append(k1.to_map() if k1 else None)

        if self.ocrtexts is not None:
            result['OCRTexts'] = self.ocrtexts

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ocrcontents = []
        if m.get('OCRContents') is not None:
            for k1 in m.get('OCRContents'):
                temp_model = main_models.OCRContents()
                self.ocrcontents.append(temp_model.from_map(k1))

        if m.get('OCRTexts') is not None:
            self.ocrtexts = m.get('OCRTexts')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

