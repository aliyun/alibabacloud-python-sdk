# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class DescribeGroupUserResponseBody(DaraModel):
    def __init__(
        self,
        groups: List[main_models.DescribeGroupUserResponseBodyGroups] = None,
        next_token: str = None,
        request_id: str = None,
        users: List[main_models.DescribeGroupUserResponseBodyUsers] = None,
    ):
        # >  This field is deprecated.
        self.groups = groups
        # The token for the next query. If NextToken is empty, all results have been queried.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The members.
        self.users = users

    def validate(self):
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()
        if self.users:
            for v1 in self.users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['Groups'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.DescribeGroupUserResponseBodyGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.DescribeGroupUserResponseBodyUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class DescribeGroupUserResponseBodyUsers(DaraModel):
    def __init__(
        self,
        address: str = None,
        avatar: str = None,
        email: str = None,
        end_user_id: str = None,
        gmt_created: str = None,
        gmt_join_group: str = None,
        job_number: str = None,
        nick_name: str = None,
        phone: str = None,
        remark: str = None,
    ):
        # >  This field is deprecated.
        self.address = address
        # >  This field is deprecated.
        self.avatar = avatar
        # The email address.
        self.email = email
        # The user name.
        self.end_user_id = end_user_id
        # The time when the user was created.
        self.gmt_created = gmt_created
        # The time when the user was added to the user group.
        self.gmt_join_group = gmt_join_group
        # >  This field is deprecated.
        self.job_number = job_number
        # The display name.
        self.nick_name = nick_name
        # The mobile number.
        self.phone = phone
        # The remarks on the user.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.avatar is not None:
            result['Avatar'] = self.avatar

        if self.email is not None:
            result['Email'] = self.email

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_join_group is not None:
            result['GmtJoinGroup'] = self.gmt_join_group

        if self.job_number is not None:
            result['JobNumber'] = self.job_number

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtJoinGroup') is not None:
            self.gmt_join_group = m.get('GmtJoinGroup')

        if m.get('JobNumber') is not None:
            self.job_number = m.get('JobNumber')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

class DescribeGroupUserResponseBodyGroups(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
        user_count: str = None,
    ):
        # The user group ID.
        self.group_id = group_id
        # The name of the user group.
        self.group_name = group_name
        # The number of members in the user group.
        self.user_count = user_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.user_count is not None:
            result['UserCount'] = self.user_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')

        return self

