# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckTrialFixCountResponseBody(DaraModel):
    def __init__(
        self,
        can_fix: bool = None,
        expend_count: int = None,
        remain_count: int = None,
        repaired_count: int = None,
        request_id: str = None,
        is_trial: bool = None,
    ):
        # Indicates whether the vulnerability can be fixed. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.can_fix = can_fix
        # The quota usage required for the current fix operation.
        self.expend_count = expend_count
        # The quota that remains after the current fix operation is complete.
        self.remain_count = remain_count
        # The number of the vulnerabilities that are fixed.
        self.repaired_count = repaired_count
        # The request ID.
        self.request_id = request_id
        # Indicates whether Security Center is in free trial. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_trial = is_trial

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_fix is not None:
            result['CanFix'] = self.can_fix

        if self.expend_count is not None:
            result['ExpendCount'] = self.expend_count

        if self.remain_count is not None:
            result['RemainCount'] = self.remain_count

        if self.repaired_count is not None:
            result['RepairedCount'] = self.repaired_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.is_trial is not None:
            result['isTrial'] = self.is_trial

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanFix') is not None:
            self.can_fix = m.get('CanFix')

        if m.get('ExpendCount') is not None:
            self.expend_count = m.get('ExpendCount')

        if m.get('RemainCount') is not None:
            self.remain_count = m.get('RemainCount')

        if m.get('RepairedCount') is not None:
            self.repaired_count = m.get('RepairedCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('isTrial') is not None:
            self.is_trial = m.get('isTrial')

        return self

