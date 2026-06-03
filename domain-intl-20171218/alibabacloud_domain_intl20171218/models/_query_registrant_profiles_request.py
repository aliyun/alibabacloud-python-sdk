# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRegistrantProfilesRequest(DaraModel):
    def __init__(
        self,
        default_registrant_profile: bool = None,
        email: str = None,
        lang: str = None,
        page_num: int = None,
        page_size: int = None,
        real_name_status: str = None,
        registrant_organization: str = None,
        registrant_profile_id: int = None,
        registrant_profile_type: str = None,
        registrant_type: str = None,
        user_client_ip: str = None,
    ):
        self.default_registrant_profile = default_registrant_profile
        self.email = email
        self.lang = lang
        self.page_num = page_num
        self.page_size = page_size
        self.real_name_status = real_name_status
        self.registrant_organization = registrant_organization
        self.registrant_profile_id = registrant_profile_id
        self.registrant_profile_type = registrant_profile_type
        self.registrant_type = registrant_type
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_registrant_profile is not None:
            result['DefaultRegistrantProfile'] = self.default_registrant_profile

        if self.email is not None:
            result['Email'] = self.email

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.real_name_status is not None:
            result['RealNameStatus'] = self.real_name_status

        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization

        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id

        if self.registrant_profile_type is not None:
            result['RegistrantProfileType'] = self.registrant_profile_type

        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultRegistrantProfile') is not None:
            self.default_registrant_profile = m.get('DefaultRegistrantProfile')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RealNameStatus') is not None:
            self.real_name_status = m.get('RealNameStatus')

        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')

        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')

        if m.get('RegistrantProfileType') is not None:
            self.registrant_profile_type = m.get('RegistrantProfileType')

        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

