# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCostOptimizationOverviewShrinkRequest(DaraModel):
    def __init__(
        self,
        assume_aliyun_id: int = None,
        assume_aliyun_id_list_shrink: str = None,
        check_plan_id: int = None,
        token: str = None,
    ):
        self.assume_aliyun_id = assume_aliyun_id
        self.assume_aliyun_id_list_shrink = assume_aliyun_id_list_shrink
        self.check_plan_id = check_plan_id
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assume_aliyun_id is not None:
            result['AssumeAliyunId'] = self.assume_aliyun_id

        if self.assume_aliyun_id_list_shrink is not None:
            result['AssumeAliyunIdList'] = self.assume_aliyun_id_list_shrink

        if self.check_plan_id is not None:
            result['CheckPlanId'] = self.check_plan_id

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeAliyunId') is not None:
            self.assume_aliyun_id = m.get('AssumeAliyunId')

        if m.get('AssumeAliyunIdList') is not None:
            self.assume_aliyun_id_list_shrink = m.get('AssumeAliyunIdList')

        if m.get('CheckPlanId') is not None:
            self.check_plan_id = m.get('CheckPlanId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

