# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetMultiModalRerankerRequest(DaraModel):
    def __init__(
        self,
        docs: List[main_models.GetMultiModalRerankerRequestDocs] = None,
        options: Dict[str, Any] = None,
        query: main_models.GetMultiModalRerankerRequestQuery = None,
    ):
        self.docs = docs
        self.options = options
        self.query = query

    def validate(self):
        if self.docs:
            for v1 in self.docs:
                 if v1:
                    v1.validate()
        if self.query:
            self.query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['docs'] = []
        if self.docs is not None:
            for k1 in self.docs:
                result['docs'].append(k1.to_map() if k1 else None)

        if self.options is not None:
            result['options'] = self.options

        if self.query is not None:
            result['query'] = self.query.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.docs = []
        if m.get('docs') is not None:
            for k1 in m.get('docs'):
                temp_model = main_models.GetMultiModalRerankerRequestDocs()
                self.docs.append(temp_model.from_map(k1))

        if m.get('options') is not None:
            self.options = m.get('options')

        if m.get('query') is not None:
            temp_model = main_models.GetMultiModalRerankerRequestQuery()
            self.query = temp_model.from_map(m.get('query'))

        return self

class GetMultiModalRerankerRequestQuery(DaraModel):
    def __init__(
        self,
        image: str = None,
        text: str = None,
    ):
        self.image = image
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image is not None:
            result['image'] = self.image

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

class GetMultiModalRerankerRequestDocs(DaraModel):
    def __init__(
        self,
        image: str = None,
        text: str = None,
    ):
        self.image = image
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image is not None:
            result['image'] = self.image

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

