# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class CreateDocumentAnalyzeTaskRequest(DaraModel):
    def __init__(
        self,
        document: main_models.CreateDocumentAnalyzeTaskRequestDocument = None,
        output: main_models.CreateDocumentAnalyzeTaskRequestOutput = None,
        strategy: main_models.CreateDocumentAnalyzeTaskRequestStrategy = None,
    ):
        self.document = document
        self.output = output
        self.strategy = strategy

    def validate(self):
        if self.document:
            self.document.validate()
        if self.output:
            self.output.validate()
        if self.strategy:
            self.strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document is not None:
            result['document'] = self.document.to_map()

        if self.output is not None:
            result['output'] = self.output.to_map()

        if self.strategy is not None:
            result['strategy'] = self.strategy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('document') is not None:
            temp_model = main_models.CreateDocumentAnalyzeTaskRequestDocument()
            self.document = temp_model.from_map(m.get('document'))

        if m.get('output') is not None:
            temp_model = main_models.CreateDocumentAnalyzeTaskRequestOutput()
            self.output = temp_model.from_map(m.get('output'))

        if m.get('strategy') is not None:
            temp_model = main_models.CreateDocumentAnalyzeTaskRequestStrategy()
            self.strategy = temp_model.from_map(m.get('strategy'))

        return self

class CreateDocumentAnalyzeTaskRequestStrategy(DaraModel):
    def __init__(
        self,
        enable_semantic: bool = None,
    ):
        self.enable_semantic = enable_semantic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_semantic is not None:
            result['enable_semantic'] = self.enable_semantic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable_semantic') is not None:
            self.enable_semantic = m.get('enable_semantic')

        return self

class CreateDocumentAnalyzeTaskRequestOutput(DaraModel):
    def __init__(
        self,
        image_storage: str = None,
    ):
        self.image_storage = image_storage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_storage is not None:
            result['image_storage'] = self.image_storage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image_storage') is not None:
            self.image_storage = m.get('image_storage')

        return self

class CreateDocumentAnalyzeTaskRequestDocument(DaraModel):
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

