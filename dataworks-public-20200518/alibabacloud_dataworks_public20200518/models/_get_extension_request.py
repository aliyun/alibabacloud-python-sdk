# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetExtensionRequest(DaraModel):
    def __init__(
        self,
        extension_code: str = None,
    ):
        # The unique code of the extension.
        # 
        # This parameter is required.
        self.extension_code = extension_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extension_code is not None:
            result['ExtensionCode'] = self.extension_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtensionCode') is not None:
            self.extension_code = m.get('ExtensionCode')

        return self

