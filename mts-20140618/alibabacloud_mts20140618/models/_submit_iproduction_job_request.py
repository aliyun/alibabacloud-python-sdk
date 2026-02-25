# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitIProductionJobRequest(DaraModel):
    def __init__(
        self,
        function_name: str = None,
        input: str = None,
        job_params: str = None,
        model_id: str = None,
        notify_url: str = None,
        output: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pipeline_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        schedule_params: str = None,
        user_data: str = None,
    ):
        # This parameter is required.
        self.function_name = function_name
        self.input = input
        self.job_params = job_params
        self.model_id = model_id
        self.notify_url = notify_url
        self.output = output
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.pipeline_id = pipeline_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.schedule_params = schedule_params
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

        if self.job_params is not None:
            result['JobParams'] = self.job_params

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url

        if self.output is not None:
            result['Output'] = self.output

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.schedule_params is not None:
            result['ScheduleParams'] = self.schedule_params

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('JobParams') is not None:
            self.job_params = m.get('JobParams')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScheduleParams') is not None:
            self.schedule_params = m.get('ScheduleParams')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

