# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class ForkReviewListResult(DaraModel):
    def __init__(
        self,
        fork_reviews: List[main_models.ForkReview] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.fork_reviews = fork_reviews
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.fork_reviews:
            for v1 in self.fork_reviews:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['forkReviews'] = []
        if self.fork_reviews is not None:
            for k1 in self.fork_reviews:
                result['forkReviews'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fork_reviews = []
        if m.get('forkReviews') is not None:
            for k1 in m.get('forkReviews'):
                temp_model = main_models.ForkReview()
                self.fork_reviews.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

