# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetReductionProposalResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetReductionProposalResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetReductionProposalResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetReductionProposalResponseBodyData(DaraModel):
    def __init__(
        self,
        reduction: str = None,
        reduction_evaluation: str = None,
    ):
        # Proactive carbon reduction recommendations and advice.
        self.reduction = reduction
        # Active carbon reduction assessment.
        self.reduction_evaluation = reduction_evaluation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reduction is not None:
            result['reduction'] = self.reduction

        if self.reduction_evaluation is not None:
            result['reductionEvaluation'] = self.reduction_evaluation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reduction') is not None:
            self.reduction = m.get('reduction')

        if m.get('reductionEvaluation') is not None:
            self.reduction_evaluation = m.get('reductionEvaluation')

        return self

