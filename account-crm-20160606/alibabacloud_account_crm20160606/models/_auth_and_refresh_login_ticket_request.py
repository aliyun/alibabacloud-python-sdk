# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuthAndRefreshLoginTicketRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        havana_id: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.havana_id = havana_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.havana_id is not None:
            result['HavanaId'] = self.havana_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('HavanaId') is not None:
            self.havana_id = m.get('HavanaId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

