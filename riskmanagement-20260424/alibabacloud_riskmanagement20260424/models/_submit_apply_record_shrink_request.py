# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitApplyRecordShrinkRequest(DaraModel):
    def __init__(
        self,
        apply_request: str = None,
        commitment_letter: str = None,
        description: str = None,
        event_id_list_shrink: str = None,
        qualification_proof: str = None,
        trial: bool = None,
    ):
        # This parameter is required.
        self.apply_request = apply_request
        self.commitment_letter = commitment_letter
        self.description = description
        self.event_id_list_shrink = event_id_list_shrink
        self.qualification_proof = qualification_proof
        self.trial = trial

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_request is not None:
            result['ApplyRequest'] = self.apply_request

        if self.commitment_letter is not None:
            result['CommitmentLetter'] = self.commitment_letter

        if self.description is not None:
            result['Description'] = self.description

        if self.event_id_list_shrink is not None:
            result['EventIdList'] = self.event_id_list_shrink

        if self.qualification_proof is not None:
            result['QualificationProof'] = self.qualification_proof

        if self.trial is not None:
            result['Trial'] = self.trial

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyRequest') is not None:
            self.apply_request = m.get('ApplyRequest')

        if m.get('CommitmentLetter') is not None:
            self.commitment_letter = m.get('CommitmentLetter')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EventIdList') is not None:
            self.event_id_list_shrink = m.get('EventIdList')

        if m.get('QualificationProof') is not None:
            self.qualification_proof = m.get('QualificationProof')

        if m.get('Trial') is not None:
            self.trial = m.get('Trial')

        return self

