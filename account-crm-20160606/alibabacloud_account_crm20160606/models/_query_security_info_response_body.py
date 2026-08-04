# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class QuerySecurityInfoResponseBody(DaraModel):
    def __init__(
        self,
        account_security_info_dto: main_models.QuerySecurityInfoResponseBodyAccountSecurityInfoDto = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.account_security_info_dto = account_security_info_dto
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.account_security_info_dto:
            self.account_security_info_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_security_info_dto is not None:
            result['AccountSecurityInfoDto'] = self.account_security_info_dto.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountSecurityInfoDto') is not None:
            temp_model = main_models.QuerySecurityInfoResponseBodyAccountSecurityInfoDto()
            self.account_security_info_dto = temp_model.from_map(m.get('AccountSecurityInfoDto'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QuerySecurityInfoResponseBodyAccountSecurityInfoDto(DaraModel):
    def __init__(
        self,
        aliyun_id: str = None,
        name: str = None,
        nationality_code: str = None,
        pk: str = None,
        profile_type: str = None,
        security_email: str = None,
        security_mobile: str = None,
    ):
        self.aliyun_id = aliyun_id
        self.name = name
        self.nationality_code = nationality_code
        self.pk = pk
        self.profile_type = profile_type
        self.security_email = security_email
        self.security_mobile = security_mobile

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id

        if self.name is not None:
            result['Name'] = self.name

        if self.nationality_code is not None:
            result['NationalityCode'] = self.nationality_code

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.profile_type is not None:
            result['ProfileType'] = self.profile_type

        if self.security_email is not None:
            result['SecurityEmail'] = self.security_email

        if self.security_mobile is not None:
            result['SecurityMobile'] = self.security_mobile

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NationalityCode') is not None:
            self.nationality_code = m.get('NationalityCode')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('ProfileType') is not None:
            self.profile_type = m.get('ProfileType')

        if m.get('SecurityEmail') is not None:
            self.security_email = m.get('SecurityEmail')

        if m.get('SecurityMobile') is not None:
            self.security_mobile = m.get('SecurityMobile')

        return self

