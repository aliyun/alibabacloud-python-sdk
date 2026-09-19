# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class CreateTemplateCacheResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        template_cache: main_models.PublicTemplateCache = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.template_cache = template_cache

    def validate(self):
        if self.template_cache:
            self.template_cache.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.template_cache is not None:
            result['templateCache'] = self.template_cache.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('templateCache') is not None:
            temp_model = main_models.PublicTemplateCache()
            self.template_cache = temp_model.from_map(m.get('templateCache'))

        return self

