# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListAuthorizedUsersResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        users: List[main_models.ListAuthorizedUsersResponseBodyUsers] = None,
    ):
        # The current page number.
        self.page_number = page_number
        # The number of records per page in this request.
        self.page_size = page_size
        # The request ID, which is used to locate this call.
        self.request_id = request_id
        # The total number of authorization records that match the query conditions.
        self.total_count = total_count
        # The list of authorized users on the current page. An empty list is returned if no authorization records are matched.
        self.users = users

    def validate(self):
        if self.users:
            for v1 in self.users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.ListAuthorizedUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class ListAuthorizedUsersResponseBodyUsers(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        app_id: str = None,
        app_instance_group_id: str = None,
        app_instance_group_set_id: str = None,
        app_instance_persistent_ids: List[str] = None,
        auth_mode: str = None,
        email: str = None,
        end_user_id: str = None,
        is_auth_all_apps: str = None,
        phone: str = None,
    ):
        # The user account type.
        # 
        # - `simple`: convenience account.
        # - `ad`: Active Directory (AD) domain account.
        self.account_type = account_type
        # The application ID specified in this query. This field is not returned if no application filter condition is specified.
        self.app_id = app_id
        # The delivery group ID to which the authorization relationship belongs. When querying cloud browsers, this is the browser group ID. When querying by set, this field is the primary delivery group ID of the set.
        self.app_instance_group_id = app_instance_group_id
        # The delivery group set ID of this query. This field is returned when querying by set.
        self.app_instance_group_set_id = app_instance_group_set_id
        # The list of persistent session IDs authorized to the user. This field is returned when the authorization mode is `Session`.
        self.app_instance_persistent_ids = app_instance_persistent_ids
        # The authorization mode of the delivery group. Valid values:
        # 
        # - `App`: Authorization by application.
        # - `Session`: Authorization by persistent session.
        # - `AppInstanceGroup`: Authorization by delivery group.
        self.auth_mode = auth_mode
        # The email address of the user. This field may not be returned if the email address is not available.
        self.email = email
        # The authorized username.
        self.end_user_id = end_user_id
        # Indicates whether the query is not restricted to a specific application. Valid values:
        # 
        # - `true`: No application filter condition is specified.
        # - `false`: An application filter condition is specified.
        # 
        # This field is determined by the query conditions and cannot be used alone to determine whether the user is authorized for all applications.
        self.is_auth_all_apps = is_auth_all_apps
        # The phone number of the user. This field may not be returned if the phone number is not available.
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_group_set_id is not None:
            result['AppInstanceGroupSetId'] = self.app_instance_group_set_id

        if self.app_instance_persistent_ids is not None:
            result['AppInstancePersistentIds'] = self.app_instance_persistent_ids

        if self.auth_mode is not None:
            result['AuthMode'] = self.auth_mode

        if self.email is not None:
            result['Email'] = self.email

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.is_auth_all_apps is not None:
            result['IsAuthAllApps'] = self.is_auth_all_apps

        if self.phone is not None:
            result['Phone'] = self.phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupSetId') is not None:
            self.app_instance_group_set_id = m.get('AppInstanceGroupSetId')

        if m.get('AppInstancePersistentIds') is not None:
            self.app_instance_persistent_ids = m.get('AppInstancePersistentIds')

        if m.get('AuthMode') is not None:
            self.auth_mode = m.get('AuthMode')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('IsAuthAllApps') is not None:
            self.is_auth_all_apps = m.get('IsAuthAllApps')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        return self

