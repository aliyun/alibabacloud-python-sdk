# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class DescribeDeploymentJobStatusResponseBody(DaraModel):
    def __init__(
        self,
        buy_count: int = None,
        cert_count: int = None,
        cost_count: int = None,
        failed_count: int = None,
        match_worker_count: int = None,
        product_worker_count: List[main_models.DescribeDeploymentJobStatusResponseBodyProductWorkerCount] = None,
        request_id: str = None,
        resource_count: int = None,
        rollback_count: int = None,
        rollback_failed_count: int = None,
        rollback_success_count: int = None,
        success_count: int = None,
        use_count: int = None,
        worker_count: int = None,
    ):
        # The total number of purchased resources.
        self.buy_count = buy_count
        # The number of certificates involved in the deployment task.
        self.cert_count = cert_count
        # The number of resources consumed by worker tasks.
        self.cost_count = cost_count
        # The number of failed worker tasks, excluding rollback tasks.
        self.failed_count = failed_count
        # The total number of worker tasks that match the certificate.
        self.match_worker_count = match_worker_count
        # The number of cloud resources to which certificates are deployed in the deployment task.
        self.product_worker_count = product_worker_count
        # The request ID.
        self.request_id = request_id
        # The total number of resources.
        self.resource_count = resource_count
        # The number of worker tasks that are rolled backed.
        self.rollback_count = rollback_count
        # The number of worker tasks that failed to be rolled back.
        self.rollback_failed_count = rollback_failed_count
        # The number of worker tasks that are successfully rolled back.
        self.rollback_success_count = rollback_success_count
        # The number of successful worker tasks, excluding rollback tasks.
        self.success_count = success_count
        # The total number of used resources.
        self.use_count = use_count
        # The total number of resources to which certificate are deployed in the current cloud service. The value indicates the total number of worker tasks.
        self.worker_count = worker_count

    def validate(self):
        if self.product_worker_count:
            for v1 in self.product_worker_count:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buy_count is not None:
            result['BuyCount'] = self.buy_count

        if self.cert_count is not None:
            result['CertCount'] = self.cert_count

        if self.cost_count is not None:
            result['CostCount'] = self.cost_count

        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.match_worker_count is not None:
            result['MatchWorkerCount'] = self.match_worker_count

        result['ProductWorkerCount'] = []
        if self.product_worker_count is not None:
            for k1 in self.product_worker_count:
                result['ProductWorkerCount'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count

        if self.rollback_count is not None:
            result['RollbackCount'] = self.rollback_count

        if self.rollback_failed_count is not None:
            result['RollbackFailedCount'] = self.rollback_failed_count

        if self.rollback_success_count is not None:
            result['RollbackSuccessCount'] = self.rollback_success_count

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.use_count is not None:
            result['UseCount'] = self.use_count

        if self.worker_count is not None:
            result['WorkerCount'] = self.worker_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyCount') is not None:
            self.buy_count = m.get('BuyCount')

        if m.get('CertCount') is not None:
            self.cert_count = m.get('CertCount')

        if m.get('CostCount') is not None:
            self.cost_count = m.get('CostCount')

        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('MatchWorkerCount') is not None:
            self.match_worker_count = m.get('MatchWorkerCount')

        self.product_worker_count = []
        if m.get('ProductWorkerCount') is not None:
            for k1 in m.get('ProductWorkerCount'):
                temp_model = main_models.DescribeDeploymentJobStatusResponseBodyProductWorkerCount()
                self.product_worker_count.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')

        if m.get('RollbackCount') is not None:
            self.rollback_count = m.get('RollbackCount')

        if m.get('RollbackFailedCount') is not None:
            self.rollback_failed_count = m.get('RollbackFailedCount')

        if m.get('RollbackSuccessCount') is not None:
            self.rollback_success_count = m.get('RollbackSuccessCount')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('UseCount') is not None:
            self.use_count = m.get('UseCount')

        if m.get('WorkerCount') is not None:
            self.worker_count = m.get('WorkerCount')

        return self

class DescribeDeploymentJobStatusResponseBodyProductWorkerCount(DaraModel):
    def __init__(
        self,
        count: int = None,
        product_name: str = None,
    ):
        # The total number of resources of a cloud service in the deployment task.
        self.count = count
        # The name of the cloud service. Valid values:
        # 
        # *   **SLB**: Classic Load Balancer (CLB). This value is supported only at the China site (aliyun.com).
        # *   **LIVE**: ApsaraVideo Live. This value is supported only at the China site (aliyun.com).
        # *   **webHosting**: Cloud Web Hosting. This value is supported only at the China site (aliyun.com).
        # *   **VOD**: ApsaraVideo VOD. This value is supported only at the China site (aliyun.com).
        # *   **CR**: Container Registry. This value is supported only at the China site (aliyun.com).
        # *   **DCDN**: Dynamic Content Delivery Network (DCDN).
        # *   **DDOS**: Anti-DDoS.
        # *   **CDN**: Alibaba Cloud CDN (CDN).
        # *   **ALB**: Application Load Balancer (ALB).
        # *   **APIGateway**: API Gateway.
        # *   **FC**: Function Compute.
        # *   **GA**: Global Accelerator (GA).
        # *   **MSE**: Microservices Engine (MSE).
        # *   **NLB**: Network Load Balancer (NLB).
        # *   **OSS**: Object Storage Service (OSS).
        # *   **SAE**: Serverless App Engine (SAE).
        # *   **TencentCDN**: Tencent Cloud Content Delivery Network (CDN).
        # *   **WAF**: Web Application Firewall (WAF).
        self.product_name = product_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        return self

