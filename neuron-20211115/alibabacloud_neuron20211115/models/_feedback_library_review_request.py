# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FeedbackLibraryReviewRequest(DaraModel):
    def __init__(
        self,
        approve: str = None,
        feedback: str = None,
        review_id: int = None,
    ):
        self.approve = approve
        self.feedback = feedback
        self.review_id = review_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approve is not None:
            result['approve'] = self.approve

        if self.feedback is not None:
            result['feedback'] = self.feedback

        if self.review_id is not None:
            result['reviewId'] = self.review_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('approve') is not None:
            self.approve = m.get('approve')

        if m.get('feedback') is not None:
            self.feedback = m.get('feedback')

        if m.get('reviewId') is not None:
            self.review_id = m.get('reviewId')

        return self

