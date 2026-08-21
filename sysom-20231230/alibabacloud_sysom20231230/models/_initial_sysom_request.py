# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InitialSysomRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        check_only: bool = None,
        source: str = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        # Specifies whether to only check if the service-linked role exists.
        self.check_only = check_only
        # The source. Set this parameter to console.
        self.source = source
        self.x_sysom_invoke_source = x_sysom_invoke_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_debug_id is not None:
            result['X-Debug-Id'] = self.x_debug_id

        if self.check_only is not None:
            result['check_only'] = self.check_only

        if self.source is not None:
            result['source'] = self.source

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('check_only') is not None:
            self.check_only = m.get('check_only')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

