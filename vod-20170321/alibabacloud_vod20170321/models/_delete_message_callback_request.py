# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMessageCallbackRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        owner_account: str = None,
    ):
        # The ID of the application. If you do not set this parameter, the default value **app-1000000** is used.
        self.app_id = app_id
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        return self

