# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeScalingActivityDetailResponseBody(DaraModel):
    def __init__(
        self,
        detail: str = None,
        request_id: str = None,
        scaling_activity_id: str = None,
    ):
        # The details of the scaling activity. The result of a scaling activity is either successful or failed. If the scaling activity is rejected, no scaling activity details are returned.
        self.detail = detail
        # The ID of the request.
        self.request_id = request_id
        # The ID of the scaling activity.
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')

        return self

