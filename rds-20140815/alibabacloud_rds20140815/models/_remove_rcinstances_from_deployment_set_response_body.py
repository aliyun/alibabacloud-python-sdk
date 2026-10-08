# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class RemoveRCInstancesFromDeploymentSetResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[main_models.RemoveRCInstancesFromDeploymentSetResponseBodyResults] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The call results of the operation.
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.RemoveRCInstancesFromDeploymentSetResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self

class RemoveRCInstancesFromDeploymentSetResponseBodyResults(DaraModel):
    def __init__(
        self,
        rcinstance_id: str = None,
        status: str = None,
    ):
        # The instance ID.
        self.rcinstance_id = rcinstance_id
        # The node status. Valid values:
        # * **Success**: Succeeded.
        # * **Failed**: Failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rcinstance_id is not None:
            result['RCInstanceId'] = self.rcinstance_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RCInstanceId') is not None:
            self.rcinstance_id = m.get('RCInstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

