# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateCLICommandResponseBody(DaraModel):
    def __init__(
        self,
        cli: str = None,
        request_id: str = None,
        unified_cli: str = None,
    ):
        self.cli = cli
        self.request_id = request_id
        self.unified_cli = unified_cli

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cli is not None:
            result['cli'] = self.cli

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.unified_cli is not None:
            result['unifiedCli'] = self.unified_cli

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cli') is not None:
            self.cli = m.get('cli')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('unifiedCli') is not None:
            self.unified_cli = m.get('unifiedCli')

        return self

