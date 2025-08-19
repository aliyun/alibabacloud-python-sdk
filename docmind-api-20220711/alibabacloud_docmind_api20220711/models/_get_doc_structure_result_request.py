# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDocStructureResultRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        image_strategy: str = None,
        reveal_markdown: bool = None,
        use_url_response_body: bool = None,
    ):
        self.id = id
        self.image_strategy = image_strategy
        self.reveal_markdown = reveal_markdown
        self.use_url_response_body = use_url_response_body

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.image_strategy is not None:
            result['ImageStrategy'] = self.image_strategy

        if self.reveal_markdown is not None:
            result['RevealMarkdown'] = self.reveal_markdown

        if self.use_url_response_body is not None:
            result['UseUrlResponseBody'] = self.use_url_response_body

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ImageStrategy') is not None:
            self.image_strategy = m.get('ImageStrategy')

        if m.get('RevealMarkdown') is not None:
            self.reveal_markdown = m.get('RevealMarkdown')

        if m.get('UseUrlResponseBody') is not None:
            self.use_url_response_body = m.get('UseUrlResponseBody')

        return self

