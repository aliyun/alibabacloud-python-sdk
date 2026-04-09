# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshLoginTokenRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_type: str = None,
        end_user_id: str = None,
        login_identifier: str = None,
        login_token: str = None,
        office_site_id: str = None,
        profile_region: str = None,
        session_id: str = None,
        uuid: str = None,
    ):
        # This parameter is required.
        self.client_id = client_id
        self.client_type = client_type
        self.end_user_id = end_user_id
        self.login_identifier = login_identifier
        # This parameter is required.
        self.login_token = login_token
        self.office_site_id = office_site_id
        self.profile_region = profile_region
        # This parameter is required.
        self.session_id = session_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.login_identifier is not None:
            result['LoginIdentifier'] = self.login_identifier

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.profile_region is not None:
            result['ProfileRegion'] = self.profile_region

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('LoginIdentifier') is not None:
            self.login_identifier = m.get('LoginIdentifier')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('ProfileRegion') is not None:
            self.profile_region = m.get('ProfileRegion')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

