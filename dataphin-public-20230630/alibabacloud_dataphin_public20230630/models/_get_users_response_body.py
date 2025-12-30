# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetUsersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        user_list: List[main_models.GetUsersResponseBodyUserList] = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
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
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        result['UserList'] = []
        if self.user_list is not None:
            for k1 in self.user_list:
                result['UserList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.user_list = []
        if m.get('UserList') is not None:
            for k1 in m.get('UserList'):
                temp_model = main_models.GetUsersResponseBodyUserList()
                self.user_list.append(temp_model.from_map(k1))

        return self

class GetUsersResponseBodyUserList(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        ding_number: str = None,
        display_name: str = None,
        display_name_without_status: str = None,
        enable_white_ip: str = None,
        fei_shu_robot: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
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
        self.account_name = account_name
        self.ding_number = ding_number
        self.display_name = display_name
        self.display_name_without_status = display_name_without_status
        self.enable_white_ip = enable_white_ip
        self.fei_shu_robot = fei_shu_robot
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.mail = mail
        self.mobile_phone = mobile_phone
        self.name = name
        self.nick_name = nick_name
        self.parent_id = parent_id
        self.real_name = real_name
        self.source_id = source_id
        self.source_type = source_type
        self.we_chat_robot = we_chat_robot
        self.white_ip = white_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

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

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

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

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

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

