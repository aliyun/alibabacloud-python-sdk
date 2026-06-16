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
        max_results: int = None,
        next_token: str = None,
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
        # The prefix of the display name. The query is performed based on the prefix.
        self.display_name_starts_with = display_name_starts_with
        # The email address of the user.
        self.email = email
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of entries per page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the organizational unit.
        self.organizational_unit_id = organizational_unit_id
        # The page number. The default value is 1.
        self.page_number = page_number
        # The number of entries per page. The default value is 20. The maximum value is 100.
        self.page_size = page_size
        # The mobile number of the user.
        self.phone_number = phone_number
        # The country calling code. For example, the country calling code of China is `86`. Do not add `00` or `+` to the country calling code.
        self.phone_region = phone_region
        # The status of the user. Valid values:
        # 
        # - `enabled`: The user is enabled.
        # 
        # - `disabled`: The user is disabled.
        self.status = status
        # The external ID of the user. The external ID can be used to associate the user with a user in an external system.
        # 
        # > The external ID must be unique within the same source type and source ID.
        self.user_external_id = user_external_id
        # The list of user IDs.
        self.user_ids = user_ids
        # The source ID of the user.
        # 
        # If the user is created in EIAM, the value of this parameter is the ID of the EIAM instance. If the user is imported from an external system, the value of this parameter is the enterprise ID of the user in the external system. For example, if the user is imported from DingTalk, the value of this parameter is the `corpId` of the enterprise in DingTalk.
        self.user_source_id = user_source_id
        # The source type of the user. Valid values:
        # 
        # - `build_in`: The user is created in EIAM.
        # 
        # - `ding_talk`: The user is imported from DingTalk.
        # 
        # - `ad`: The user is imported from Active Directory (AD).
        # 
        # - `ldap`: The user is imported from a Lightweight Directory Access Protocol (LDAP) directory.
        # 
        # - `we_com`: The user is imported from WeCom.
        self.user_source_type = user_source_type
        # The prefix of the username. The query is performed based on the prefix.
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

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

