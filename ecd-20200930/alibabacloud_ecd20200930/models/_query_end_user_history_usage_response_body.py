# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class QueryEndUserHistoryUsageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        user_usage_info_list: List[main_models.QueryEndUserHistoryUsageResponseBodyUserUsageInfoList] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The total number of users that meet the query conditions.
        self.total_count = total_count
        # The list of user usage duration entries on the current page.
        self.user_usage_info_list = user_usage_info_list

    def validate(self):
        if self.user_usage_info_list:
            for v1 in self.user_usage_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['UserUsageInfoList'] = []
        if self.user_usage_info_list is not None:
            for k1 in self.user_usage_info_list:
                result['UserUsageInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.user_usage_info_list = []
        if m.get('UserUsageInfoList') is not None:
            for k1 in m.get('UserUsageInfoList'):
                temp_model = main_models.QueryEndUserHistoryUsageResponseBodyUserUsageInfoList()
                self.user_usage_info_list.append(temp_model.from_map(k1))

        return self

class QueryEndUserHistoryUsageResponseBodyUserUsageInfoList(DaraModel):
    def __init__(
        self,
        description: str = None,
        desktop_usage_list: List[main_models.QueryEndUserHistoryUsageResponseBodyUserUsageInfoListDesktopUsageList] = None,
        display_name: str = None,
        duration: int = None,
        end_user_id: str = None,
        end_user_name: str = None,
        org_path_list: List[str] = None,
        user_group_list: List[main_models.QueryEndUserHistoryUsageResponseBodyUserUsageInfoListUserGroupList] = None,
    ):
        # The remarks of the user. This parameter has a value only for convenience account users.
        self.description = description
        # The list of usage duration details for each desktop.
        self.desktop_usage_list = desktop_usage_list
        # The display name of the user. For convenience account users, this is the actual nickname. For AD users, this is the display name.
        self.display_name = display_name
        # The total usage duration, in seconds.
        self.duration = duration
        # The end user ID.
        self.end_user_id = end_user_id
        # The username. For convenience account users, this is the nickname. For AD users, this is the UserPrincipalName.
        self.end_user_name = end_user_name
        # The list of organization paths. For convenience account users, this contains multiple organization paths. For AD users, this is the organizational unit (OU) path.
        self.org_path_list = org_path_list
        # The list of user groups. This parameter has a value only for convenience account users.
        self.user_group_list = user_group_list

    def validate(self):
        if self.desktop_usage_list:
            for v1 in self.desktop_usage_list:
                 if v1:
                    v1.validate()
        if self.user_group_list:
            for v1 in self.user_group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        result['DesktopUsageList'] = []
        if self.desktop_usage_list is not None:
            for k1 in self.desktop_usage_list:
                result['DesktopUsageList'].append(k1.to_map() if k1 else None)

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.end_user_name is not None:
            result['EndUserName'] = self.end_user_name

        if self.org_path_list is not None:
            result['OrgPathList'] = self.org_path_list

        result['UserGroupList'] = []
        if self.user_group_list is not None:
            for k1 in self.user_group_list:
                result['UserGroupList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.desktop_usage_list = []
        if m.get('DesktopUsageList') is not None:
            for k1 in m.get('DesktopUsageList'):
                temp_model = main_models.QueryEndUserHistoryUsageResponseBodyUserUsageInfoListDesktopUsageList()
                self.desktop_usage_list.append(temp_model.from_map(k1))

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('EndUserName') is not None:
            self.end_user_name = m.get('EndUserName')

        if m.get('OrgPathList') is not None:
            self.org_path_list = m.get('OrgPathList')

        self.user_group_list = []
        if m.get('UserGroupList') is not None:
            for k1 in m.get('UserGroupList'):
                temp_model = main_models.QueryEndUserHistoryUsageResponseBodyUserUsageInfoListUserGroupList()
                self.user_group_list.append(temp_model.from_map(k1))

        return self

class QueryEndUserHistoryUsageResponseBodyUserUsageInfoListUserGroupList(DaraModel):
    def __init__(
        self,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        # The user group ID.
        self.user_group_id = user_group_id
        # The user group name.
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')

        return self

class QueryEndUserHistoryUsageResponseBodyUserUsageInfoListDesktopUsageList(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        desktop_name: str = None,
        duration: int = None,
    ):
        # The desktop ID.
        self.desktop_id = desktop_id
        # The desktop name.
        self.desktop_name = desktop_name
        # The usage duration of the user on the desktop, in seconds.
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.duration is not None:
            result['Duration'] = self.duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        return self

