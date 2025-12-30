# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTemplateMaterialsResponseBody(DaraModel):
    def __init__(
        self,
        material_urls: str = None,
        request_id: str = None,
    ):
        # The URLs of the associated materials.
        self.material_urls = material_urls
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.material_urls is not None:
            result['MaterialUrls'] = self.material_urls

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialUrls') is not None:
            self.material_urls = m.get('MaterialUrls')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

