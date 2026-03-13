# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExceedApplySyncRequest(DaraModel):
    def __init__(
        self,
        apply_id: int = None,
        biz_category: int = None,
        remark: str = None,
        status: int = None,
        thirdparty_flow_id: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.apply_id = apply_id
        self.biz_category = biz_category
        self.remark = remark
        # This parameter is required.
        self.status = status
        self.thirdparty_flow_id = thirdparty_flow_id
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        if self.biz_category is not None:
            result['biz_category'] = self.biz_category

        if self.remark is not None:
            result['remark'] = self.remark

        if self.status is not None:
            result['status'] = self.status

        if self.thirdparty_flow_id is not None:
            result['thirdparty_flow_id'] = self.thirdparty_flow_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('biz_category') is not None:
            self.biz_category = m.get('biz_category')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('thirdparty_flow_id') is not None:
            self.thirdparty_flow_id = m.get('thirdparty_flow_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

