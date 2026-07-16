# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRegistrantProfileRealNameVerificationInfoRequest(DaraModel):
    def __init__(
        self,
        fetch_image: bool = None,
        lang: str = None,
        registrant_profile_id: int = None,
        user_client_ip: str = None,
    ):
        self.fetch_image = fetch_image
        self.lang = lang
        # This parameter is required.
        self.registrant_profile_id = registrant_profile_id
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fetch_image is not None:
            result['FetchImage'] = self.fetch_image

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FetchImage') is not None:
            self.fetch_image = m.get('FetchImage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

