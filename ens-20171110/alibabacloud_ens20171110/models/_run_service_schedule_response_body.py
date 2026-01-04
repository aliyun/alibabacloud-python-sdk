# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class RunServiceScheduleResponseBody(DaraModel):
    def __init__(
        self,
        command_results: main_models.RunServiceScheduleResponseBodyCommandResults = None,
        index: int = None,
        instance_id: str = None,
        instance_ip: str = None,
        instance_port: int = None,
        request_id: str = None,
        request_repeated: str = None,
        tcp_ports: bool = None,
    ):
        # The execution results of the commands.
        self.command_results = command_results
        # The index number of the scheduled virtual device (pod).
        self.index = index
        # The ID of the scheduled instance.
        self.instance_id = instance_id
        # The IP address of the scheduled instance.
        self.instance_ip = instance_ip
        # The start port of the scheduled instance.
        self.instance_port = instance_port
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is repeated. This parameter is not returned if ServcieAction is set to Console.
        self.request_repeated = request_repeated
        # The TCP port range of the scheduled instance or container. The value is in the ${from}-$-{to} format. Example: 80-88.
        self.tcp_ports = tcp_ports

    def validate(self):
        if self.command_results:
            self.command_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_results is not None:
            result['CommandResults'] = self.command_results.to_map()

        if self.index is not None:
            result['Index'] = self.index

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip

        if self.instance_port is not None:
            result['InstancePort'] = self.instance_port

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.request_repeated is not None:
            result['RequestRepeated'] = self.request_repeated

        if self.tcp_ports is not None:
            result['TcpPorts'] = self.tcp_ports

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandResults') is not None:
            temp_model = main_models.RunServiceScheduleResponseBodyCommandResults()
            self.command_results = temp_model.from_map(m.get('CommandResults'))

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')

        if m.get('InstancePort') is not None:
            self.instance_port = m.get('InstancePort')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequestRepeated') is not None:
            self.request_repeated = m.get('RequestRepeated')

        if m.get('TcpPorts') is not None:
            self.tcp_ports = m.get('TcpPorts')

        return self

class RunServiceScheduleResponseBodyCommandResults(DaraModel):
    def __init__(
        self,
        command_result: List[main_models.RunServiceScheduleResponseBodyCommandResultsCommandResult] = None,
    ):
        self.command_result = command_result

    def validate(self):
        if self.command_result:
            for v1 in self.command_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CommandResult'] = []
        if self.command_result is not None:
            for k1 in self.command_result:
                result['CommandResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.command_result = []
        if m.get('CommandResult') is not None:
            for k1 in m.get('CommandResult'):
                temp_model = main_models.RunServiceScheduleResponseBodyCommandResultsCommandResult()
                self.command_result.append(temp_model.from_map(k1))

        return self

class RunServiceScheduleResponseBodyCommandResultsCommandResult(DaraModel):
    def __init__(
        self,
        command: str = None,
        container_name: str = None,
        result_msg: str = None,
    ):
        # The command.
        self.command = command
        # The name of the container.
        self.container_name = container_name
        # The execution result of the command.
        self.result_msg = result_msg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['Command'] = self.command

        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        return self

