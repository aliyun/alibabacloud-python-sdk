# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class GetStackExecutionResultResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        stack_results: List[main_models.GetStackExecutionResultResponseBodyStackResults] = None,
        trigger_id: str = None,
        triggered_status: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.stack_results = stack_results
        self.trigger_id = trigger_id
        self.triggered_status = triggered_status

    def validate(self):
        if self.stack_results:
            for v1 in self.stack_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['stackResults'] = []
        if self.stack_results is not None:
            for k1 in self.stack_results:
                result['stackResults'].append(k1.to_map() if k1 else None)

        if self.trigger_id is not None:
            result['triggerId'] = self.trigger_id

        if self.triggered_status is not None:
            result['triggeredStatus'] = self.triggered_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.stack_results = []
        if m.get('stackResults') is not None:
            for k1 in m.get('stackResults'):
                temp_model = main_models.GetStackExecutionResultResponseBodyStackResults()
                self.stack_results.append(temp_model.from_map(k1))

        if m.get('triggerId') is not None:
            self.trigger_id = m.get('triggerId')

        if m.get('triggeredStatus') is not None:
            self.triggered_status = m.get('triggeredStatus')

        return self

class GetStackExecutionResultResponseBodyStackResults(DaraModel):
    def __init__(
        self,
        deployments: List[main_models.GetStackExecutionResultResponseBodyStackResultsDeployments] = None,
        message: str = None,
        stack_id: str = None,
        stack_name: str = None,
        stack_status: str = None,
    ):
        self.deployments = deployments
        self.message = message
        self.stack_id = stack_id
        self.stack_name = stack_name
        self.stack_status = stack_status

    def validate(self):
        if self.deployments:
            for v1 in self.deployments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['deployments'] = []
        if self.deployments is not None:
            for k1 in self.deployments:
                result['deployments'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.stack_id is not None:
            result['stackId'] = self.stack_id

        if self.stack_name is not None:
            result['stackName'] = self.stack_name

        if self.stack_status is not None:
            result['stackStatus'] = self.stack_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deployments = []
        if m.get('deployments') is not None:
            for k1 in m.get('deployments'):
                temp_model = main_models.GetStackExecutionResultResponseBodyStackResultsDeployments()
                self.deployments.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('stackId') is not None:
            self.stack_id = m.get('stackId')

        if m.get('stackName') is not None:
            self.stack_name = m.get('stackName')

        if m.get('stackStatus') is not None:
            self.stack_status = m.get('stackStatus')

        return self

class GetStackExecutionResultResponseBodyStackResultsDeployments(DaraModel):
    def __init__(
        self,
        deployment_name: str = None,
        job_result: str = None,
        status: str = None,
        url: str = None,
    ):
        self.deployment_name = deployment_name
        self.job_result = job_result
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_name is not None:
            result['deploymentName'] = self.deployment_name

        if self.job_result is not None:
            result['jobResult'] = self.job_result

        if self.status is not None:
            result['status'] = self.status

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentName') is not None:
            self.deployment_name = m.get('deploymentName')

        if m.get('jobResult') is not None:
            self.job_result = m.get('jobResult')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

