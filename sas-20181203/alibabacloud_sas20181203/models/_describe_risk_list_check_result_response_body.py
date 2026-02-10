# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeRiskListCheckResultResponseBody(DaraModel):
    def __init__(
        self,
        list: List[main_models.DescribeRiskListCheckResultResponseBodyList] = None,
        request_id: str = None,
    ):
        # The number of risk items for each cloud service.
        self.list = list
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.DescribeRiskListCheckResultResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRiskListCheckResultResponseBodyList(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        risk_count: int = None,
    ):
        # The instance ID of the cloud service.
        self.instance_id = instance_id
        # The total number of risk items detected in the current cloud service.
        self.risk_count = risk_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.risk_count is not None:
            result['riskCount'] = self.risk_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('riskCount') is not None:
            self.risk_count = m.get('riskCount')

        return self

