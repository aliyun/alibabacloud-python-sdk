# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePackageRequest(DaraModel):
    def __init__(
        self,
        body: str = None,
        is_install: bool = None,
    ):
        # The request body parameters.
        self.body = body
        # Specifies whether to install the package.
        self.is_install = is_install

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        if self.is_install is not None:
            result['isInstall'] = self.is_install

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('isInstall') is not None:
            self.is_install = m.get('isInstall')

        return self

