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
        # The current page number, which is the same as the PageNumber request parameter.
        self.page_number = page_number
        # The number of records per page, which is the same as the PageSize request parameter.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records that match the query conditions. Use this value to determine whether to continue paging.
        # 
        # - When the authorization mode is `App` or `AppInstanceGroup`, this is the number of authorization records. If the same user has multiple authorization records, the user is counted multiple times. Therefore, this value may be greater than the actual number of users.
        # - When the authorization mode is `Session`, this is the deduplicated user count.
        self.total_count = total_count
        # The list of authorized users on the current page. Multiple authorization records for the same user are merged into a single entry. An empty list is returned if no authorized users match the conditions.
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
        # The account type of the user. Valid values:
        # 
        # - simple: Convenience account.
        # - ad: Active Directory (AD) domain account, which originates from an enterprise AD domain.
        self.account_type = account_type
        # The application ID. Returned only when AppId is specified in the request. The value is the same as the request parameter. Not returned if AppId is not specified or when querying by delivery group set.
        self.app_id = app_id
        # The delivery group ID associated with the user\\"s authorization relationship. When querying by delivery group, this value is the same as the request parameter. When querying by delivery group set, this value is the primary delivery group ID of the set.
        self.app_instance_group_id = app_instance_group_id
        # The delivery group set ID. Returned only when querying by delivery group set. The value is the same as the AppInstanceGroupSetId request parameter.
        self.app_instance_group_set_id = app_instance_group_set_id
        # The list of persistent session IDs granted to the user. Returned only when the delivery group authorization mode (AuthMode) is `Session`. This list is not affected by the AppInstancePersistentId request parameter and always includes all persistent sessions granted to the user.
        self.app_instance_persistent_ids = app_instance_persistent_ids
        # The authorization mode of the delivery group, which determines the scope of results returned by this operation. Valid values:
        # 
        # - App: Application-level authorization. Applications within the delivery group are authorized to users without restricting which sessions the users can use.
        # - Session: Session-level authorization. Persistent sessions within the delivery group are authorized to users without restricting which applications the users can use. In this case, AppInstancePersistentIds returns the persistent sessions granted to the user.
        # - AppInstanceGroup: Delivery group-level authorization. The entire delivery group is authorized to users, allowing them to open any application using any session within the delivery group.
        # 
        # When querying by delivery group set, the authorization mode of the primary delivery group in the set is returned.
        self.auth_mode = auth_mode
        # The email address of the user. Returned only when the account information of the user can be retrieved.
        self.email = email
        # The username. To remove authorization, pass this value to the UnAuthorizeUserIds parameter of the [AuthorizeInstanceGroup](~~AuthorizeInstanceGroup~~) or [AuthorizeUsersForApp](~~AuthorizeUsersForApp~~) operation.
        self.end_user_id = end_user_id
        # Indicates whether the query is not restricted to a specific application. Valid values:
        # 
        # - true: AppId is not specified in the request. All authorized users under the delivery group are returned.
        # - false: AppId is specified in the request. Only users authorized for that specific application are returned.
        # 
        # > This field is determined by whether the AppId request parameter is specified. It does not reflect the actual scope of applications authorized to the user and cannot be used to determine whether the user is authorized for all applications.
        self.is_auth_all_apps = is_auth_all_apps
        # The phone number of the user. Returned only when the account information of the user can be retrieved.
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

