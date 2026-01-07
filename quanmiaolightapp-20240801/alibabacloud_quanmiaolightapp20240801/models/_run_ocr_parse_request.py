# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunOcrParseRequest(DaraModel):
    def __init__(
        self,
        file_key: str = None,
        model_id: str = None,
        url: str = None,
    ):
        self.file_key = file_key
        self.model_id = model_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_key is not None:
            result['fileKey'] = self.file_key

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileKey') is not None:
            self.file_key = m.get('fileKey')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

