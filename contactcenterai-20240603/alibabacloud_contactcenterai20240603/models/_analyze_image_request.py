# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AnalyzeImageRequest(DaraModel):
    def __init__(
        self,
        image_urls: List[str] = None,
        response_format_type: str = None,
        result_types: List[str] = None,
        stream: bool = None,
    ):
        self.image_urls = image_urls
        self.response_format_type = response_format_type
        self.result_types = result_types
        # This parameter is required.
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_urls is not None:
            result['imageUrls'] = self.image_urls

        if self.response_format_type is not None:
            result['responseFormatType'] = self.response_format_type

        if self.result_types is not None:
            result['resultTypes'] = self.result_types

        if self.stream is not None:
            result['stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageUrls') is not None:
            self.image_urls = m.get('imageUrls')

        if m.get('responseFormatType') is not None:
            self.response_format_type = m.get('responseFormatType')

        if m.get('resultTypes') is not None:
            self.result_types = m.get('resultTypes')

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        return self

