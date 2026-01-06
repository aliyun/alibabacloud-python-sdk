# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterHealthStatusResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        cs: main_models.DescribeDBClusterHealthStatusResponseBodyCS = None,
        executor: main_models.DescribeDBClusterHealthStatusResponseBodyExecutor = None,
        instance_status: str = None,
        request_id: str = None,
        worker: main_models.DescribeDBClusterHealthStatusResponseBodyWorker = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The access nodes of the queried cluster.
        self.cs = cs
        # The compute node groups of the queried cluster.
        self.executor = executor
        # The health state of the cluster. Valid values:
        # 
        # *   **RISK**
        # *   **NORMAL**
        # *   **UNAVAILABLE**
        # 
        # >  When the states of the access nodes, compute node groups, and storage node groups of a cluster are all **NORMAL** and a connection to the cluster is established, the state of the cluster is **NORMAL**. When the state of the access nodes, compute node groups, or storage node groups of the cluster is **RISK**, the state of the cluster is **RISK**. When the state of the access nodes, compute node groups, or storage node groups of the cluster is **UNAVAILABLE**, the state of the cluster is **UNAVAILABLE**.
        self.instance_status = instance_status
        # The request ID.
        self.request_id = request_id
        # The storage node groups of the queried cluster.
        self.worker = worker

    def validate(self):
        if self.cs:
            self.cs.validate()
        if self.executor:
            self.executor.validate()
        if self.worker:
            self.worker.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.cs is not None:
            result['CS'] = self.cs.to_map()

        if self.executor is not None:
            result['Executor'] = self.executor.to_map()

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.worker is not None:
            result['Worker'] = self.worker.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('CS') is not None:
            temp_model = main_models.DescribeDBClusterHealthStatusResponseBodyCS()
            self.cs = temp_model.from_map(m.get('CS'))

        if m.get('Executor') is not None:
            temp_model = main_models.DescribeDBClusterHealthStatusResponseBodyExecutor()
            self.executor = temp_model.from_map(m.get('Executor'))

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Worker') is not None:
            temp_model = main_models.DescribeDBClusterHealthStatusResponseBodyWorker()
            self.worker = temp_model.from_map(m.get('Worker'))

        return self

class DescribeDBClusterHealthStatusResponseBodyWorker(DaraModel):
    def __init__(
        self,
        active_count: int = None,
        expected_count: int = None,
        risk_count: int = None,
        status: str = None,
        unavailable_count: int = None,
    ):
        # The number of healthy storage node groups.
        self.active_count = active_count
        # The total number of storage node groups.
        self.expected_count = expected_count
        # The number of risky storage node groups.
        self.risk_count = risk_count
        # The health state of storage node groups. Valid values:
        # 
        # *   **RISK**
        # *   **NORMAL**
        # *   **UNAVAILABLE**
        self.status = status
        # The number of unavailable storage node groups.
        self.unavailable_count = unavailable_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_count is not None:
            result['ActiveCount'] = self.active_count

        if self.expected_count is not None:
            result['ExpectedCount'] = self.expected_count

        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count

        if self.status is not None:
            result['Status'] = self.status

        if self.unavailable_count is not None:
            result['UnavailableCount'] = self.unavailable_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveCount') is not None:
            self.active_count = m.get('ActiveCount')

        if m.get('ExpectedCount') is not None:
            self.expected_count = m.get('ExpectedCount')

        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UnavailableCount') is not None:
            self.unavailable_count = m.get('UnavailableCount')

        return self

class DescribeDBClusterHealthStatusResponseBodyExecutor(DaraModel):
    def __init__(
        self,
        active_count: int = None,
        expected_count: int = None,
        risk_count: int = None,
        status: str = None,
        unavailable_count: int = None,
    ):
        # The number of healthy access nodes.
        self.active_count = active_count
        # The total number of compute nodes.
        self.expected_count = expected_count
        # The number of risky nodes.
        self.risk_count = risk_count
        # The health state of compute node groups. Valid values:
        # 
        # *   **RISK**
        # *   **NORMAL**
        # *   **UNAVAILABLE**
        self.status = status
        # The number of unavailable access nodes.
        self.unavailable_count = unavailable_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_count is not None:
            result['ActiveCount'] = self.active_count

        if self.expected_count is not None:
            result['ExpectedCount'] = self.expected_count

        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count

        if self.status is not None:
            result['Status'] = self.status

        if self.unavailable_count is not None:
            result['UnavailableCount'] = self.unavailable_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveCount') is not None:
            self.active_count = m.get('ActiveCount')

        if m.get('ExpectedCount') is not None:
            self.expected_count = m.get('ExpectedCount')

        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UnavailableCount') is not None:
            self.unavailable_count = m.get('UnavailableCount')

        return self

class DescribeDBClusterHealthStatusResponseBodyCS(DaraModel):
    def __init__(
        self,
        active_count: int = None,
        expected_count: int = None,
        risk_count: int = None,
        status: str = None,
        unavailable_count: int = None,
    ):
        # The number of healthy access nodes.
        self.active_count = active_count
        # The total number of access nodes.
        self.expected_count = expected_count
        # The number of risky nodes.
        self.risk_count = risk_count
        # The health state of access nodes. Valid values:
        # 
        # *   **RISK**
        # *   **NORMAL**
        # *   **UNAVAILABLE**
        self.status = status
        # The number of unavailable access nodes.
        self.unavailable_count = unavailable_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_count is not None:
            result['ActiveCount'] = self.active_count

        if self.expected_count is not None:
            result['ExpectedCount'] = self.expected_count

        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count

        if self.status is not None:
            result['Status'] = self.status

        if self.unavailable_count is not None:
            result['UnavailableCount'] = self.unavailable_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveCount') is not None:
            self.active_count = m.get('ActiveCount')

        if m.get('ExpectedCount') is not None:
            self.expected_count = m.get('ExpectedCount')

        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UnavailableCount') is not None:
            self.unavailable_count = m.get('UnavailableCount')

        return self

