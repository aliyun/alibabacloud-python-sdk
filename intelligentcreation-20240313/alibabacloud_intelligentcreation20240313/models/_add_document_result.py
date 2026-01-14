# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class AddDocumentResult(DaraModel):
    def __init__(
        self,
        doc_name: str = None,
        document_info: main_models.DocumentInfo = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.doc_name = doc_name
        self.document_info = document_info
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.document_info:
            self.document_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_name is not None:
            result['docName'] = self.doc_name

        if self.document_info is not None:
            result['documentInfo'] = self.document_info.to_map()

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docName') is not None:
            self.doc_name = m.get('docName')

        if m.get('documentInfo') is not None:
            temp_model = main_models.DocumentInfo()
            self.document_info = temp_model.from_map(m.get('documentInfo'))

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

