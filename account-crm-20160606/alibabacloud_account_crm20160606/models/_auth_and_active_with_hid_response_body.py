# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class AuthAndActiveWithHidResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.AuthAndActiveWithHidResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.AuthAndActiveWithHidResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AuthAndActiveWithHidResponseBodyData(DaraModel):
    def __init__(
        self,
        account_model: main_models.AuthAndActiveWithHidResponseBodyDataAccountModel = None,
        session_model: main_models.AuthAndActiveWithHidResponseBodyDataSessionModel = None,
    ):
        self.account_model = account_model
        self.session_model = session_model

    def validate(self):
        if self.account_model:
            self.account_model.validate()
        if self.session_model:
            self.session_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_model is not None:
            result['AccountModel'] = self.account_model.to_map()

        if self.session_model is not None:
            result['SessionModel'] = self.session_model.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountModel') is not None:
            temp_model = main_models.AuthAndActiveWithHidResponseBodyDataAccountModel()
            self.account_model = temp_model.from_map(m.get('AccountModel'))

        if m.get('SessionModel') is not None:
            temp_model = main_models.AuthAndActiveWithHidResponseBodyDataSessionModel()
            self.session_model = temp_model.from_map(m.get('SessionModel'))

        return self

class AuthAndActiveWithHidResponseBodyDataSessionModel(DaraModel):
    def __init__(
        self,
        aliyun_pk: str = None,
        login_ticket: str = None,
    ):
        self.aliyun_pk = aliyun_pk
        self.login_ticket = login_ticket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_pk is not None:
            result['AliyunPK'] = self.aliyun_pk

        if self.login_ticket is not None:
            result['LoginTicket'] = self.login_ticket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunPK') is not None:
            self.aliyun_pk = m.get('AliyunPK')

        if m.get('LoginTicket') is not None:
            self.login_ticket = m.get('LoginTicket')

        return self



class AuthAndActiveWithHidResponseBodyDataAccountModel(DaraModel):
    def __init__(
        self,
        aliyun_id: str = None,
        create_time: int = None,
        email: str = None,
        havana_id: int = None,
        mobile: str = None,
        pk: str = None,
    ):
        self.aliyun_id = aliyun_id
        self.create_time = create_time
        self.email = email
        self.havana_id = havana_id
        self.mobile = mobile
        self.pk = pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.email is not None:
            result['Email'] = self.email

        if self.havana_id is not None:
            result['HavanaId'] = self.havana_id

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.pk is not None:
            result['PK'] = self.pk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('HavanaId') is not None:
            self.havana_id = m.get('HavanaId')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('PK') is not None:
            self.pk = m.get('PK')

        return self

