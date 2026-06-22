# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListScriptsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        scripts: List[main_models.ListScriptsResponseBodyScripts] = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned in the request.
        self.max_results = max_results
        # The token that is used to start the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The list of scripts.
        self.scripts = scripts
        # The total number of entries that meet the request conditions.
        self.total_count = total_count

    def validate(self):
        if self.scripts:
            for v1 in self.scripts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Scripts'] = []
        if self.scripts is not None:
            for k1 in self.scripts:
                result['Scripts'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.scripts = []
        if m.get('Scripts') is not None:
            for k1 in m.get('Scripts'):
                temp_model = main_models.ListScriptsResponseBodyScripts()
                self.scripts.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListScriptsResponseBodyScripts(DaraModel):
    def __init__(
        self,
        action: str = None,
        end_time: int = None,
        execution_fail_strategy: str = None,
        execution_moment: str = None,
        execution_state: str = None,
        last_update_time: int = None,
        node_selector: main_models.NodeSelector = None,
        region_id: str = None,
        script_args: str = None,
        script_id: str = None,
        script_name: str = None,
        script_path: str = None,
        start_time: int = None,
    ):
        # The name of the API.
        self.action = action
        # The time when the execution ended. This parameter is returned only when ScriptType is set to NORMAL.
        self.end_time = end_time
        # The policy used to handle an execution failure. Valid values:
        # 
        # - FAILED_CONTINUE: Continue the execution.
        # 
        # - FAILED_BLOCK: Block the execution.
        self.execution_fail_strategy = execution_fail_strategy
        # The time to execute the script. Valid values:
        # 
        # - BEFORE_INSTALL: before application installation.
        # 
        # - AFTER_STARTED: after application startup.
        self.execution_moment = execution_moment
        # The execution status of the script. This parameter is returned only when `ScriptType` is set to `NORMAL`. Valid values:
        # 
        # - SCRIPT_COMPLETED: The script is successfully executed.
        # 
        # - SCRIPT_SUBMISSION_FAILED: The script fails to be executed.
        # 
        # - SCRIPT_RUNNING: The script is being executed.
        self.execution_state = execution_state
        # The time when the script was last updated.
        self.last_update_time = last_update_time
        # The node selector.
        self.node_selector = node_selector
        # The region ID.
        self.region_id = region_id
        # The runtime parameters of the script.
        self.script_args = script_args
        # The script ID.
        self.script_id = script_id
        # The script name.
        self.script_name = script_name
        # The script path.
        self.script_path = script_path
        # The time when the execution started. This parameter is returned only when ScriptType is set to NORMAL.
        self.start_time = start_time

    def validate(self):
        if self.node_selector:
            self.node_selector.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.execution_fail_strategy is not None:
            result['ExecutionFailStrategy'] = self.execution_fail_strategy

        if self.execution_moment is not None:
            result['ExecutionMoment'] = self.execution_moment

        if self.execution_state is not None:
            result['ExecutionState'] = self.execution_state

        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time

        if self.node_selector is not None:
            result['NodeSelector'] = self.node_selector.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.script_args is not None:
            result['ScriptArgs'] = self.script_args

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.script_name is not None:
            result['ScriptName'] = self.script_name

        if self.script_path is not None:
            result['ScriptPath'] = self.script_path

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExecutionFailStrategy') is not None:
            self.execution_fail_strategy = m.get('ExecutionFailStrategy')

        if m.get('ExecutionMoment') is not None:
            self.execution_moment = m.get('ExecutionMoment')

        if m.get('ExecutionState') is not None:
            self.execution_state = m.get('ExecutionState')

        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')

        if m.get('NodeSelector') is not None:
            temp_model = main_models.NodeSelector()
            self.node_selector = temp_model.from_map(m.get('NodeSelector'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScriptArgs') is not None:
            self.script_args = m.get('ScriptArgs')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')

        if m.get('ScriptPath') is not None:
            self.script_path = m.get('ScriptPath')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

