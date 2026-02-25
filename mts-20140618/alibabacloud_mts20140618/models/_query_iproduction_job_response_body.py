# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryIProductionJobResponseBody(DaraModel):
    def __init__(
        self,
        function_name: str = None,
        input: str = None,
        job_id: str = None,
        job_params: str = None,
        output: str = None,
        pipeline_id: str = None,
        request_id: str = None,
        result: str = None,
        state: str = None,
        user_data: str = None,
    ):
        self.function_name = function_name
        self.input = input
        self.job_id = job_id
        self.job_params = job_params
        self.output = output
        self.pipeline_id = pipeline_id
        self.request_id = request_id
        self.result = result
        self.state = state
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        if self.input is not None:
            result['Input'] = self.input

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_params is not None:
            result['JobParams'] = self.job_params

        if self.output is not None:
            result['Output'] = self.output

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        if self.state is not None:
            result['State'] = self.state

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobParams') is not None:
            self.job_params = m.get('JobParams')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

