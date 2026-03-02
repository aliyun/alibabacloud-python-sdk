# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAppSecretRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.app_secret_id = app_secret_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')

        return self

