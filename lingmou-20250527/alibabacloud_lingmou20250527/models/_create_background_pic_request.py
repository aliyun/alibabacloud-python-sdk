# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBackgroundPicRequest(DaraModel):
    def __init__(
        self,
        filename: str = None,
        oss_key: str = None,
    ):
        self.filename = filename
        self.oss_key = oss_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filename is not None:
            result['filename'] = self.filename

        if self.oss_key is not None:
            result['ossKey'] = self.oss_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filename') is not None:
            self.filename = m.get('filename')

        if m.get('ossKey') is not None:
            self.oss_key = m.get('ossKey')

        return self

