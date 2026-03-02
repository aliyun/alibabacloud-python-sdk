# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FeedbackReviewCmd(DaraModel):
    def __init__(
        self,
        feedback_pbc_api: str = None,
        feedback_pbc_instruction: str = None,
        feedback_pbc_schema: str = None,
        feedback_security: str = None,
        feedback_service_available: str = None,
        review_id: int = None,
        status: str = None,
    ):
        # This parameter is required.
        self.feedback_pbc_api = feedback_pbc_api
        # This parameter is required.
        self.feedback_pbc_instruction = feedback_pbc_instruction
        # This parameter is required.
        self.feedback_pbc_schema = feedback_pbc_schema
        # This parameter is required.
        self.feedback_security = feedback_security
        # This parameter is required.
        self.feedback_service_available = feedback_service_available
        # This parameter is required.
        self.review_id = review_id
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feedback_pbc_api is not None:
            result['feedbackPbcAPI'] = self.feedback_pbc_api

        if self.feedback_pbc_instruction is not None:
            result['feedbackPbcInstruction'] = self.feedback_pbc_instruction

        if self.feedback_pbc_schema is not None:
            result['feedbackPbcSchema'] = self.feedback_pbc_schema

        if self.feedback_security is not None:
            result['feedbackSecurity'] = self.feedback_security

        if self.feedback_service_available is not None:
            result['feedbackServiceAvailable'] = self.feedback_service_available

        if self.review_id is not None:
            result['reviewId'] = self.review_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('feedbackPbcAPI') is not None:
            self.feedback_pbc_api = m.get('feedbackPbcAPI')

        if m.get('feedbackPbcInstruction') is not None:
            self.feedback_pbc_instruction = m.get('feedbackPbcInstruction')

        if m.get('feedbackPbcSchema') is not None:
            self.feedback_pbc_schema = m.get('feedbackPbcSchema')

        if m.get('feedbackSecurity') is not None:
            self.feedback_security = m.get('feedbackSecurity')

        if m.get('feedbackServiceAvailable') is not None:
            self.feedback_service_available = m.get('feedbackServiceAvailable')

        if m.get('reviewId') is not None:
            self.review_id = m.get('reviewId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

