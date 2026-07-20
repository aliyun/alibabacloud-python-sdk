# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class ExternalUserQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        module: main_models.ExternalUserQueryResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.module = module
        self.request_id = request_id
        self.success = success
        # traceId
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.module is not None:
            result['module'] = self.module.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('module') is not None:
            temp_model = main_models.ExternalUserQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class ExternalUserQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        birthday: str = None,
        corp_id: str = None,
        email: str = None,
        external_user_id: str = None,
        phone: str = None,
        real_name: str = None,
        real_name_en: str = None,
        user_id: str = None,
        user_nick: str = None,
        user_type: int = None,
    ):
        self.birthday = birthday
        self.corp_id = corp_id
        self.email = email
        self.external_user_id = external_user_id
        self.phone = phone
        self.real_name = real_name
        self.real_name_en = real_name_en
        self.user_id = user_id
        self.user_nick = user_nick
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.birthday is not None:
            result['birthday'] = self.birthday

        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.email is not None:
            result['email'] = self.email

        if self.external_user_id is not None:
            result['external_user_id'] = self.external_user_id

        if self.phone is not None:
            result['phone'] = self.phone

        if self.real_name is not None:
            result['real_name'] = self.real_name

        if self.real_name_en is not None:
            result['real_name_en'] = self.real_name_en

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_nick is not None:
            result['user_nick'] = self.user_nick

        if self.user_type is not None:
            result['user_type'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')

        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('external_user_id') is not None:
            self.external_user_id = m.get('external_user_id')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('real_name') is not None:
            self.real_name = m.get('real_name')

        if m.get('real_name_en') is not None:
            self.real_name_en = m.get('real_name_en')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_nick') is not None:
            self.user_nick = m.get('user_nick')

        if m.get('user_type') is not None:
            self.user_type = m.get('user_type')

        return self

