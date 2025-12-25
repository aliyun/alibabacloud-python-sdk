# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class UploadBookRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        docs: List[main_models.UploadBookRequestDocs] = None,
        workspace_id: str = None,
    ):
        self.category_id = category_id
        # This parameter is required.
        self.docs = docs
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.docs:
            for v1 in self.docs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        result['Docs'] = []
        if self.docs is not None:
            for k1 in self.docs:
                result['Docs'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        self.docs = []
        if m.get('Docs') is not None:
            for k1 in m.get('Docs'):
                temp_model = main_models.UploadBookRequestDocs()
                self.docs.append(temp_model.from_map(k1))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class UploadBookRequestDocs(DaraModel):
    def __init__(
        self,
        doc_name: str = None,
        file_url: str = None,
    ):
        self.doc_name = doc_name
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_name is not None:
            result['DocName'] = self.doc_name

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        return self

