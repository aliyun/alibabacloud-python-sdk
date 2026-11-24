# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WithdrawQuotaApplicationRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        reason: str = None,
    ):
        # The ID of the quota application.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The reason for withdrawing the quota increase request.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

