# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeSendFileResultsResponseBody(DaraModel):
    def __init__(
        self,
        invocations: main_models.DescribeSendFileResultsResponseBodyInvocations = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The file sending records.
        self.invocations = invocations
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of file sending tasks queried.
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

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
        if m.get('Invocations') is not None:
            temp_model = main_models.DescribeSendFileResultsResponseBodyInvocations()
            self.invocations = temp_model.from_map(m.get('Invocations'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

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
        invoke_id: str = None,
        invoke_instances: main_models.DescribeSendFileResultsResponseBodyInvocationsInvocationInvokeInstances = None,
        name: str = None,
        overwrite: str = None,
        tags: main_models.DescribeSendFileResultsResponseBodyInvocationsInvocationTags = None,
        target_dir: str = None,
        vm_count: int = None,
    ):
        # The content of the file.
        self.content = content
        # The type of the file content. Valid values:
        # 
        # *   PlainText: The file content is not encoded.
        # *   Base64: The file content is encoded in Base64.
        self.content_type = content_type
        # The time when the file sending task was created.
        self.creation_time = creation_time
        # The description of the file.
        self.description = description
        # The group of the file.
        self.file_group = file_group
        # The permissions on the file.
        self.file_mode = file_mode
        # The owner of the file.
        self.file_owner = file_owner
        # The overall sending status of the file. The overall sending status of the file varies based on the sending status of the file on all destination instances. Valid values:
        # 
        # *   Pending: The file is being verified or sent. If the sending state of the file on at least one instance is Pending, the overall sending state of the file is Pending.
        # 
        # *   Running: The file is being sent to the instances. If the sending state of the file on at least one instance is Running, the overall sending state of the file is Running.
        # 
        # *   Success: If the sending state of the file on all instances is Success, the overall sending state of the file is Success.
        # 
        # *   If the sending state of the file on all instances is Failed, the overall sending state of the file is Failed. If the sending state of the file on one or more instances is one of the following values, the overall sending state of the file is Failed:
        # 
        #     *   Invalid: The file is invalid.
        #     *   Aborted: The file failed to be sent to the instances.
        #     *   Failed: The file failed to be created on the instances.
        #     *   Timeout: The file sending task timed out.
        #     *   Error: An error occurred and interrupted the file sending task.
        # 
        # *   PartialFailed: The file sending task was completed on some instances but failed on other instances. If the sending state of the file is Success on some instances and is Failed on other instances, the overall sending state of the file is PartialFailed.
        self.invocation_status = invocation_status
        # The ID of the file sending task.
        self.invoke_id = invoke_id
        # The destination instances.
        self.invoke_instances = invoke_instances
        # The name of the file.
        self.name = name
        # Indicates whether a file in the destination directory is overwritten if the file has the same name as the sent file.
        self.overwrite = overwrite
        # The tags of the file sending task.
        self.tags = tags
        # The destination directory.
        self.target_dir = target_dir
        # The number of the destination instances.
        self.vm_count = vm_count

    def validate(self):
        if self.invoke_instances:
            self.invoke_instances.validate()
        if self.tags:
            self.tags.validate()

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

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.invoke_instances is not None:
            result['InvokeInstances'] = self.invoke_instances.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.target_dir is not None:
            result['TargetDir'] = self.target_dir

        if self.vm_count is not None:
            result['VmCount'] = self.vm_count

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

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('InvokeInstances') is not None:
            temp_model = main_models.DescribeSendFileResultsResponseBodyInvocationsInvocationInvokeInstances()
            self.invoke_instances = temp_model.from_map(m.get('InvokeInstances'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeSendFileResultsResponseBodyInvocationsInvocationTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TargetDir') is not None:
            self.target_dir = m.get('TargetDir')

        if m.get('VmCount') is not None:
            self.vm_count = m.get('VmCount')

        return self

class DescribeSendFileResultsResponseBodyInvocationsInvocationTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeSendFileResultsResponseBodyInvocationsInvocationTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeSendFileResultsResponseBodyInvocationsInvocationTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeSendFileResultsResponseBodyInvocationsInvocationTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the file sending task.
        self.tag_key = tag_key
        # The tag value of the file sending task.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeSendFileResultsResponseBodyInvocationsInvocationInvokeInstances(DaraModel):
    def __init__(
        self,
        invoke_instance: List[main_models.DescribeSendFileResultsResponseBodyInvocationsInvocationInvokeInstancesInvokeInstance] = None,
    ):
        self.invoke_instance = invoke_instance

    def validate(self):
        if self.invoke_instance:
            for v1 in self.invoke_instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InvokeInstance'] = []
        if self.invoke_instance is not None:
            for k1 in self.invoke_instance:
                result['InvokeInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invoke_instance = []
        if m.get('InvokeInstance') is not None:
            for k1 in m.get('InvokeInstance'):
                temp_model = main_models.DescribeSendFileResultsResponseBodyInvocationsInvocationInvokeInstancesInvokeInstance()
                self.invoke_instance.append(temp_model.from_map(k1))

        return self

class DescribeSendFileResultsResponseBodyInvocationsInvocationInvokeInstancesInvokeInstance(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        error_code: str = None,
        error_info: str = None,
        finish_time: str = None,
        instance_id: str = None,
        invocation_status: str = None,
        start_time: str = None,
        update_time: str = None,
    ):
        # The creation time of the file sending task.
        self.creation_time = creation_time
        # The error code returned when the file failed to be sent to the instance. Valid values:
        # 
        # *   Null: The file is sent to the instance.
        # *   InstanceNotExists: The instance does not exist or has been released.
        # *   InstanceReleased: The instance is released while the file is being sent.
        # *   InstanceNotRunning: The instance is not running when the file sending task is being created.
        # *   AccountNotExists: The specified account does not exist.
        # *   ClientNotRunning: Cloud Assistant Agent is not running.
        # *   ClientNotResponse: Cloud Assistant Agent does not respond.
        # *   ClientIsUpgrading: Cloud Assistant Agent is being upgraded.
        # *   ClientNeedUpgrade: Cloud Assistant Agent needs to be upgraded.
        # *   DeliveryTimeout: The file sending task timed out.
        # *   FileCreateFail: The file failed to be created.
        # *   FileAlreadyExists: A file with the same name exists in the specified directory.
        # *   FileContentInvalid: The file content is invalid.
        # *   FileNameInvalid: The file name is invalid.
        # *   FilePathInvalid: The specified directory is invalid.
        # *   FileAuthorityInvalid: The specified permissions on the file are invalid.
        # *   UserGroupNotExists: The specified user group does not exist.
        self.error_code = error_code
        # The error message returned when the file failed to be sent or the file sending task failed to be executed. Valid values:
        # 
        # *   Null: The file is sent to the instance.
        # *   the specified instance does not exists
        # *   the specified instance has been released
        # *   the instance is not running when create task
        # *   the specified account does not exists
        # *   the aliyun service is not running on the instance
        # *   the aliyun service in the instance does not response
        # *   the aliyun service in the instance is upgrading now
        # *   the aliyun service in the instance need upgrade
        # *   the command delivery has been timeout
        # *   the file creation is failed due to unknown error
        # *   the authority of file is invalid
        # *   File content is empty
        # *   the content of file is invalid
        # *   File already exists
        # *   File name is invalid
        # *   File path is invalid
        # *   Owner not exists
        # *   Group not exists
        # *   Mode is invalid
        self.error_info = error_info
        # The time when the file sending task was completed.
        self.finish_time = finish_time
        # The ID of the instance.
        self.instance_id = instance_id
        # The status of the file sending task. Valid values:
        # 
        # *   Pending: The file is being verified or sent.
        # *   Invalid: The file is invalid.
        # *   Running: The file is being sent to the instance.
        # *   Aborted: The file failed to be sent to the instance.
        # *   Success: The file is sent.
        # *   Failed: The file failed to be created on the instance.
        # *   Error: An error occurred and interrupted the file sending task.
        # *   Timeout: The file sending task timed out.
        self.invocation_status = invocation_status
        # The time when the file sending task started to be executed on the instance.
        self.start_time = start_time
        # The time when the task status was last updated.
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status

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

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

