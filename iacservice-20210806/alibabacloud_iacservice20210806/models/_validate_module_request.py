# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ValidateModuleRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        code: str = None,
        code_map: Dict[str, Any] = None,
        source: str = None,
        source_path: str = None,
    ):
        self.client_token = client_token
        self.code = code
        self.code_map = code_map
        self.source = source
        self.source_path = source_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.code is not None:
            result['code'] = self.code

        if self.code_map is not None:
            result['codeMap'] = self.code_map

        if self.source is not None:
            result['source'] = self.source

        if self.source_path is not None:
            result['sourcePath'] = self.source_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('codeMap') is not None:
            self.code_map = m.get('codeMap')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')

        return self

