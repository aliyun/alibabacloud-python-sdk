# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class ExternalUserUpdateRequest(DaraModel):
    def __init__(
        self,
        birthday: str = None,
        cert_request_list: List[main_models.ExternalUserUpdateRequestCertRequestList] = None,
        email: str = None,
        phone: str = None,
        real_name: str = None,
        real_name_en: str = None,
    ):
        self.birthday = birthday
        self.cert_request_list = cert_request_list
        self.email = email
        self.phone = phone
        self.real_name = real_name
        self.real_name_en = real_name_en

    def validate(self):
        if self.cert_request_list:
            for v1 in self.cert_request_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.birthday is not None:
            result['birthday'] = self.birthday

        result['cert_request_list'] = []
        if self.cert_request_list is not None:
            for k1 in self.cert_request_list:
                result['cert_request_list'].append(k1.to_map() if k1 else None)

        if self.email is not None:
            result['email'] = self.email

        if self.phone is not None:
            result['phone'] = self.phone

        if self.real_name is not None:
            result['real_name'] = self.real_name

        if self.real_name_en is not None:
            result['real_name_en'] = self.real_name_en

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')

        self.cert_request_list = []
        if m.get('cert_request_list') is not None:
            for k1 in m.get('cert_request_list'):
                temp_model = main_models.ExternalUserUpdateRequestCertRequestList()
                self.cert_request_list.append(temp_model.from_map(k1))

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('real_name') is not None:
            self.real_name = m.get('real_name')

        if m.get('real_name_en') is not None:
            self.real_name_en = m.get('real_name_en')

        return self

class ExternalUserUpdateRequestCertRequestList(DaraModel):
    def __init__(
        self,
        cert_expired_time: str = None,
        cert_nation: str = None,
        cert_no: str = None,
        cert_type: int = None,
        nationality: str = None,
    ):
        self.cert_expired_time = cert_expired_time
        self.cert_nation = cert_nation
        # This parameter is required.
        self.cert_no = cert_no
        # This parameter is required.
        self.cert_type = cert_type
        self.nationality = nationality

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_expired_time is not None:
            result['cert_expired_time'] = self.cert_expired_time

        if self.cert_nation is not None:
            result['cert_nation'] = self.cert_nation

        if self.cert_no is not None:
            result['cert_no'] = self.cert_no

        if self.cert_type is not None:
            result['cert_type'] = self.cert_type

        if self.nationality is not None:
            result['nationality'] = self.nationality

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cert_expired_time') is not None:
            self.cert_expired_time = m.get('cert_expired_time')

        if m.get('cert_nation') is not None:
            self.cert_nation = m.get('cert_nation')

        if m.get('cert_no') is not None:
            self.cert_no = m.get('cert_no')

        if m.get('cert_type') is not None:
            self.cert_type = m.get('cert_type')

        if m.get('nationality') is not None:
            self.nationality = m.get('nationality')

        return self

