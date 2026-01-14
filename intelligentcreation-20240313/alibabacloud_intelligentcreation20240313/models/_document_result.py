# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class DocumentResult(DaraModel):
    def __init__(
        self,
        document_info: main_models.DocumentInfo = None,
        request_id: str = None,
    ):
        self.document_info = document_info
        self.request_id = request_id

    def validate(self):
        if self.document_info:
            self.document_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document_info is not None:
            result['documentInfo'] = self.document_info.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('documentInfo') is not None:
            temp_model = main_models.DocumentInfo()
            self.document_info = temp_model.from_map(m.get('documentInfo'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

