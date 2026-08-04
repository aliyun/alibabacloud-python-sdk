# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class MobileRecommendResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[main_models.MobileRecommendResponseBodyResult] = None,
    ):
        # Return code of the invocation
        self.code = code
        # If an error occurs, the error message will be output.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Request result.
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.MobileRecommendResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class MobileRecommendResponseBodyResult(DaraModel):
    def __init__(
        self,
        authors: List[str] = None,
        cover: str = None,
        raw_id: str = None,
        source: str = None,
        title: str = None,
    ):
        # Author information
        self.authors = authors
        # Album thumbnail image
        self.cover = cover
        # Third-party ID of the content
        self.raw_id = raw_id
        # Source of the content
        self.source = source
        # Content title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authors is not None:
            result['Authors'] = self.authors

        if self.cover is not None:
            result['Cover'] = self.cover

        if self.raw_id is not None:
            result['RawId'] = self.raw_id

        if self.source is not None:
            result['Source'] = self.source

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authors') is not None:
            self.authors = m.get('Authors')

        if m.get('Cover') is not None:
            self.cover = m.get('Cover')

        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

