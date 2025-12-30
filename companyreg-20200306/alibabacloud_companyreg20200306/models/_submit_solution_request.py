# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitSolutionRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        intention_biz_id: str = None,
        operate_type: str = None,
        solution: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.biz_type = biz_type
        # This parameter is required.
        self.intention_biz_id = intention_biz_id
        self.operate_type = operate_type
        # This parameter is required.
        self.solution = solution
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        if self.solution is not None:
            result['Solution'] = self.solution

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('Solution') is not None:
            self.solution = m.get('Solution')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

