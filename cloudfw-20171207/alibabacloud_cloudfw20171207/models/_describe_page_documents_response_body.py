# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribePageDocumentsResponseBody(DaraModel):
    def __init__(
        self,
        docs: List[main_models.DescribePageDocumentsResponseBodyDocs] = None,
        image_url: str = None,
        module: str = None,
        more: main_models.DescribePageDocumentsResponseBodyMore = None,
        request_id: str = None,
    ):
        self.docs = docs
        self.image_url = image_url
        self.module = module
        self.more = more
        self.request_id = request_id

    def validate(self):
        if self.docs:
            for v1 in self.docs:
                 if v1:
                    v1.validate()
        if self.more:
            self.more.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Docs'] = []
        if self.docs is not None:
            for k1 in self.docs:
                result['Docs'].append(k1.to_map() if k1 else None)

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.module is not None:
            result['Module'] = self.module

        if self.more is not None:
            result['More'] = self.more.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.docs = []
        if m.get('Docs') is not None:
            for k1 in m.get('Docs'):
                temp_model = main_models.DescribePageDocumentsResponseBodyDocs()
                self.docs.append(temp_model.from_map(k1))

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('More') is not None:
            temp_model = main_models.DescribePageDocumentsResponseBodyMore()
            self.more = temp_model.from_map(m.get('More'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePageDocumentsResponseBodyMore(DaraModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class DescribePageDocumentsResponseBodyDocs(DaraModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

