# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_qweneduaisuite20261102 import models as main_models
from darabonba.model import DaraModel

class CreateEduProblemSolveRequest(DaraModel):
    def __init__(
        self,
        query: main_models.CreateEduProblemSolveRequestQuery = None,
        request_id: str = None,
    ):
        # **The question image container.**
        self.query = query
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.query:
            self.query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query is not None:
            result['query'] = self.query.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('query') is not None:
            temp_model = main_models.CreateEduProblemSolveRequestQuery()
            self.query = temp_model.from_map(m.get('query'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class CreateEduProblemSolveRequestQuery(DaraModel):
    def __init__(
        self,
        image: main_models.CreateEduProblemSolveRequestQueryImage = None,
    ):
        # **The image information.**
        self.image = image

    def validate(self):
        if self.image:
            self.image.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image is not None:
            result['image'] = self.image.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            temp_model = main_models.CreateEduProblemSolveRequestQueryImage()
            self.image = temp_model.from_map(m.get('image'))

        return self

class CreateEduProblemSolveRequestQueryImage(DaraModel):
    def __init__(
        self,
        base_64: str = None,
        format: str = None,
        url: str = None,
    ):
        # **The Base64-encoded image**. If both this parameter and the URL are provided, this parameter takes precedence.
        self.base_64 = base_64
        # **The image format**: jpg, jpeg, or png. The value must match the actual file format.
        # 
        # This parameter is required.
        self.format = format
        # The URL of a single question image.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_64 is not None:
            result['base64'] = self.base_64

        if self.format is not None:
            result['format'] = self.format

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('base64') is not None:
            self.base_64 = m.get('base64')

        if m.get('format') is not None:
            self.format = m.get('format')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

