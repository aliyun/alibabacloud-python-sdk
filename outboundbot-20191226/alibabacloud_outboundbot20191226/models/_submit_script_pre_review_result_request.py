# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitScriptPreReviewResultRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        record_id: str = None,
        reject_reason: str = None,
        review_result: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the script review record.
        # 
        # This parameter is required.
        self.record_id = record_id
        # The reason for pre-review rejection. This parameter is required when ReviewResult is set to REJECT.
        self.reject_reason = reject_reason
        # The pre-review result. Valid values: PASS (approved) and REJECT (rejected). The value is not case-sensitive.
        # 
        # This parameter is required.
        self.review_result = review_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.reject_reason is not None:
            result['RejectReason'] = self.reject_reason

        if self.review_result is not None:
            result['ReviewResult'] = self.review_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('RejectReason') is not None:
            self.reject_reason = m.get('RejectReason')

        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')

        return self

