# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class DescribeBeebotIntentResponseBody(DaraModel):
    def __init__(
        self,
        beebot_request_id: str = None,
        code: str = None,
        http_status_code: int = None,
        intent: main_models.DescribeBeebotIntentResponseBodyIntent = None,
        intent_id: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.beebot_request_id = beebot_request_id
        self.code = code
        self.http_status_code = http_status_code
        self.intent = intent
        self.intent_id = intent_id
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.intent:
            self.intent.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.beebot_request_id is not None:
            result['BeebotRequestId'] = self.beebot_request_id

        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.intent is not None:
            result['Intent'] = self.intent.to_map()

        if self.intent_id is not None:
            result['IntentId'] = self.intent_id

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeebotRequestId') is not None:
            self.beebot_request_id = m.get('BeebotRequestId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Intent') is not None:
            temp_model = main_models.DescribeBeebotIntentResponseBodyIntent()
            self.intent = temp_model.from_map(m.get('Intent'))

        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeBeebotIntentResponseBodyIntent(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        create_time: str = None,
        create_user_id: str = None,
        create_user_name: str = None,
        intent_id: int = None,
        intent_name: str = None,
        modify_time: str = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
    ):
        self.alias_name = alias_name
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.intent_id = intent_id
        self.intent_name = intent_name
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id

        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name

        if self.intent_id is not None:
            result['IntentId'] = self.intent_id

        if self.intent_name is not None:
            result['IntentName'] = self.intent_name

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id

        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')

        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')

        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')

        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')

        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')

        return self

