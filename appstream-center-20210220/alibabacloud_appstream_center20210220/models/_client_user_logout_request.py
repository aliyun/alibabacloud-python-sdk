# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ClientUserLogoutRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        login_token: str = None,
        office_site_id: str = None,
        profile_region: str = None,
        session_id: str = None,
    ):
        self.client_id = client_id
        self.login_token = login_token
        self.office_site_id = office_site_id
        self.profile_region = profile_region
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.profile_region is not None:
            result['ProfileRegion'] = self.profile_region

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('ProfileRegion') is not None:
            self.profile_region = m.get('ProfileRegion')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

