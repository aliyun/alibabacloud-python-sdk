# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class ReviewerListResult(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        reviewers: List[main_models.Reviewer] = None,
    ):
        self.request_id = request_id
        self.reviewers = reviewers

    def validate(self):
        if self.reviewers:
            for v1 in self.reviewers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['reviewers'] = []
        if self.reviewers is not None:
            for k1 in self.reviewers:
                result['reviewers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.reviewers = []
        if m.get('reviewers') is not None:
            for k1 in m.get('reviewers'):
                temp_model = main_models.Reviewer()
                self.reviewers.append(temp_model.from_map(k1))

        return self

