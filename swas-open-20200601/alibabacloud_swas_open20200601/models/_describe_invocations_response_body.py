# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class DescribeInvocationsResponseBody(DaraModel):
    def __init__(
        self,
        invocations: List[main_models.DescribeInvocationsResponseBodyInvocations] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The command execution records.
        self.invocations = invocations
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Settings for paging in a paged query.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of commands.
        self.total_count = total_count

    def validate(self):
        if self.invocations:
            for v1 in self.invocations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Invocations'] = []
        if self.invocations is not None:
            for k1 in self.invocations:
                result['Invocations'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invocations = []
        if m.get('Invocations') is not None:
            for k1 in m.get('Invocations'):
                temp_model = main_models.DescribeInvocationsResponseBodyInvocations()
                self.invocations.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInvocationsResponseBodyInvocations(DaraModel):
    def __init__(
        self,
        command_content: str = None,
        command_name: str = None,
        command_type: str = None,
        creation_time: str = None,
        invocation_status: str = None,
        invoke_id: str = None,
        invoke_status: str = None,
        parameters: Dict[str, Any] = None,
    ):
        # The command content, which is transmitted in Base64 encoding.
        self.command_content = command_content
        # The command name.
        self.command_name = command_name
        # The type of the command. Valid values:
        # 
        # - RunBatScript: a Bat command for Windows instances.
        # - RunPowerShellScript: a PowerShell command for Windows instances.
        # - RunShellScript: a shell command for Linux instances.
        self.command_type = command_type
        # The time when the command was created. The time is displayed in UTC (Z) in the YYYY-MM-DDThh:mm:ssZ format.
        self.creation_time = creation_time
        # The execution status of the command. Valid values:
        # 
        # - Pending: The system is verifying or sending the command.
        # - Invalid: The specified command type or parameter is invalid.
        # - Aborted: The command failed to be sent to the instance. The instance must be in the Running state, and the command must be delivered within one minute.
        # - Running: The command is being run on the instance.
        # - Success: The command execution is complete, and the exit code is 0.
        # - Failed: The command execution is complete, and the exit code is non-zero.
        # - Error: An exception occurred during command execution, and the command could not continue.
        # - Timeout: The command execution timed out.
        # - Cancelled: The command execution has been canceled, and the command was never started.
        # - Stopping: The running command is being stopped.
        # - Terminated: The command was terminated during execution.
        self.invocation_status = invocation_status
        # The command execution ID.
        self.invoke_id = invoke_id
        # The status of the command. Valid values:
        # 
        # - Running: The command is running.
        # - Finished: The command execution is complete.
        # - Failed: The command execution failed.
        # - Stopped: The command has been stopped.
        self.invoke_status = invoke_status
        # The custom parameters included in the command. If no parameters exist, the default value is {}.
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_content is not None:
            result['CommandContent'] = self.command_content

        if self.command_name is not None:
            result['CommandName'] = self.command_name

        if self.command_type is not None:
            result['CommandType'] = self.command_type

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.invoke_status is not None:
            result['InvokeStatus'] = self.invoke_status

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')

        if m.get('CommandName') is not None:
            self.command_name = m.get('CommandName')

        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('InvokeStatus') is not None:
            self.invoke_status = m.get('InvokeStatus')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        return self

