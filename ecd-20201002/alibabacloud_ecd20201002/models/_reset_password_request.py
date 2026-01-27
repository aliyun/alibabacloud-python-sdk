# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetPasswordRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_token: str = None,
        email: str = None,
        end_user_id: str = None,
        office_site_id: str = None,
        region_id: str = None,
        phone: str = None,
    ):
        # The client ID. The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The email address of the user.
        self.email = email
        # The user ID.
        # 
        # This parameter is required.
        self.end_user_id = end_user_id
        # The office network ID.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The phone number of the user.
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.email is not None:
            result['Email'] = self.email

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.phone is not None:
            result['phone'] = self.phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        return self

