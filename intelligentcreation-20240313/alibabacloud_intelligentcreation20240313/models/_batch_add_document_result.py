# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class BatchAddDocumentResult(DaraModel):
    def __init__(
        self,
        add_document_results: List[main_models.AddDocumentResult] = None,
        request_id: str = None,
    ):
        # This parameter is required.
        self.add_document_results = add_document_results
        self.request_id = request_id

    def validate(self):
        if self.add_document_results:
            for v1 in self.add_document_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['addDocumentResults'] = []
        if self.add_document_results is not None:
            for k1 in self.add_document_results:
                result['addDocumentResults'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.add_document_results = []
        if m.get('addDocumentResults') is not None:
            for k1 in m.get('addDocumentResults'):
                temp_model = main_models.AddDocumentResult()
                self.add_document_results.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

