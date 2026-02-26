# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefundReason(DaraModel):
    def __init__(
        self,
        proof_required: bool = None,
        reason_text_id: str = None,
        reason_tips: str = None,
        refund_desc_required: bool = None,
    ):
        self.proof_required = proof_required
        self.reason_text_id = reason_text_id
        self.reason_tips = reason_tips
        self.refund_desc_required = refund_desc_required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.proof_required is not None:
            result['proofRequired'] = self.proof_required

        if self.reason_text_id is not None:
            result['reasonTextId'] = self.reason_text_id

        if self.reason_tips is not None:
            result['reasonTips'] = self.reason_tips

        if self.refund_desc_required is not None:
            result['refundDescRequired'] = self.refund_desc_required

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('proofRequired') is not None:
            self.proof_required = m.get('proofRequired')

        if m.get('reasonTextId') is not None:
            self.reason_text_id = m.get('reasonTextId')

        if m.get('reasonTips') is not None:
            self.reason_tips = m.get('reasonTips')

        if m.get('refundDescRequired') is not None:
            self.refund_desc_required = m.get('refundDescRequired')

        return self

