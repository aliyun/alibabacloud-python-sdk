# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWaitingRoomPreviewPageRequest(DaraModel):
    def __init__(
        self,
        custom_page_html: str = None,
    ):
        # The custom waiting room page content. This parameter is required when the waiting room type is custom. The content must be URL-encoded.
        # 
        # This parameter is required.
        self.custom_page_html = custom_page_html

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_page_html is not None:
            result['CustomPageHtml'] = self.custom_page_html

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomPageHtml') is not None:
            self.custom_page_html = m.get('CustomPageHtml')

        return self

