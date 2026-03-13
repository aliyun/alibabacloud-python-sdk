# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class IsvUserSaveRequest(DaraModel):
    def __init__(
        self,
        user_list: List[main_models.IsvUserSaveRequestUserList] = None,
    ):
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
        result['user_list'] = []
        if self.user_list is not None:
            for k1 in self.user_list:
                result['user_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_list = []
        if m.get('user_list') is not None:
            for k1 in m.get('user_list'):
                temp_model = main_models.IsvUserSaveRequestUserList()
                self.user_list.append(temp_model.from_map(k1))

        return self

class IsvUserSaveRequestUserList(DaraModel):
    def __init__(
        self,
        base_city_code: str = None,
        birthday: str = None,
        cert_list: List[main_models.IsvUserSaveRequestUserListCertList] = None,
        depart_id: int = None,
        email: str = None,
        gender: str = None,
        is_admin: bool = None,
        job_no: str = None,
        leave_status: int = None,
        manager_user_id: str = None,
        phone: str = None,
        position: str = None,
        position_level: str = None,
        real_name_en: str = None,
        role_id_list: List[str] = None,
        third_depart_id: str = None,
        third_depart_id_list: List[str] = None,
        user_id: str = None,
        user_name: str = None,
        user_nick: str = None,
    ):
        self.base_city_code = base_city_code
        self.birthday = birthday
        self.cert_list = cert_list
        self.depart_id = depart_id
        self.email = email
        self.gender = gender
        self.is_admin = is_admin
        self.job_no = job_no
        self.leave_status = leave_status
        self.manager_user_id = manager_user_id
        self.phone = phone
        self.position = position
        self.position_level = position_level
        self.real_name_en = real_name_en
        self.role_id_list = role_id_list
        self.third_depart_id = third_depart_id
        self.third_depart_id_list = third_depart_id_list
        # This parameter is required.
        self.user_id = user_id
        # This parameter is required.
        self.user_name = user_name
        self.user_nick = user_nick

    def validate(self):
        if self.cert_list:
            for v1 in self.cert_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_city_code is not None:
            result['base_city_code'] = self.base_city_code

        if self.birthday is not None:
            result['birthday'] = self.birthday

        result['cert_list'] = []
        if self.cert_list is not None:
            for k1 in self.cert_list:
                result['cert_list'].append(k1.to_map() if k1 else None)

        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

        if self.email is not None:
            result['email'] = self.email

        if self.gender is not None:
            result['gender'] = self.gender

        if self.is_admin is not None:
            result['is_admin'] = self.is_admin

        if self.job_no is not None:
            result['job_no'] = self.job_no

        if self.leave_status is not None:
            result['leave_status'] = self.leave_status

        if self.manager_user_id is not None:
            result['manager_user_id'] = self.manager_user_id

        if self.phone is not None:
            result['phone'] = self.phone

        if self.position is not None:
            result['position'] = self.position

        if self.position_level is not None:
            result['position_level'] = self.position_level

        if self.real_name_en is not None:
            result['real_name_en'] = self.real_name_en

        if self.role_id_list is not None:
            result['role_id_list'] = self.role_id_list

        if self.third_depart_id is not None:
            result['third_depart_id'] = self.third_depart_id

        if self.third_depart_id_list is not None:
            result['third_depart_id_list'] = self.third_depart_id_list

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        if self.user_nick is not None:
            result['user_nick'] = self.user_nick

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('base_city_code') is not None:
            self.base_city_code = m.get('base_city_code')

        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')

        self.cert_list = []
        if m.get('cert_list') is not None:
            for k1 in m.get('cert_list'):
                temp_model = main_models.IsvUserSaveRequestUserListCertList()
                self.cert_list.append(temp_model.from_map(k1))

        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('is_admin') is not None:
            self.is_admin = m.get('is_admin')

        if m.get('job_no') is not None:
            self.job_no = m.get('job_no')

        if m.get('leave_status') is not None:
            self.leave_status = m.get('leave_status')

        if m.get('manager_user_id') is not None:
            self.manager_user_id = m.get('manager_user_id')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('position') is not None:
            self.position = m.get('position')

        if m.get('position_level') is not None:
            self.position_level = m.get('position_level')

        if m.get('real_name_en') is not None:
            self.real_name_en = m.get('real_name_en')

        if m.get('role_id_list') is not None:
            self.role_id_list = m.get('role_id_list')

        if m.get('third_depart_id') is not None:
            self.third_depart_id = m.get('third_depart_id')

        if m.get('third_depart_id_list') is not None:
            self.third_depart_id_list = m.get('third_depart_id_list')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        if m.get('user_nick') is not None:
            self.user_nick = m.get('user_nick')

        return self

class IsvUserSaveRequestUserListCertList(DaraModel):
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
        self.cert_no = cert_no
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

