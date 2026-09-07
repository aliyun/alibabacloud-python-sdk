# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InvalidateApprovalRequest(DaraModel):
    def __init__(
        self,
        approval_id: str = None,
    ):
        # The ID of the approval instance to immediately invalidate. You can call ListApprovals to query approval instance IDs. Only one approval instance ID under the current Alibaba Cloud account can be specified per request.
        # 
        # This parameter is required.
        self.approval_id = approval_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_id is not None:
            result['ApprovalId'] = self.approval_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalId') is not None:
            self.approval_id = m.get('ApprovalId')

        return self

