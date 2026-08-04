# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class QueryEncryptedAccountProfileInfoResponseBody(DaraModel):
    def __init__(
        self,
        encrypted_profile_info: main_models.QueryEncryptedAccountProfileInfoResponseBodyEncryptedProfileInfo = None,
        request_id: str = None,
    ):
        self.encrypted_profile_info = encrypted_profile_info
        self.request_id = request_id

    def validate(self):
        if self.encrypted_profile_info:
            self.encrypted_profile_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encrypted_profile_info is not None:
            result['EncryptedProfileInfo'] = self.encrypted_profile_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptedProfileInfo') is not None:
            temp_model = main_models.QueryEncryptedAccountProfileInfoResponseBodyEncryptedProfileInfo()
            self.encrypted_profile_info = temp_model.from_map(m.get('EncryptedProfileInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryEncryptedAccountProfileInfoResponseBodyEncryptedProfileInfo(DaraModel):
    def __init__(
        self,
        encrypted_aliyun_id: str = None,
        encrypted_email: str = None,
        encrypted_mobile: str = None,
        encrypted_security_mobile: str = None,
        is_aliyun_id_an_email: bool = None,
        pk: str = None,
    ):
        self.encrypted_aliyun_id = encrypted_aliyun_id
        self.encrypted_email = encrypted_email
        self.encrypted_mobile = encrypted_mobile
        self.encrypted_security_mobile = encrypted_security_mobile
        self.is_aliyun_id_an_email = is_aliyun_id_an_email
        self.pk = pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encrypted_aliyun_id is not None:
            result['EncryptedAliyunID'] = self.encrypted_aliyun_id

        if self.encrypted_email is not None:
            result['EncryptedEmail'] = self.encrypted_email

        if self.encrypted_mobile is not None:
            result['EncryptedMobile'] = self.encrypted_mobile

        if self.encrypted_security_mobile is not None:
            result['EncryptedSecurityMobile'] = self.encrypted_security_mobile

        if self.is_aliyun_id_an_email is not None:
            result['IsAliyunIdAnEmail'] = self.is_aliyun_id_an_email

        if self.pk is not None:
            result['pk'] = self.pk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptedAliyunID') is not None:
            self.encrypted_aliyun_id = m.get('EncryptedAliyunID')

        if m.get('EncryptedEmail') is not None:
            self.encrypted_email = m.get('EncryptedEmail')

        if m.get('EncryptedMobile') is not None:
            self.encrypted_mobile = m.get('EncryptedMobile')

        if m.get('EncryptedSecurityMobile') is not None:
            self.encrypted_security_mobile = m.get('EncryptedSecurityMobile')

        if m.get('IsAliyunIdAnEmail') is not None:
            self.is_aliyun_id_an_email = m.get('IsAliyunIdAnEmail')

        if m.get('pk') is not None:
            self.pk = m.get('pk')

        return self

