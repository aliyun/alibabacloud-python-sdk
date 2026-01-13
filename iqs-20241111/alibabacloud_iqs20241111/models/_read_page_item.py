# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReadPageItem(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        html: str = None,
        markdown: str = None,
        raw_html: str = None,
        screenshot: str = None,
        status_code: int = None,
        text: str = None,
    ):
        self.error_message = error_message
        self.html = html
        self.markdown = markdown
        self.raw_html = raw_html
        self.screenshot = screenshot
        self.status_code = status_code
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.html is not None:
            result['html'] = self.html

        if self.markdown is not None:
            result['markdown'] = self.markdown

        if self.raw_html is not None:
            result['rawHtml'] = self.raw_html

        if self.screenshot is not None:
            result['screenshot'] = self.screenshot

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('html') is not None:
            self.html = m.get('html')

        if m.get('markdown') is not None:
            self.markdown = m.get('markdown')

        if m.get('rawHtml') is not None:
            self.raw_html = m.get('rawHtml')

        if m.get('screenshot') is not None:
            self.screenshot = m.get('screenshot')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

