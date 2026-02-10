# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImageStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        instance_count: int = None,
        request_id: str = None,
        risk_instance_count: int = None,
    ):
        # The number of container images in your assets. Only Container Registry Enterprise Edition instances are counted.
        self.instance_count = instance_count
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The number of container images that have security risks. Only Container Registry Enterprise Edition instances are counted.
        self.risk_instance_count = risk_instance_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_instance_count is not None:
            result['RiskInstanceCount'] = self.risk_instance_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskInstanceCount') is not None:
            self.risk_instance_count = m.get('RiskInstanceCount')

        return self

