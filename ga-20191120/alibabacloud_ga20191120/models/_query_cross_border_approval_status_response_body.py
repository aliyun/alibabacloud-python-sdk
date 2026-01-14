# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCrossBorderApprovalStatusResponseBody(DaraModel):
    def __init__(
        self,
        approval_status: str = None,
        request_id: str = None,
    ):
        # Cross border permissions of Alibaba Cloud account (main account).
        # 
        # -  UNAPPLIED : No cross-border permission application has been submitted or application records cannot be found.
        # -  APPLIED : Cross-border permission review in progress.
        # -  REJECTED : Cross-border permission review failed.
        # -  PASSED : Cross-border permission review passed.
        self.approval_status = approval_status
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_status is not None:
            result['ApprovalStatus'] = self.approval_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalStatus') is not None:
            self.approval_status = m.get('ApprovalStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

