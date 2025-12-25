# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetUserResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        user: main_models.GetUserResponseBodyUser = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request fails.
        self.success = success
        # The information about the user.
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.user is not None:
            result['User'] = self.user.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('User') is not None:
            temp_model = main_models.GetUserResponseBodyUser()
            self.user = temp_model.from_map(m.get('User'))

        return self

class GetUserResponseBodyUser(DaraModel):
    def __init__(
        self,
        cur_execute_count: int = None,
        cur_result_count: int = None,
        ding_robot: str = None,
        email: str = None,
        last_login_time: str = None,
        max_execute_count: int = None,
        max_result_count: int = None,
        mobile: str = None,
        nick_name: str = None,
        notification_mode: str = None,
        parent_uid: int = None,
        role_id_list: main_models.GetUserResponseBodyUserRoleIdList = None,
        role_name_list: main_models.GetUserResponseBodyUserRoleNameList = None,
        signature_method: str = None,
        state: str = None,
        uid: str = None,
        user_id: str = None,
        webhook: str = None,
    ):
        # The number of queries that are performed on the current day.
        self.cur_execute_count = cur_execute_count
        # The number of rows that are queried on the current day.
        self.cur_result_count = cur_result_count
        # The DingTalk chatbot URL that is used to receive notifications.
        # 
        # > 
        # 
        # *   The system returns this parameter if the user has set a DingTalk chatbot URL in the console. To set a DingTalk chatbot URL in the console, move the pointer over the profile picture in the upper-right corner and click the Edit icon next to **Notice**.
        # 
        # *   The system does not return this parameter if the user has not set a DingTalk chatbot URL.
        self.ding_robot = ding_robot
        # The email address that is used to receive notifications.
        # 
        # > 
        # 
        # *   The system returns this parameter if the user has set an email address in the console. To set an email address in the console, move the pointer over the profile picture in the upper-right corner and click the Edit icon next to **Notice**.
        # 
        # *   The system does not return this parameter if the user has not set an email address.
        self.email = email
        # The last point in time when the user logged on to the console.
        self.last_login_time = last_login_time
        # The maximum number of queries that can be performed on the current day.
        self.max_execute_count = max_execute_count
        # The maximum number of rows that can be queried on the current day.
        self.max_result_count = max_result_count
        # The mobile number of the user.
        # 
        # > 
        # 
        # *   The system returns this parameter if the user has set a mobile phone number in the console. To set a mobile phone number in the console, move the pointer over the profile picture in the upper-right corner and click the Edit icon next to **Notice**.
        # 
        # *   The system does not return this parameter if the user has not set a mobile phone number.
        self.mobile = mobile
        # The nickname of the user.
        self.nick_name = nick_name
        # The notification method. The system returns one or more values. Valid values:
        # 
        # *   **SMS**: text message
        # *   **EMAIL**: email.
        # *   **DINGDING**: DingTalk.
        # *   **DINGROBOT**: DingTalk chatbot.
        # *   **WEBHOOK**: webhook.
        self.notification_mode = notification_mode
        # The UID of the Alibaba Cloud account of the user.
        # 
        # > An Alibaba Cloud account can contain one or more RAM users.
        self.parent_uid = parent_uid
        # The list of role IDs.
        self.role_id_list = role_id_list
        # The list of role names.
        self.role_name_list = role_name_list
        # The signature method that is used to secure connections when a webhook URL is used. Valid values:
        # 
        # *   **NONE**: no signature.
        # *   **HMAC_SHA1**: HMAC_SHA1.
        self.signature_method = signature_method
        # The status of the user. Valid values:
        # 
        # *   **NORMAL**: The user is normal.
        # *   **DISABLE**: The user is disabled.
        # *   **DELETE**: The user is deleted.
        self.state = state
        # The UID of the user.
        self.uid = uid
        # The ID of the user.
        self.user_id = user_id
        # The webhook URL that is used to receive notifications.
        # 
        # > 
        # 
        # *   If the user has set a webhook URL, DMS sends notifications to the specified URL.
        # 
        # *   The system does not return this parameter if the user has not set a webhook URL.
        self.webhook = webhook

    def validate(self):
        if self.role_id_list:
            self.role_id_list.validate()
        if self.role_name_list:
            self.role_name_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cur_execute_count is not None:
            result['CurExecuteCount'] = self.cur_execute_count

        if self.cur_result_count is not None:
            result['CurResultCount'] = self.cur_result_count

        if self.ding_robot is not None:
            result['DingRobot'] = self.ding_robot

        if self.email is not None:
            result['Email'] = self.email

        if self.last_login_time is not None:
            result['LastLoginTime'] = self.last_login_time

        if self.max_execute_count is not None:
            result['MaxExecuteCount'] = self.max_execute_count

        if self.max_result_count is not None:
            result['MaxResultCount'] = self.max_result_count

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.notification_mode is not None:
            result['NotificationMode'] = self.notification_mode

        if self.parent_uid is not None:
            result['ParentUid'] = self.parent_uid

        if self.role_id_list is not None:
            result['RoleIdList'] = self.role_id_list.to_map()

        if self.role_name_list is not None:
            result['RoleNameList'] = self.role_name_list.to_map()

        if self.signature_method is not None:
            result['SignatureMethod'] = self.signature_method

        if self.state is not None:
            result['State'] = self.state

        if self.uid is not None:
            result['Uid'] = self.uid

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.webhook is not None:
            result['Webhook'] = self.webhook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurExecuteCount') is not None:
            self.cur_execute_count = m.get('CurExecuteCount')

        if m.get('CurResultCount') is not None:
            self.cur_result_count = m.get('CurResultCount')

        if m.get('DingRobot') is not None:
            self.ding_robot = m.get('DingRobot')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('LastLoginTime') is not None:
            self.last_login_time = m.get('LastLoginTime')

        if m.get('MaxExecuteCount') is not None:
            self.max_execute_count = m.get('MaxExecuteCount')

        if m.get('MaxResultCount') is not None:
            self.max_result_count = m.get('MaxResultCount')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('NotificationMode') is not None:
            self.notification_mode = m.get('NotificationMode')

        if m.get('ParentUid') is not None:
            self.parent_uid = m.get('ParentUid')

        if m.get('RoleIdList') is not None:
            temp_model = main_models.GetUserResponseBodyUserRoleIdList()
            self.role_id_list = temp_model.from_map(m.get('RoleIdList'))

        if m.get('RoleNameList') is not None:
            temp_model = main_models.GetUserResponseBodyUserRoleNameList()
            self.role_name_list = temp_model.from_map(m.get('RoleNameList'))

        if m.get('SignatureMethod') is not None:
            self.signature_method = m.get('SignatureMethod')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')

        return self

class GetUserResponseBodyUserRoleNameList(DaraModel):
    def __init__(
        self,
        role_names: List[str] = None,
    ):
        self.role_names = role_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_names is not None:
            result['RoleNames'] = self.role_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleNames') is not None:
            self.role_names = m.get('RoleNames')

        return self

class GetUserResponseBodyUserRoleIdList(DaraModel):
    def __init__(
        self,
        role_ids: List[int] = None,
    ):
        self.role_ids = role_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_ids is not None:
            result['RoleIds'] = self.role_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleIds') is not None:
            self.role_ids = m.get('RoleIds')

        return self

