# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SyncSingleUserShrinkRequest(DaraModel):
    def __init__(
        self,
        email: str = None,
        job_no: str = None,
        leave_status: int = None,
        manager_user_id: str = None,
        phone: str = None,
        position: str = None,
        position_level: str = None,
        real_name_en: str = None,
        third_depart_id_list_shrink: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.email = email
        self.job_no = job_no
        self.leave_status = leave_status
        self.manager_user_id = manager_user_id
        self.phone = phone
        self.position = position
        self.position_level = position_level
        self.real_name_en = real_name_en
        self.third_depart_id_list_shrink = third_depart_id_list_shrink
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
        if self.email is not None:
            result['email'] = self.email

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

        if self.third_depart_id_list_shrink is not None:
            result['third_depart_id_list'] = self.third_depart_id_list_shrink

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')

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

        if m.get('third_depart_id_list') is not None:
            self.third_depart_id_list_shrink = m.get('third_depart_id_list')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

