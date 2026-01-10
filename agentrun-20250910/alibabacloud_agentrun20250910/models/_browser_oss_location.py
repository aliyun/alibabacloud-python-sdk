# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BrowserOssLocation(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        prefix: str = None,
    ):
        self.bucket = bucket
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['bucket'] = self.bucket

        if self.prefix is not None:
            result['prefix'] = self.prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')

        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')

        return self

