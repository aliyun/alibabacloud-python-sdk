# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeScanTaskStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        dealed_risk_num: int = None,
        personal_task_num: int = None,
        request_id: str = None,
        total_task_num: int = None,
        user_num: int = None,
    ):
        # The number of risks that are handled for the user.
        self.dealed_risk_num = dealed_risk_num
        # The total number of tasks that are created for the user.
        self.personal_task_num = personal_task_num
        # The request ID.
        self.request_id = request_id
        # The total number of virus detection tasks.
        self.total_task_num = total_task_num
        # The number of risks that are detected for the user.
        self.user_num = user_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dealed_risk_num is not None:
            result['DealedRiskNum'] = self.dealed_risk_num

        if self.personal_task_num is not None:
            result['PersonalTaskNum'] = self.personal_task_num

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_task_num is not None:
            result['TotalTaskNum'] = self.total_task_num

        if self.user_num is not None:
            result['UserNum'] = self.user_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DealedRiskNum') is not None:
            self.dealed_risk_num = m.get('DealedRiskNum')

        if m.get('PersonalTaskNum') is not None:
            self.personal_task_num = m.get('PersonalTaskNum')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalTaskNum') is not None:
            self.total_task_num = m.get('TotalTaskNum')

        if m.get('UserNum') is not None:
            self.user_num = m.get('UserNum')

        return self

