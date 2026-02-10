# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDefenceCountResponseBody(DaraModel):
    def __init__(
        self,
        defence_count_15days: int = None,
        defence_count_total: int = None,
        request_id: str = None,
        suspicious_dealt_count: int = None,
        tamper_proof_15days: int = None,
        tamper_proof_total: int = None,
    ):
        # The number of handled alerts of the precise defense type in the last 15 days.
        self.defence_count_15days = defence_count_15days
        # The number of handled alerts of the precision defense type.
        self.defence_count_total = defence_count_total
        # The request ID.
        self.request_id = request_id
        # The number of handled security alerts of Cloud Security Center.
        self.suspicious_dealt_count = suspicious_dealt_count
        # The number of handled alerts of the web tamper proofing type in the last 15 days.
        self.tamper_proof_15days = tamper_proof_15days
        # The number of handled alerts of the web tamper proofing type.
        self.tamper_proof_total = tamper_proof_total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defence_count_15days is not None:
            result['DefenceCount15Days'] = self.defence_count_15days

        if self.defence_count_total is not None:
            result['DefenceCountTotal'] = self.defence_count_total

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.suspicious_dealt_count is not None:
            result['SuspiciousDealtCount'] = self.suspicious_dealt_count

        if self.tamper_proof_15days is not None:
            result['TamperProof15Days'] = self.tamper_proof_15days

        if self.tamper_proof_total is not None:
            result['TamperProofTotal'] = self.tamper_proof_total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenceCount15Days') is not None:
            self.defence_count_15days = m.get('DefenceCount15Days')

        if m.get('DefenceCountTotal') is not None:
            self.defence_count_total = m.get('DefenceCountTotal')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuspiciousDealtCount') is not None:
            self.suspicious_dealt_count = m.get('SuspiciousDealtCount')

        if m.get('TamperProof15Days') is not None:
            self.tamper_proof_15days = m.get('TamperProof15Days')

        if m.get('TamperProofTotal') is not None:
            self.tamper_proof_total = m.get('TamperProofTotal')

        return self

