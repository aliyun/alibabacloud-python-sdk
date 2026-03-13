# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyApproveRequest(DaraModel):
    def __init__(
        self,
        apply_id: str = None,
        note: str = None,
        operate_time: str = None,
        status: int = None,
        sub_corp_id: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # This parameter is required.
        self.apply_id = apply_id
        self.note = note
        # This parameter is required.
        self.operate_time = operate_time
        # This parameter is required.
        self.status = status
        self.sub_corp_id = sub_corp_id
        # This parameter is required.
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        if self.note is not None:
            result['note'] = self.note

        if self.operate_time is not None:
            result['operate_time'] = self.operate_time

        if self.status is not None:
            result['status'] = self.status

        if self.sub_corp_id is not None:
            result['sub_corp_id'] = self.sub_corp_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('note') is not None:
            self.note = m.get('note')

        if m.get('operate_time') is not None:
            self.operate_time = m.get('operate_time')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('sub_corp_id') is not None:
            self.sub_corp_id = m.get('sub_corp_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

