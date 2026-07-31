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
        # Details of the authentication failure.
        self.access_denied_detail = access_denied_detail
        # The health status of the instance access nodes.
        self.cs = cs
        # The health status of the executor groups.
        self.executor = executor
        # The health status of the cluster. Valid values:
        # 
        # - **RISK**: The cluster is at risk.
        # 
        # - **NORMAL**: The cluster is healthy.
        # 
        # - **UNAVAILABLE**: The cluster is unavailable.
        # 
        # > The cluster health status is considered **NORMAL** only if the instance access nodes, executor groups, and worker node groups are all **NORMAL**, and the instance is responsive. If any of these components has a **RISK** status, the cluster status is **RISK**. If any component has an **UNAVAILABLE** status, the cluster status is **UNAVAILABLE**.
        self.instance_status = instance_status
        # The request ID.
        self.request_id = request_id
        # The health status of the worker node groups.
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
        # The number of healthy worker node groups.
        self.active_count = active_count
        # The total number of worker node groups.
        self.expected_count = expected_count
        # The number of worker node groups at risk.
        self.risk_count = risk_count
        # The health status of the worker node groups. Valid values:
        # 
        # - **RISK**: The worker node groups are at risk.
        # 
        # - **NORMAL**: The worker node groups are healthy.
        # 
        # - **UNAVAILABLE**: The worker node groups are unavailable.
        self.status = status
        # The number of unavailable worker node groups.
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
        # The number of healthy executor nodes.
        self.active_count = active_count
        # The total number of executor nodes.
        self.expected_count = expected_count
        # The number of executor nodes at risk.
        self.risk_count = risk_count
        # The health status of the executor groups. Valid values:
        # 
        # - **RISK**: The executor groups are at risk.
        # 
        # - **NORMAL**: The executor groups are healthy.
        # 
        # - **UNAVAILABLE**: The executor groups are unavailable.
        self.status = status
        # The number of unavailable executor nodes.
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
        # The number of healthy instance access nodes.
        self.active_count = active_count
        # The total number of instance access nodes.
        self.expected_count = expected_count
        # The number of instance access nodes at risk.
        self.risk_count = risk_count
        # The health status of the instance access nodes. Valid values:
        # 
        # - **RISK**: The instance access nodes are at risk.
        # 
        # - **NORMAL**: The instance access nodes are healthy.
        # 
        # - **UNAVAILABLE**: The instance access nodes are unavailable.
        self.status = status
        # The number of unavailable instance access nodes.
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

