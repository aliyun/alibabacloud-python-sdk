# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ProcessApprovalRequest(DaraModel):
    def __init__(
        self,
        application_sheet_id: str = None,
        approval_action: str = None,
        approval_comments: str = None,
    ):
        # This parameter is required.
        self.application_sheet_id = application_sheet_id
        # This parameter is required.
        self.approval_action = approval_action
        # This parameter is required.
        self.approval_comments = approval_comments

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_sheet_id is not None:
            result['ApplicationSheetId'] = self.application_sheet_id

        if self.approval_action is not None:
            result['ApprovalAction'] = self.approval_action

        if self.approval_comments is not None:
            result['ApprovalComments'] = self.approval_comments

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationSheetId') is not None:
            self.application_sheet_id = m.get('ApplicationSheetId')

        if m.get('ApprovalAction') is not None:
            self.approval_action = m.get('ApprovalAction')

        if m.get('ApprovalComments') is not None:
            self.approval_comments = m.get('ApprovalComments')

        return self

