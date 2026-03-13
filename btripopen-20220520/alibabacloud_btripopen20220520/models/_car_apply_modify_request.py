# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CarApplyModifyRequest(DaraModel):
    def __init__(
        self,
        operate_time: str = None,
        remark: str = None,
        status: int = None,
        third_part_apply_id: str = None,
        user_id: str = None,
    ):
        self.operate_time = operate_time
        self.remark = remark
        # This parameter is required.
        self.status = status
        # This parameter is required.
        self.third_part_apply_id = third_part_apply_id
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operate_time is not None:
            result['operate_time'] = self.operate_time

        if self.remark is not None:
            result['remark'] = self.remark

        if self.status is not None:
            result['status'] = self.status

        if self.third_part_apply_id is not None:
            result['third_part_apply_id'] = self.third_part_apply_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operate_time') is not None:
            self.operate_time = m.get('operate_time')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('third_part_apply_id') is not None:
            self.third_part_apply_id = m.get('third_part_apply_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

