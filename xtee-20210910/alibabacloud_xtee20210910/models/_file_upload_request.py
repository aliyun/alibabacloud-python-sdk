# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FileUploadRequest(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_url: str = None,
        lang: str = None,
        tab: str = None,
    ):
        # File name.
        self.file_name = file_name
        # File URL
        self.file_url = file_url
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Scenario.
        self.tab = tab

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.tab is not None:
            result['Tab'] = self.tab

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Tab') is not None:
            self.tab = m.get('Tab')

        return self

