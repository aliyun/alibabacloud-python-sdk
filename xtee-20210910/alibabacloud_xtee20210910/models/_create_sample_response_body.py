# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class CreateSampleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.CreateSampleResponseBodyResultObject = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.CreateSampleResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class CreateSampleResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        community_count: int = None,
        fail_count: int = None,
        recall_probability: str = None,
        risk_density: str = None,
        sample_count: int = None,
        success_count: int = None,
    ):
        # Number of colored groups
        self.community_count = community_count
        # Number of failed samples
        self.fail_count = fail_count
        # Recall probability
        self.recall_probability = recall_probability
        # Risk density
        self.risk_density = risk_density
        # Number of samples
        self.sample_count = sample_count
        # Number of successful samples
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.community_count is not None:
            result['communityCount'] = self.community_count

        if self.fail_count is not None:
            result['failCount'] = self.fail_count

        if self.recall_probability is not None:
            result['recallProbability'] = self.recall_probability

        if self.risk_density is not None:
            result['riskDensity'] = self.risk_density

        if self.sample_count is not None:
            result['sampleCount'] = self.sample_count

        if self.success_count is not None:
            result['successCount'] = self.success_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('communityCount') is not None:
            self.community_count = m.get('communityCount')

        if m.get('failCount') is not None:
            self.fail_count = m.get('failCount')

        if m.get('recallProbability') is not None:
            self.recall_probability = m.get('recallProbability')

        if m.get('riskDensity') is not None:
            self.risk_density = m.get('riskDensity')

        if m.get('sampleCount') is not None:
            self.sample_count = m.get('sampleCount')

        if m.get('successCount') is not None:
            self.success_count = m.get('successCount')

        return self

