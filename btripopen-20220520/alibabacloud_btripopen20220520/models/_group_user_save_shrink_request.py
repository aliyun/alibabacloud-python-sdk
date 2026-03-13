# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GroupUserSaveShrinkRequest(DaraModel):
    def __init__(
        self,
        base_city_code: str = None,
        birthday: str = None,
        cert_list_shrink: str = None,
        gender: str = None,
        job_no: str = None,
        phone: str = None,
        real_name_en: str = None,
        sub_corp_id_list_shrink: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.base_city_code = base_city_code
        self.birthday = birthday
        self.cert_list_shrink = cert_list_shrink
        self.gender = gender
        self.job_no = job_no
        self.phone = phone
        self.real_name_en = real_name_en
        # This parameter is required.
        self.sub_corp_id_list_shrink = sub_corp_id_list_shrink
        # This parameter is required.
        self.user_id = user_id
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_city_code is not None:
            result['base_city_code'] = self.base_city_code

        if self.birthday is not None:
            result['birthday'] = self.birthday

        if self.cert_list_shrink is not None:
            result['cert_list'] = self.cert_list_shrink

        if self.gender is not None:
            result['gender'] = self.gender

        if self.job_no is not None:
            result['job_no'] = self.job_no

        if self.phone is not None:
            result['phone'] = self.phone

        if self.real_name_en is not None:
            result['real_name_en'] = self.real_name_en

        if self.sub_corp_id_list_shrink is not None:
            result['sub_corp_id_list'] = self.sub_corp_id_list_shrink

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('base_city_code') is not None:
            self.base_city_code = m.get('base_city_code')

        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')

        if m.get('cert_list') is not None:
            self.cert_list_shrink = m.get('cert_list')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('job_no') is not None:
            self.job_no = m.get('job_no')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('real_name_en') is not None:
            self.real_name_en = m.get('real_name_en')

        if m.get('sub_corp_id_list') is not None:
            self.sub_corp_id_list_shrink = m.get('sub_corp_id_list')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

