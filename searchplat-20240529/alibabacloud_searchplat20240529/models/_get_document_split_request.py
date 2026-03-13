# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetDocumentSplitRequest(DaraModel):
    def __init__(
        self,
        document: main_models.GetDocumentSplitRequestDocument = None,
        strategy: main_models.GetDocumentSplitRequestStrategy = None,
    ):
        # This parameter is required.
        self.document = document
        self.strategy = strategy

    def validate(self):
        if self.document:
            self.document.validate()
        if self.strategy:
            self.strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document is not None:
            result['document'] = self.document.to_map()

        if self.strategy is not None:
            result['strategy'] = self.strategy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('document') is not None:
            temp_model = main_models.GetDocumentSplitRequestDocument()
            self.document = temp_model.from_map(m.get('document'))

        if m.get('strategy') is not None:
            temp_model = main_models.GetDocumentSplitRequestStrategy()
            self.strategy = temp_model.from_map(m.get('strategy'))

        return self

class GetDocumentSplitRequestStrategy(DaraModel):
    def __init__(
        self,
        compute_type: str = None,
        max_chunk_size: int = None,
        need_sentence: bool = None,
    ):
        self.compute_type = compute_type
        self.max_chunk_size = max_chunk_size
        self.need_sentence = need_sentence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_type is not None:
            result['compute_type'] = self.compute_type

        if self.max_chunk_size is not None:
            result['max_chunk_size'] = self.max_chunk_size

        if self.need_sentence is not None:
            result['need_sentence'] = self.need_sentence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('compute_type') is not None:
            self.compute_type = m.get('compute_type')

        if m.get('max_chunk_size') is not None:
            self.max_chunk_size = m.get('max_chunk_size')

        if m.get('need_sentence') is not None:
            self.need_sentence = m.get('need_sentence')

        return self

class GetDocumentSplitRequestDocument(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_encoding: str = None,
        content_type: str = None,
    ):
        self.content = content
        self.content_encoding = content_encoding
        self.content_type = content_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.content_encoding is not None:
            result['content_encoding'] = self.content_encoding

        if self.content_type is not None:
            result['content_type'] = self.content_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('content_encoding') is not None:
            self.content_encoding = m.get('content_encoding')

        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')

        return self

