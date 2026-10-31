# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListUsersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListUsersResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The request error code. OK indicates that the request is successful.
        self.code = code
        # The HTTP status code of the backend response.
        self.http_status_code = http_status_code
        # The request error message.
        self.message = message
        # The paged query result.
        self.page_result = page_result
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListUsersResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListUsersResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        total_count: int = None,
        user_list: List[main_models.ListUsersResponseBodyPageResultUserList] = None,
    ):
        # The total number of records.
        self.total_count = total_count
        # The user list.
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for v1 in self.user_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['UserList'] = []
        if self.user_list is not None:
            for k1 in self.user_list:
                result['UserList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.user_list = []
        if m.get('UserList') is not None:
            for k1 in m.get('UserList'):
                temp_model = main_models.ListUsersResponseBodyPageResultUserList()
                self.user_list.append(temp_model.from_map(k1))

        return self

class ListUsersResponseBodyPageResultUserList(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        deleted: bool = None,
        dept_list: List[main_models.ListUsersResponseBodyPageResultUserListDeptList] = None,
        ding_number: str = None,
        display_name: str = None,
        display_name_without_status: str = None,
        enable_white_ip: bool = None,
        fei_shu_robot: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        id: str = None,
        mail: str = None,
        mobile_phone: str = None,
        name: str = None,
        nick_name: str = None,
        parent_id: str = None,
        real_name: str = None,
        source_id: str = None,
        source_type: str = None,
        we_chat_robot: str = None,
        white_ip: str = None,
    ):
        # The logon name of the original account.
        self.account_name = account_name
        # Indicates whether the user is deleted.
        self.deleted = deleted
        # The department list.
        self.dept_list = dept_list
        # The DingTalk number.
        self.ding_number = ding_number
        # The display name of the original account.
        self.display_name = display_name
        # The display name of the original account without the status suffix.
        self.display_name_without_status = display_name_without_status
        # Indicates whether the IP whitelist is enabled.
        self.enable_white_ip = enable_white_ip
        # The Lark bot.
        self.fei_shu_robot = fei_shu_robot
        # The creation time.
        self.gmt_create_time = gmt_create_time
        # The update time.
        self.gmt_modified_time = gmt_modified_time
        # The user ID.
        self.id = id
        # The email address.
        self.mail = mail
        # The mobile phone number.
        self.mobile_phone = mobile_phone
        # The user name.
        self.name = name
        # The nickname of the original account.
        self.nick_name = nick_name
        # The user ID of the tenant owner.
        self.parent_id = parent_id
        # The real name of the original account.
        self.real_name = real_name
        # The original account ID.
        self.source_id = source_id
        # The original account type.
        self.source_type = source_type
        # The WeCom bot.
        self.we_chat_robot = we_chat_robot
        # The IP address whitelist.
        self.white_ip = white_ip

    def validate(self):
        if self.dept_list:
            for v1 in self.dept_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.deleted is not None:
            result['Deleted'] = self.deleted

        result['DeptList'] = []
        if self.dept_list is not None:
            for k1 in self.dept_list:
                result['DeptList'].append(k1.to_map() if k1 else None)

        if self.ding_number is not None:
            result['DingNumber'] = self.ding_number

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.display_name_without_status is not None:
            result['DisplayNameWithoutStatus'] = self.display_name_without_status

        if self.enable_white_ip is not None:
            result['EnableWhiteIp'] = self.enable_white_ip

        if self.fei_shu_robot is not None:
            result['FeiShuRobot'] = self.fei_shu_robot

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.id is not None:
            result['Id'] = self.id

        if self.mail is not None:
            result['Mail'] = self.mail

        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone

        if self.name is not None:
            result['Name'] = self.name

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.real_name is not None:
            result['RealName'] = self.real_name

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.we_chat_robot is not None:
            result['WeChatRobot'] = self.we_chat_robot

        if self.white_ip is not None:
            result['WhiteIp'] = self.white_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        self.dept_list = []
        if m.get('DeptList') is not None:
            for k1 in m.get('DeptList'):
                temp_model = main_models.ListUsersResponseBodyPageResultUserListDeptList()
                self.dept_list.append(temp_model.from_map(k1))

        if m.get('DingNumber') is not None:
            self.ding_number = m.get('DingNumber')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('DisplayNameWithoutStatus') is not None:
            self.display_name_without_status = m.get('DisplayNameWithoutStatus')

        if m.get('EnableWhiteIp') is not None:
            self.enable_white_ip = m.get('EnableWhiteIp')

        if m.get('FeiShuRobot') is not None:
            self.fei_shu_robot = m.get('FeiShuRobot')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Mail') is not None:
            self.mail = m.get('Mail')

        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('RealName') is not None:
            self.real_name = m.get('RealName')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('WeChatRobot') is not None:
            self.we_chat_robot = m.get('WeChatRobot')

        if m.get('WhiteIp') is not None:
            self.white_ip = m.get('WhiteIp')

        return self

class ListUsersResponseBodyPageResultUserListDeptList(DaraModel):
    def __init__(
        self,
        children: List[Dict[str, Any]] = None,
        full_name: str = None,
        id: str = None,
        name: str = None,
        parent_id: str = None,
        parents: List[Dict[str, Any]] = None,
    ):
        # The sub-department list.
        self.children = children
        # The full path of the department.
        self.full_name = full_name
        # The department ID.
        self.id = id
        # The department name.
        self.name = name
        # The parent department ID.
        self.parent_id = parent_id
        # The parent department list.
        self.parents = parents

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.children is not None:
            result['Children'] = self.children

        if self.full_name is not None:
            result['FullName'] = self.full_name

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.parents is not None:
            result['Parents'] = self.parents

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Children') is not None:
            self.children = m.get('Children')

        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Parents') is not None:
            self.parents = m.get('Parents')

        return self

