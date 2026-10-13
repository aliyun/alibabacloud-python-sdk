# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class DescribeSendFileResultsResponseBody(DaraModel):
    def __init__(
        self,
        invocations: main_models.DescribeSendFileResultsResponseBodyInvocations = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The file sending records.
        self.invocations = invocations
        # Id of the request
        self.request_id = request_id
        # The total number of commands.
        self.total_count = total_count

    def validate(self):
        if self.invocations:
            self.invocations.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.invocations is not None:
            result['Invocations'] = self.invocations.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Invocations') is not None:
            temp_model = main_models.DescribeSendFileResultsResponseBodyInvocations()
            self.invocations = temp_model.from_map(m.get('Invocations'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSendFileResultsResponseBodyInvocations(DaraModel):
    def __init__(
        self,
        invocation: List[main_models.DescribeSendFileResultsResponseBodyInvocationsInvocation] = None,
    ):
        # The command execution ID.
        self.invocation = invocation

    def validate(self):
        if self.invocation:
            for v1 in self.invocation:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Invocation'] = []
        if self.invocation is not None:
            for k1 in self.invocation:
                result['Invocation'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invocation = []
        if m.get('Invocation') is not None:
            for k1 in m.get('Invocation'):
                temp_model = main_models.DescribeSendFileResultsResponseBodyInvocationsInvocation()
                self.invocation.append(temp_model.from_map(k1))

        return self

class DescribeSendFileResultsResponseBodyInvocationsInvocation(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        creation_time: str = None,
        description: str = None,
        file_group: str = None,
        file_mode: str = None,
        file_owner: str = None,
        invocation_status: str = None,
        invoke_nodes: main_models.DescribeSendFileResultsResponseBodyInvocationsInvocationInvokeNodes = None,
        name: str = None,
        node_count: int = None,
        overwrite: bool = None,
        target_dir: str = None,
    ):
        # The output information after command execution.
        # 
        # If ContentEncoding is set to PlainText, the original output information is returned.
        # If ContentEncoding is set to Base64, the Base64-encoded output information is returned.
        self.content = content
        # The file content type. Valid values:
        # 
        # - PlainText: Plain text.
        # - Base64: Base64 encoding.
        # 
        # Default value: PlainText.
        self.content_type = content_type
        # The time when the sending task was created. The time is in ISO 8601 format and includes the time zone offset.
        self.creation_time = creation_time
        # The command description.
        self.description = description
        # The user group of the file.
        self.file_group = file_group
        # The permissions of the file.
        self.file_mode = file_mode
        # The user of the file.
        self.file_owner = file_owner
        # The overall sending status of the file. The overall status depends on the combined execution status of all instances in this sending operation. Valid values:
        # 
        # - Pending: The system is validating or sending the file. If the file sending status of at least one instance is Pending, the overall status is Pending.
        # - Running: The file is being sent on the instance. If the file sending status of at least one instance is Running, the overall status is Running.
        # - Success: If the file sending status on all instances is Success, the overall status is Success.
        # - Failed: If the file sending status on all instances is Failed, the overall status is Failed. The return value is Failed when one or more of the following statuses occur on an instance:
        #     - The specified file parameters are invalid and validation failed (Invalid).
        #     - Failed to send the file to the instance (Aborted).
        #     - Failed to create the file on the instance (Failed).
        #     - File sending timed out (Timeout).
        #     - An exception occurred during file sending and the operation cannot continue (Error).
        # - PartialFailed: File sending succeeded on some instances but failed on others. If the file sending status on all instances is either Success or Failed, the overall status is PartialFailed.
        self.invocation_status = invocation_status
        # The file sending records.
        self.invoke_nodes = invoke_nodes
        # The file sending name.
        self.name = name
        # The number of nodes.
        self.node_count = node_count
        # Specifies whether to overwrite the file if a file with the same name already exists in the target directory. Valid values:
        # 
        # - true: Overwrite the file.
        # - false: Do not overwrite the file.
        # 
        # Default value: false.
        self.overwrite = overwrite
        # The target path.
        self.target_dir = target_dir

    def validate(self):
        if self.invoke_nodes:
            self.invoke_nodes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.file_group is not None:
            result['FileGroup'] = self.file_group

        if self.file_mode is not None:
            result['FileMode'] = self.file_mode

        if self.file_owner is not None:
            result['FileOwner'] = self.file_owner

        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status

        if self.invoke_nodes is not None:
            result['InvokeNodes'] = self.invoke_nodes.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite

        if self.target_dir is not None:
            result['TargetDir'] = self.target_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileGroup') is not None:
            self.file_group = m.get('FileGroup')

        if m.get('FileMode') is not None:
            self.file_mode = m.get('FileMode')

        if m.get('FileOwner') is not None:
            self.file_owner = m.get('FileOwner')

        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')

        if m.get('InvokeNodes') is not None:
            temp_model = main_models.DescribeSendFileResultsResponseBodyInvocationsInvocationInvokeNodes()
            self.invoke_nodes = temp_model.from_map(m.get('InvokeNodes'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')

        if m.get('TargetDir') is not None:
            self.target_dir = m.get('TargetDir')

        return self

class DescribeSendFileResultsResponseBodyInvocationsInvocationInvokeNodes(DaraModel):
    def __init__(
        self,
        invoke_node: List[main_models.DescribeSendFileResultsResponseBodyInvocationsInvocationInvokeNodesInvokeNode] = None,
    ):
        # The file sending record of a node.
        self.invoke_node = invoke_node

    def validate(self):
        if self.invoke_node:
            for v1 in self.invoke_node:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InvokeNode'] = []
        if self.invoke_node is not None:
            for k1 in self.invoke_node:
                result['InvokeNode'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invoke_node = []
        if m.get('InvokeNode') is not None:
            for k1 in m.get('InvokeNode'):
                temp_model = main_models.DescribeSendFileResultsResponseBodyInvocationsInvocationInvokeNodesInvokeNode()
                self.invoke_node.append(temp_model.from_map(k1))

        return self

class DescribeSendFileResultsResponseBodyInvocationsInvocationInvokeNodesInvokeNode(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        error_code: str = None,
        error_info: str = None,
        finish_time: str = None,
        invocation_status: str = None,
        node_id: str = None,
        start_time: str = None,
        update_time: str = None,
    ):
        # The time when the file sending task was created. The time is in ISO 8601 format. Z in the example indicates UTC.
        self.creation_time = creation_time
        # The error code for the file sending failure. Valid values:
        # 
        # - Empty: File sending was normal.
        # - NodeNotExists: The specified instance does not exist or has been released.
        # - NodeReleased: The instance was released during file sending.
        # - NodeNotRunning: The instance was not running when the file sending task was created.
        # - AccountNotExists: The specified account does not exist.
        # - ClientNotRunning: Cloud Assistant Agent is not running.
        # - ClientNotResponse: Cloud Assistant Agent is not responding.
        # - ClientIsUpgrading: Cloud Assistant Agent is being upgraded.
        # - ClientNeedUpgrade: Cloud Assistant Agent needs to be upgraded.
        # - DeliveryTimeout: File sending timed out.
        # - FileCreateFail: File creation failed.
        # - FileAlreadyExists: A file with the same name already exists in the same path.
        # - FileContentInvalid: The file content is invalid.
        # - FileNameInvalid: The file name is invalid.
        # - FilePathInvalid: The file path is invalid.
        # - FileAuthorityInvalid: The file permissions are invalid.
        # - UserGroupNotExists: The user group specified during file sending does not exist.
        self.error_code = error_code
        # The details of the reason why the command failed to be sent or executed. Valid values:
        # - Empty: The command was executed normally.
        # - the specified instance does not exists: The specified instance does not exist or has been released.
        # - the node has released when create task: The instance was released during command execution.
        # - the node is not running when create task: The instance was not running when the command was executed.
        # - the command is not applicable: The command is not applicable to the specified instance.
        # - the specified account does not exists: The specified account does not exist.
        # - the specified directory does not exists: The specified directory does not exist.
        # - the cron job expression is invalid: The specified execution time expression is invalid.
        # - the aliyun service is not running on the instance: Cloud Assistant Agent is not running.
        # - the aliyun service in the instance does not response: Cloud Assistant Agent is not responding.
        # - the aliyun service in the node is upgrading now: Cloud Assistant Agent is being upgraded.
        # - the aliyun service in the node need upgrade: Cloud Assistant Agent needs to be upgraded.
        # - the command delivery has been timeout: Sending the command timed out.
        # - the command execution has been timeout: Command execution timed out.
        # - the command execution got an exception: An exception occurred during command execution.
        # - the command execution has been interrupted: Command execution was interrupted.
        # - the command execution exit code is not zero: Command execution ended with a non-zero exit code.
        # - the specified instance has been released: The instance was released during file sending.
        self.error_info = error_info
        # The end time, in the format: "2020-05-22T17:04:18".
        self.finish_time = finish_time
        # The file sending status on a single instance. Valid values:
        # - Pending: The system is validating or sending the file.
        # - Invalid: The specified file parameters are invalid and validation failed.
        # - Running: The file is being sent on the instance.
        # - Aborted: Failed to send the file to the instance.
        # - Success: File sending completed.
        # - Failed: Failed to create the file on the instance.
        # - Error: An exception occurred during file sending and the operation cannot continue.
        # - Timeout: File sending timed out.
        self.invocation_status = invocation_status
        # The node ID.
        self.node_id = node_id
        # The start time. The time is in ISO 8601 format. Z in the example indicates UTC.
        self.start_time = start_time
        # The update time. The time is in ISO 8601 format. Z in the example indicates UTC.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

