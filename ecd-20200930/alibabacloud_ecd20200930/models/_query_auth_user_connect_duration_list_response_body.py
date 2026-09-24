# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class QueryAuthUserConnectDurationListResponseBody(DaraModel):
    def __init__(
        self,
        auth_user_connect_duration_list: List[main_models.QueryAuthUserConnectDurationListResponseBodyAuthUserConnectDurationList] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The connection duration list of authorized users.
        self.auth_user_connect_duration_list = auth_user_connect_duration_list
        # The pagination token for the next page. This parameter is returned when the results span multiple pages. Pass this value as the NextToken in the next request to retrieve the next page. This parameter is returned only when statistics are collected by individual session details.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of records that match the specified conditions.
        self.total_count = total_count

    def validate(self):
        if self.auth_user_connect_duration_list:
            for v1 in self.auth_user_connect_duration_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthUserConnectDurationList'] = []
        if self.auth_user_connect_duration_list is not None:
            for k1 in self.auth_user_connect_duration_list:
                result['AuthUserConnectDurationList'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auth_user_connect_duration_list = []
        if m.get('AuthUserConnectDurationList') is not None:
            for k1 in m.get('AuthUserConnectDurationList'):
                temp_model = main_models.QueryAuthUserConnectDurationListResponseBodyAuthUserConnectDurationList()
                self.auth_user_connect_duration_list.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryAuthUserConnectDurationListResponseBodyAuthUserConnectDurationList(DaraModel):
    def __init__(
        self,
        connect_duration: int = None,
        connect_end_time: str = None,
        connect_start_time: str = None,
        description: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        directory_type: int = None,
        display_name: str = None,
        display_name_new: str = None,
        domain_name: str = None,
        end_user_id: str = None,
        nick_name: str = None,
        region_id: str = None,
        user_principal_name: str = None,
    ):
        # The connection duration of the user, in seconds.
        self.connect_duration = connect_duration
        # The end time of the connection, as a UNIX timestamp in milliseconds. This parameter is returned only when statistics are collected by individual session details (StatisticType=SingleSession).
        self.connect_end_time = connect_end_time
        # The start time of the connection, as a UNIX timestamp in milliseconds. This parameter is returned only when statistics are collected by individual session details (StatisticType=SingleSession).
        self.connect_start_time = connect_start_time
        # The remarks of the user. This parameter is returned only for convenience users when WithDetail is set to true.
        self.description = description
        # The cloud desktop ID.
        self.desktop_id = desktop_id
        # The cloud desktop name.
        self.desktop_name = desktop_name
        # The type of the directory to which the user belongs. Valid values:
        # 
        # - 1: convenience account.
        # - 2: RAM account.
        # - 3: AD account.
        # - 4: personal edition.
        self.directory_type = directory_type
        # The display name of the user. This parameter is returned only for AD users when WithDetail is set to true.
        self.display_name = display_name
        # The new display name of the user. This parameter is returned only for AD users when WithDetail is set to true.
        self.display_name_new = display_name_new
        # The AD domain name.
        self.domain_name = domain_name
        # The end user ID.
        self.end_user_id = end_user_id
        # The nickname of the user. This parameter is returned only for convenience users when WithDetail is set to true.
        self.nick_name = nick_name
        # The region ID.
        self.region_id = region_id
        # The user principal name (UPN). This parameter is returned only for AD users when WithDetail is set to true.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_duration is not None:
            result['ConnectDuration'] = self.connect_duration

        if self.connect_end_time is not None:
            result['ConnectEndTime'] = self.connect_end_time

        if self.connect_start_time is not None:
            result['ConnectStartTime'] = self.connect_start_time

        if self.description is not None:
            result['Description'] = self.description

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.display_name_new is not None:
            result['DisplayNameNew'] = self.display_name_new

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectDuration') is not None:
            self.connect_duration = m.get('ConnectDuration')

        if m.get('ConnectEndTime') is not None:
            self.connect_end_time = m.get('ConnectEndTime')

        if m.get('ConnectStartTime') is not None:
            self.connect_start_time = m.get('ConnectStartTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('DisplayNameNew') is not None:
            self.display_name_new = m.get('DisplayNameNew')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

