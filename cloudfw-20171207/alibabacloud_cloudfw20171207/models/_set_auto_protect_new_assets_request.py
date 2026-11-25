# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetAutoProtectNewAssetsRequest(DaraModel):
    def __init__(
        self,
        auto_protect: bool = None,
        lang: str = None,
    ):
        # Specifies whether to enable automatic traffic redirection. Valid values:
        # - **true**: Enabled.
        # - **false**: Disabled.
        # 
        # This parameter is required.
        self.auto_protect = auto_protect
        # The language type. Valid values:
        # - **zh**: Chinese. Default value.
        # - **en**: English.
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_protect is not None:
            result['AutoProtect'] = self.auto_protect

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoProtect') is not None:
            self.auto_protect = m.get('AutoProtect')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

