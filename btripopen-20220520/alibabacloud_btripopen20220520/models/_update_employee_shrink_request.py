# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateEmployeeShrinkRequest(DaraModel):
    def __init__(
        self,
        account_email: str = None,
        account_phone: str = None,
        attribute: str = None,
        avatar: str = None,
        base_city_code_list_shrink: str = None,
        base_location_list_shrink: str = None,
        birthday: str = None,
        cert_list_shrink: str = None,
        custom_role_code_list_shrink: str = None,
        email: str = None,
        gender: str = None,
        is_admin: bool = None,
        is_boss: bool = None,
        is_dept_leader: bool = None,
        job_no: str = None,
        manager_user_id: str = None,
        out_dept_id_list_shrink: str = None,
        phone: str = None,
        position_level: str = None,
        real_name: str = None,
        real_name_en: str = None,
        user_id: str = None,
        user_nick: str = None,
    ):
        self.account_email = account_email
        self.account_phone = account_phone
        self.attribute = attribute
        self.avatar = avatar
        self.base_city_code_list_shrink = base_city_code_list_shrink
        self.base_location_list_shrink = base_location_list_shrink
        self.birthday = birthday
        self.cert_list_shrink = cert_list_shrink
        self.custom_role_code_list_shrink = custom_role_code_list_shrink
        self.email = email
        self.gender = gender
        self.is_admin = is_admin
        self.is_boss = is_boss
        self.is_dept_leader = is_dept_leader
        self.job_no = job_no
        self.manager_user_id = manager_user_id
        self.out_dept_id_list_shrink = out_dept_id_list_shrink
        self.phone = phone
        self.position_level = position_level
        self.real_name = real_name
        self.real_name_en = real_name_en
        # This parameter is required.
        self.user_id = user_id
        self.user_nick = user_nick

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_email is not None:
            result['account_email'] = self.account_email

        if self.account_phone is not None:
            result['account_phone'] = self.account_phone

        if self.attribute is not None:
            result['attribute'] = self.attribute

        if self.avatar is not None:
            result['avatar'] = self.avatar

        if self.base_city_code_list_shrink is not None:
            result['base_city_code_list'] = self.base_city_code_list_shrink

        if self.base_location_list_shrink is not None:
            result['base_location_list'] = self.base_location_list_shrink

        if self.birthday is not None:
            result['birthday'] = self.birthday

        if self.cert_list_shrink is not None:
            result['cert_list'] = self.cert_list_shrink

        if self.custom_role_code_list_shrink is not None:
            result['custom_role_code_list'] = self.custom_role_code_list_shrink

        if self.email is not None:
            result['email'] = self.email

        if self.gender is not None:
            result['gender'] = self.gender

        if self.is_admin is not None:
            result['is_admin'] = self.is_admin

        if self.is_boss is not None:
            result['is_boss'] = self.is_boss

        if self.is_dept_leader is not None:
            result['is_dept_leader'] = self.is_dept_leader

        if self.job_no is not None:
            result['job_no'] = self.job_no

        if self.manager_user_id is not None:
            result['manager_user_id'] = self.manager_user_id

        if self.out_dept_id_list_shrink is not None:
            result['out_dept_id_list'] = self.out_dept_id_list_shrink

        if self.phone is not None:
            result['phone'] = self.phone

        if self.position_level is not None:
            result['position_level'] = self.position_level

        if self.real_name is not None:
            result['real_name'] = self.real_name

        if self.real_name_en is not None:
            result['real_name_en'] = self.real_name_en

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_nick is not None:
            result['user_nick'] = self.user_nick

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('account_email') is not None:
            self.account_email = m.get('account_email')

        if m.get('account_phone') is not None:
            self.account_phone = m.get('account_phone')

        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')

        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')

        if m.get('base_city_code_list') is not None:
            self.base_city_code_list_shrink = m.get('base_city_code_list')

        if m.get('base_location_list') is not None:
            self.base_location_list_shrink = m.get('base_location_list')

        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')

        if m.get('cert_list') is not None:
            self.cert_list_shrink = m.get('cert_list')

        if m.get('custom_role_code_list') is not None:
            self.custom_role_code_list_shrink = m.get('custom_role_code_list')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('is_admin') is not None:
            self.is_admin = m.get('is_admin')

        if m.get('is_boss') is not None:
            self.is_boss = m.get('is_boss')

        if m.get('is_dept_leader') is not None:
            self.is_dept_leader = m.get('is_dept_leader')

        if m.get('job_no') is not None:
            self.job_no = m.get('job_no')

        if m.get('manager_user_id') is not None:
            self.manager_user_id = m.get('manager_user_id')

        if m.get('out_dept_id_list') is not None:
            self.out_dept_id_list_shrink = m.get('out_dept_id_list')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('position_level') is not None:
            self.position_level = m.get('position_level')

        if m.get('real_name') is not None:
            self.real_name = m.get('real_name')

        if m.get('real_name_en') is not None:
            self.real_name_en = m.get('real_name_en')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_nick') is not None:
            self.user_nick = m.get('user_nick')

        return self

