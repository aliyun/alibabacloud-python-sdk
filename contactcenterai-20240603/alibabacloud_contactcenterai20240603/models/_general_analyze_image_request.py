# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GeneralAnalyzeImageRequest(DaraModel):
    def __init__(
        self,
        custom_prompt: str = None,
        image_urls: List[str] = None,
        stream: bool = None,
        template_ids: List[int] = None,
    ):
        self.custom_prompt = custom_prompt
        # This parameter is required.
        self.image_urls = image_urls
        self.stream = stream
        self.template_ids = template_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_prompt is not None:
            result['customPrompt'] = self.custom_prompt

        if self.image_urls is not None:
            result['imageUrls'] = self.image_urls

        if self.stream is not None:
            result['stream'] = self.stream

        if self.template_ids is not None:
            result['templateIds'] = self.template_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customPrompt') is not None:
            self.custom_prompt = m.get('customPrompt')

        if m.get('imageUrls') is not None:
            self.image_urls = m.get('imageUrls')

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        if m.get('templateIds') is not None:
            self.template_ids = m.get('templateIds')

        return self

