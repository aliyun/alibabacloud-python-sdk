# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceMembersResponseBody(DaraModel):
    def __init__(
        self,
        members: List[main_models.DescribeInstanceMembersResponseBodyMembers] = None,
        page_info: main_models.DescribeInstanceMembersResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The information about the member.
        self.members = members
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.members:
            for v1 in self.members:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Members'] = []
        if self.members is not None:
            for k1 in self.members:
                result['Members'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k1 in m.get('Members'):
                temp_model = main_models.DescribeInstanceMembersResponseBodyMembers()
                self.members.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeInstanceMembersResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceMembersResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of the members.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstanceMembersResponseBodyMembers(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        member_desc: str = None,
        member_display_name: str = None,
        member_status: str = None,
        member_uid: int = None,
        modify_time: int = None,
    ):
        # The time when the member was added to Cloud Firewall. The value is a timestamp. Unit: seconds.
        self.create_time = create_time
        # The remarks of the member.
        self.member_desc = member_desc
        # The name of the member.
        self.member_display_name = member_display_name
        # The status of the member. Valid values:
        # 
        # *   **normal**
        # *   **deleting**
        self.member_status = member_status
        # The UID of the member.
        self.member_uid = member_uid
        # The time when the member was last modified. The value is a timestamp. Unit: seconds.
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.member_desc is not None:
            result['MemberDesc'] = self.member_desc

        if self.member_display_name is not None:
            result['MemberDisplayName'] = self.member_display_name

        if self.member_status is not None:
            result['MemberStatus'] = self.member_status

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('MemberDesc') is not None:
            self.member_desc = m.get('MemberDesc')

        if m.get('MemberDisplayName') is not None:
            self.member_display_name = m.get('MemberDisplayName')

        if m.get('MemberStatus') is not None:
            self.member_status = m.get('MemberStatus')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        return self

