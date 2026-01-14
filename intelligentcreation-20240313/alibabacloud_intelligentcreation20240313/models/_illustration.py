# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Illustration(DaraModel):
    def __init__(
        self,
        illustration_id: int = None,
        oss: str = None,
    ):
        self.illustration_id = illustration_id
        self.oss = oss

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.illustration_id is not None:
            result['illustrationId'] = self.illustration_id

        if self.oss is not None:
            result['oss'] = self.oss

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('illustrationId') is not None:
            self.illustration_id = m.get('illustrationId')

        if m.get('oss') is not None:
            self.oss = m.get('oss')

        return self

