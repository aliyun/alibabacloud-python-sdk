# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteCloudVendorAccountAKRequest(DaraModel):
    def __init__(
        self,
        auth_id: int = None,
        auth_modules: List[str] = None,
    ):
        # The unique ID of the AccessKey pair.
        # 
        # This parameter is required.
        self.auth_id = auth_id
        # The modules that are associated with the AccessKey pair.
        self.auth_modules = auth_modules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_id is not None:
            result['AuthId'] = self.auth_id

        if self.auth_modules is not None:
            result['AuthModules'] = self.auth_modules

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthId') is not None:
            self.auth_id = m.get('AuthId')

        if m.get('AuthModules') is not None:
            self.auth_modules = m.get('AuthModules')

        return self

