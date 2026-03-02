# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class AsyncDraftValidateResult(DaraModel):
    def __init__(
        self,
        draft_validation_detail: main_models.DraftValidationDetail = None,
        message: str = None,
        success: bool = None,
        ticket_status: str = None,
    ):
        self.draft_validation_detail = draft_validation_detail
        self.message = message
        self.success = success
        self.ticket_status = ticket_status

    def validate(self):
        if self.draft_validation_detail:
            self.draft_validation_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.draft_validation_detail is not None:
            result['draftValidationDetail'] = self.draft_validation_detail.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.success is not None:
            result['success'] = self.success

        if self.ticket_status is not None:
            result['ticketStatus'] = self.ticket_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('draftValidationDetail') is not None:
            temp_model = main_models.DraftValidationDetail()
            self.draft_validation_detail = temp_model.from_map(m.get('draftValidationDetail'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('ticketStatus') is not None:
            self.ticket_status = m.get('ticketStatus')

        return self

