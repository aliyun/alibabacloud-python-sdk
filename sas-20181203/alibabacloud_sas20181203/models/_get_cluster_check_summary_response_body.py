# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetClusterCheckSummaryResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetClusterCheckSummaryResponseBodyData = None,
        request_id: str = None,
    ):
        # Return data.
        self.data = data
        # Request ID.
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
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetClusterCheckSummaryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetClusterCheckSummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        not_pass_count: int = None,
        not_pass_high_count: int = None,
        not_pass_low_count: int = None,
        not_pass_medium_count: int = None,
    ):
        # Total number of items that failed the check.
        self.not_pass_count = not_pass_count
        # Number of high-risk inspection items that have not passed.
        self.not_pass_high_count = not_pass_high_count
        # Number of low-risk inspection items that have not passed.
        self.not_pass_low_count = not_pass_low_count
        # Number of medium-risk failed inspection items.
        self.not_pass_medium_count = not_pass_medium_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.not_pass_count is not None:
            result['NotPassCount'] = self.not_pass_count

        if self.not_pass_high_count is not None:
            result['NotPassHighCount'] = self.not_pass_high_count

        if self.not_pass_low_count is not None:
            result['NotPassLowCount'] = self.not_pass_low_count

        if self.not_pass_medium_count is not None:
            result['NotPassMediumCount'] = self.not_pass_medium_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotPassCount') is not None:
            self.not_pass_count = m.get('NotPassCount')

        if m.get('NotPassHighCount') is not None:
            self.not_pass_high_count = m.get('NotPassHighCount')

        if m.get('NotPassLowCount') is not None:
            self.not_pass_low_count = m.get('NotPassLowCount')

        if m.get('NotPassMediumCount') is not None:
            self.not_pass_medium_count = m.get('NotPassMediumCount')

        return self

