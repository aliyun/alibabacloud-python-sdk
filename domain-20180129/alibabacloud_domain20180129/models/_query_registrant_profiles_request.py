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
        remark: str = None,
        user_client_ip: str = None,
        zh_registrant_organization: str = None,
    ):
        # Specifies whether to query the default profile. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # Default value: **false**.
        self.default_registrant_profile = default_registrant_profile
        # The email address of the domain name registrant.
        self.email = email
        # The language of the error message to return if the request fails. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        # 
        # Default value: **en**.
        self.lang = lang
        # The number of the page to return. Default value: **0**.
        self.page_num = page_num
        # The number of entries per page. Default value: **0**. Maximum value: **5000**.
        self.page_size = page_size
        # The state of real-name verification for the domain name registrant. Valid values:
        # 
        # *   **FAILED**: Real-name verification for the domain name fails.
        # *   **SUCCEED**: Real-name verification for the domain name is successful.
        # *   **NONAUDIT**: Real-name verification for the domain name is not performed.
        # *   **AUDITING**: Real-name verification for the domain name is in progress.
        self.real_name_status = real_name_status
        # The name of the domain name registrant.
        self.registrant_organization = registrant_organization
        # The ID of the registrant profile that you want to query. The system generates an ID after you create a registrant profile.
        self.registrant_profile_id = registrant_profile_id
        # The type of the registrant profile. Valid values:
        # 
        # *   **common**: common profile.
        # *   **cnnic**: China Internet Network Information Center (CNNIC) profile.
        # 
        # >  Only the Alibaba Cloud international site (alibabacloud.com) supports CNNIC profiles. To register domain names provided by CNNIC such as the .cn and . domain names on the Alibaba Cloud international site, you must use a CNNIC profile. To register other domain names, use a common profile.
        self.registrant_profile_type = registrant_profile_type
        # The type of the domain name registrant. Valid values:
        # 
        # *   **1**: individual.
        # *   **2**: enterprise.
        # 
        # Default value: **1**.
        self.registrant_type = registrant_type
        # The remarks.
        self.remark = remark
        # The IP address of the client. Set the value to 127.0.0.1.
        self.user_client_ip = user_client_ip
        # The Chinese name of the domain name registrant.
        self.zh_registrant_organization = zh_registrant_organization

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

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        if self.zh_registrant_organization is not None:
            result['ZhRegistrantOrganization'] = self.zh_registrant_organization

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

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        if m.get('ZhRegistrantOrganization') is not None:
            self.zh_registrant_organization = m.get('ZhRegistrantOrganization')

        return self

