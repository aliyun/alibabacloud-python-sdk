# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateBatchJobsRequest(DaraModel):
    def __init__(
        self,
        batch_job_description: str = None,
        batch_job_name: str = None,
        calling_number: List[str] = None,
        instance_id: str = None,
        job_file_path: str = None,
        scenario_id: str = None,
        script_id: str = None,
        strategy_json: str = None,
        submitted: bool = None,
    ):
        self.batch_job_description = batch_job_description
        # This parameter is required.
        self.batch_job_name = batch_job_name
        self.calling_number = calling_number
        # This parameter is required.
        self.instance_id = instance_id
        self.job_file_path = job_file_path
        self.scenario_id = scenario_id
        self.script_id = script_id
        self.strategy_json = strategy_json
        # This parameter is required.
        self.submitted = submitted

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_job_description is not None:
            result['BatchJobDescription'] = self.batch_job_description

        if self.batch_job_name is not None:
            result['BatchJobName'] = self.batch_job_name

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_file_path is not None:
            result['JobFilePath'] = self.job_file_path

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.strategy_json is not None:
            result['StrategyJson'] = self.strategy_json

        if self.submitted is not None:
            result['Submitted'] = self.submitted

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchJobDescription') is not None:
            self.batch_job_description = m.get('BatchJobDescription')

        if m.get('BatchJobName') is not None:
            self.batch_job_name = m.get('BatchJobName')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobFilePath') is not None:
            self.job_file_path = m.get('JobFilePath')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('StrategyJson') is not None:
            self.strategy_json = m.get('StrategyJson')

        if m.get('Submitted') is not None:
            self.submitted = m.get('Submitted')

        return self

