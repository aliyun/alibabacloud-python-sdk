# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFileContentRequest(DaraModel):
    def __init__(
        self,
        file_key: str = None,
    ):
        self.file_key = file_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_key is not None:
            result['fileKey'] = self.file_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileKey') is not None:
            self.file_key = m.get('fileKey')

        return self

