# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class FindAllContacterResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.FindAllContacterResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

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

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.FindAllContacterResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class FindAllContacterResponseBodyData(DaraModel):
    def __init__(
        self,
        contacter_info: List[main_models.FindAllContacterResponseBodyDataContacterInfo] = None,
    ):
        self.contacter_info = contacter_info

    def validate(self):
        if self.contacter_info:
            for v1 in self.contacter_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ContacterInfo'] = []
        if self.contacter_info is not None:
            for k1 in self.contacter_info:
                result['ContacterInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contacter_info = []
        if m.get('ContacterInfo') is not None:
            for k1 in m.get('ContacterInfo'):
                temp_model = main_models.FindAllContacterResponseBodyDataContacterInfo()
                self.contacter_info.append(temp_model.from_map(k1))

        return self

class FindAllContacterResponseBodyDataContacterInfo(DaraModel):
    def __init__(
        self,
        contacter_address: str = None,
        contacter_dingding: str = None,
        contacter_email: str = None,
        contacter_id: int = None,
        contacter_mobile: str = None,
        contacter_name: str = None,
        contacter_position: str = None,
        contacter_staff_no: str = None,
        contacter_type: str = None,
        contacter_wangwang: str = None,
        email_confirmed: bool = None,
        mobile_confirmed: bool = None,
    ):
        self.contacter_address = contacter_address
        self.contacter_dingding = contacter_dingding
        self.contacter_email = contacter_email
        self.contacter_id = contacter_id
        self.contacter_mobile = contacter_mobile
        self.contacter_name = contacter_name
        self.contacter_position = contacter_position
        self.contacter_staff_no = contacter_staff_no
        self.contacter_type = contacter_type
        self.contacter_wangwang = contacter_wangwang
        self.email_confirmed = email_confirmed
        self.mobile_confirmed = mobile_confirmed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contacter_address is not None:
            result['ContacterAddress'] = self.contacter_address

        if self.contacter_dingding is not None:
            result['ContacterDingding'] = self.contacter_dingding

        if self.contacter_email is not None:
            result['ContacterEmail'] = self.contacter_email

        if self.contacter_id is not None:
            result['ContacterId'] = self.contacter_id

        if self.contacter_mobile is not None:
            result['ContacterMobile'] = self.contacter_mobile

        if self.contacter_name is not None:
            result['ContacterName'] = self.contacter_name

        if self.contacter_position is not None:
            result['ContacterPosition'] = self.contacter_position

        if self.contacter_staff_no is not None:
            result['ContacterStaffNo'] = self.contacter_staff_no

        if self.contacter_type is not None:
            result['ContacterType'] = self.contacter_type

        if self.contacter_wangwang is not None:
            result['ContacterWangwang'] = self.contacter_wangwang

        if self.email_confirmed is not None:
            result['EmailConfirmed'] = self.email_confirmed

        if self.mobile_confirmed is not None:
            result['MobileConfirmed'] = self.mobile_confirmed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContacterAddress') is not None:
            self.contacter_address = m.get('ContacterAddress')

        if m.get('ContacterDingding') is not None:
            self.contacter_dingding = m.get('ContacterDingding')

        if m.get('ContacterEmail') is not None:
            self.contacter_email = m.get('ContacterEmail')

        if m.get('ContacterId') is not None:
            self.contacter_id = m.get('ContacterId')

        if m.get('ContacterMobile') is not None:
            self.contacter_mobile = m.get('ContacterMobile')

        if m.get('ContacterName') is not None:
            self.contacter_name = m.get('ContacterName')

        if m.get('ContacterPosition') is not None:
            self.contacter_position = m.get('ContacterPosition')

        if m.get('ContacterStaffNo') is not None:
            self.contacter_staff_no = m.get('ContacterStaffNo')

        if m.get('ContacterType') is not None:
            self.contacter_type = m.get('ContacterType')

        if m.get('ContacterWangwang') is not None:
            self.contacter_wangwang = m.get('ContacterWangwang')

        if m.get('EmailConfirmed') is not None:
            self.email_confirmed = m.get('EmailConfirmed')

        if m.get('MobileConfirmed') is not None:
            self.mobile_confirmed = m.get('MobileConfirmed')

        return self

