# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InvalidateApprovalResponseBody(DaraModel):
    def __init__(
        self,
        approval_id: str = None,
        effect_status: str = None,
        report_type: str = None,
        request_id: str = None,
    ):
        # The ID of the invalidated approval instance.
        self.approval_id = approval_id
        # The effective status of the approval. When the invalidation succeeds, the value is fixed as Expired, which indicates that the approval has been invalidated.
        self.effect_status = effect_status
        # The approval type. Valid values:
        # * ApprovalReport: approval.
        # * BackendReport: backend approval.
        self.report_type = report_type
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_id is not None:
            result['ApprovalId'] = self.approval_id

        if self.effect_status is not None:
            result['EffectStatus'] = self.effect_status

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalId') is not None:
            self.approval_id = m.get('ApprovalId')

        if m.get('EffectStatus') is not None:
            self.effect_status = m.get('EffectStatus')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

