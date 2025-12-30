# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateProduceForPartnerRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        ext_info: str = None,
        operate_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.ext_info = ext_info
        self.operate_type = operate_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        return self

