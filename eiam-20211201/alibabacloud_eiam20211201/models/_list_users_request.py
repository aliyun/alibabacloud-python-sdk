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
        # The display name prefix. A left-match query is used.
        self.display_name_starts_with = display_name_starts_with
        # The email address of the account.
        self.email = email
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of entries per page for paging.
        self.max_results = max_results
        # The pagination token.
        self.next_token = next_token
        # The organizational unit ID.
        self.organizational_unit_id = organizational_unit_id
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20. Maximum value: 100.
        self.page_size = page_size
        # The phone number of the account.
        self.phone_number = phone_number
        # The phone region code. Example: The region code for the Chinese mainland is 86, without the 00 or + prefix.
        self.phone_region = phone_region
        # The account status. Valid values:
        # - enabled: Enabled.
        # - disabled: Disabled.
        self.status = status
        # The external ID, which is used to associate external data with IDaaS accounts.
        # 
        # Note: The external ID must be unique within the same source type and source ID.
        self.user_external_id = user_external_id
        # The list of account IDs.
        self.user_ids = user_ids
        # The source ID of the account.
        # 
        # For self-built accounts, the default value is the instance ID. For other types, the value corresponds to the enterprise ID of the respective source. For example, for a DingTalk source, the value corresponds to the corpId of the DingTalk enterprise.
        self.user_source_id = user_source_id
        # The source type of the account. Valid values:
        # - build_in: self-built.
        # - ding_talk: imported from DingTalk.
        # - ad: imported from AD.
        # - ldap: imported from LDAP.
        # - we_com: imported from WeCom.
        self.user_source_type = user_source_type
        # The username prefix. A left-match query is used.
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

