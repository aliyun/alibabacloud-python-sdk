# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class PbcInvokeReviewListResult(DaraModel):
    def __init__(
        self,
        pbc_invoke_reviews: List[main_models.PbcInvokeReview] = None,
        request_id: str = None,
    ):
        self.pbc_invoke_reviews = pbc_invoke_reviews
        self.request_id = request_id

    def validate(self):
        if self.pbc_invoke_reviews:
            for v1 in self.pbc_invoke_reviews:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['pbcInvokeReviews'] = []
        if self.pbc_invoke_reviews is not None:
            for k1 in self.pbc_invoke_reviews:
                result['pbcInvokeReviews'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pbc_invoke_reviews = []
        if m.get('pbcInvokeReviews') is not None:
            for k1 in m.get('pbcInvokeReviews'):
                temp_model = main_models.PbcInvokeReview()
                self.pbc_invoke_reviews.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

