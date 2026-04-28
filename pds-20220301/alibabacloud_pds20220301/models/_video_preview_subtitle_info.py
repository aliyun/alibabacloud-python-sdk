# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VideoPreviewSubtitleInfo(DaraModel):
    def __init__(
        self,
        language: str = None,
        status: str = None,
        url: str = None,
    ):
        # The subtitle language.
        self.language = language
        # The status of the subtitle task.
        # 
        # Valid values:
        # 
        # *   finished
        # *   failed
        self.status = status
        # The subtitle URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['language'] = self.language

        if self.status is not None:
            result['status'] = self.status

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

