# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class CreateImageAnalyzeTaskRequest(DaraModel):
    def __init__(
        self,
        document: main_models.CreateImageAnalyzeTaskRequestDocument = None,
    ):
        self.document = document

    def validate(self):
        if self.document:
            self.document.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document is not None:
            result['document'] = self.document.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('document') is not None:
            temp_model = main_models.CreateImageAnalyzeTaskRequestDocument()
            self.document = temp_model.from_map(m.get('document'))

        return self

class CreateImageAnalyzeTaskRequestDocument(DaraModel):
    def __init__(
        self,
        content: str = None,
        file_name: str = None,
        file_type: str = None,
        url: str = None,
    ):
        self.content = content
        self.file_name = file_name
        self.file_type = file_type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.file_name is not None:
            result['file_name'] = self.file_name

        if self.file_type is not None:
            result['file_type'] = self.file_type

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')

        if m.get('file_type') is not None:
            self.file_type = m.get('file_type')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

