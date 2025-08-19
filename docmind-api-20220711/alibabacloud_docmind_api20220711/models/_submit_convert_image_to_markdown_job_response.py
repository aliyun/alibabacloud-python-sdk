# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_docmind_api20220711 import models as main_models
from darabonba.model import DaraModel

class SubmitConvertImageToMarkdownJobResponse(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: main_models.SubmitConvertImageToMarkdownJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        if m.get('body') is not None:
            temp_model = main_models.SubmitConvertImageToMarkdownJobResponseBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

