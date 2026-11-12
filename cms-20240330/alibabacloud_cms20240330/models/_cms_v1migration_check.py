# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CmsV1MigrationCheck(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The check result code, where NAME_ indicates a naming issue and UNSUPPORTED_ indicates an unsupported resource.
        self.code = code
        # The check result description.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

