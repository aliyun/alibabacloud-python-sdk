# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTextbookAssistantArticlesRequest(DaraModel):
    def __init__(
        self,
        auth_token: str = None,
        directory_id: str = None,
    ):
        # This parameter is required.
        self.auth_token = auth_token
        # This parameter is required.
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_token is not None:
            result['authToken'] = self.auth_token

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        return self

