# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListUsersRequest(DaraModel):
    def __init__(
        self,
        display_name_starts_with: str = None,
        email: str = None,
        instance_id: str = None,
        organizational_unit_id: str = None,
        page_number: int = None,
        page_size: int = None,
        phone_number: str = None,
        phone_region: str = None,
        status: str = None,
        user_external_id: str = None,
        user_ids: List[str] = None,
        user_source_id: str = None,
        user_source_type: str = None,
        username_starts_with: str = None,
    ):
        # Displayname
        self.display_name_starts_with = display_name_starts_with
        # The email address of the user who owns the account.
        self.email = email
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the organizational unit.
        self.organizational_unit_id = organizational_unit_id
        # The number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 20.
        self.page_size = page_size
        # The mobile number of the user who owns the account.
        self.phone_number = phone_number
        # The country code of the mobile number. For example, the country code of China is 86 without 00 or +.
        self.phone_region = phone_region
        # The status of the account. Valid values:
        # 
        # *   enabled: The account is enabled.
        # *   disabled: The account is disabled.
        self.status = status
        # The external ID of the account. The external ID can be used by external data to map the data of the account in IDaaS EIAM.
        # 
        # For accounts with the same source type and source ID, each account has a unique external ID.
        self.user_external_id = user_external_id
        # User ID set
        self.user_ids = user_ids
        # The source ID of the account.
        # 
        # If the account was created in IDaaS, its source ID is the ID of the IDaaS instance. If the account was imported, its source ID is the enterprise ID in the source. For example, if the account was imported from DingTalk, its source ID is the corpId value of the enterprise in DingTalk.
        self.user_source_id = user_source_id
        # The source type of the account. Valid values:
        # 
        # *   build_in: The account was created in IDaaS.
        # *   ding_talk: The account was imported from DingTalk.
        # *   ad: The account was imported from Microsoft Active Directory (AD).
        # *   ldap: The account was imported from a Lightweight Directory Access Protocol (LDAP) service.
        self.user_source_type = user_source_type
        # Username
        self.username_starts_with = username_starts_with

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name_starts_with is not None:
            result['DisplayNameStartsWith'] = self.display_name_starts_with

        if self.email is not None:
            result['Email'] = self.email

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.phone_region is not None:
            result['PhoneRegion'] = self.phone_region

        if self.status is not None:
            result['Status'] = self.status

        if self.user_external_id is not None:
            result['UserExternalId'] = self.user_external_id

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        if self.user_source_id is not None:
            result['UserSourceId'] = self.user_source_id

        if self.user_source_type is not None:
            result['UserSourceType'] = self.user_source_type

        if self.username_starts_with is not None:
            result['UsernameStartsWith'] = self.username_starts_with

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayNameStartsWith') is not None:
            self.display_name_starts_with = m.get('DisplayNameStartsWith')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('PhoneRegion') is not None:
            self.phone_region = m.get('PhoneRegion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserExternalId') is not None:
            self.user_external_id = m.get('UserExternalId')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        if m.get('UserSourceId') is not None:
            self.user_source_id = m.get('UserSourceId')

        if m.get('UserSourceType') is not None:
            self.user_source_type = m.get('UserSourceType')

        if m.get('UsernameStartsWith') is not None:
            self.username_starts_with = m.get('UsernameStartsWith')

        return self

