# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeMonitoringAgentProcessesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        node_processes: main_models.DescribeMonitoringAgentProcessesResponseBodyNodeProcesses = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        # 
        # > A status code of 200 indicates that the request was successful.
        self.code = code
        # The error message.
        self.message = message
        self.node_processes = node_processes
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful. Valid values:
        # 
        # - true: The operation was successful.
        # 
        # - false: The operation failed.
        self.success = success

    def validate(self):
        if self.node_processes:
            self.node_processes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.node_processes is not None:
            result['NodeProcesses'] = self.node_processes.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NodeProcesses') is not None:
            temp_model = main_models.DescribeMonitoringAgentProcessesResponseBodyNodeProcesses()
            self.node_processes = temp_model.from_map(m.get('NodeProcesses'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeMonitoringAgentProcessesResponseBodyNodeProcesses(DaraModel):
    def __init__(
        self,
        node_process: List[main_models.DescribeMonitoringAgentProcessesResponseBodyNodeProcessesNodeProcess] = None,
    ):
        self.node_process = node_process

    def validate(self):
        if self.node_process:
            for v1 in self.node_process:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodeProcess'] = []
        if self.node_process is not None:
            for k1 in self.node_process:
                result['NodeProcess'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_process = []
        if m.get('NodeProcess') is not None:
            for k1 in m.get('NodeProcess'):
                temp_model = main_models.DescribeMonitoringAgentProcessesResponseBodyNodeProcessesNodeProcess()
                self.node_process.append(temp_model.from_map(k1))

        return self

class DescribeMonitoringAgentProcessesResponseBodyNodeProcessesNodeProcess(DaraModel):
    def __init__(
        self,
        command: str = None,
        group_id: str = None,
        instance_id: str = None,
        process_id: int = None,
        process_name: str = None,
        process_user: str = None,
    ):
        self.command = command
        self.group_id = group_id
        self.instance_id = instance_id
        self.process_id = process_id
        self.process_name = process_name
        self.process_user = process_user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['Command'] = self.command

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.process_user is not None:
            result['ProcessUser'] = self.process_user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('ProcessUser') is not None:
            self.process_user = m.get('ProcessUser')

        return self

