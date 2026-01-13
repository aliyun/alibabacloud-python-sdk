# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class ListExecutorsResponseBody(DaraModel):
    def __init__(
        self,
        executors: List[main_models.ListExecutorsResponseBodyExecutors] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # Executor list.
        self.executors = executors
        # The current page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.executors:
            for v1 in self.executors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Executors'] = []
        if self.executors is not None:
            for k1 in self.executors:
                result['Executors'].append(k1.to_map() if k1 else None)

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
        self.executors = []
        if m.get('Executors') is not None:
            for k1 in m.get('Executors'):
                temp_model = main_models.ListExecutorsResponseBodyExecutors()
                self.executors.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListExecutorsResponseBodyExecutors(DaraModel):
    def __init__(
        self,
        allocation_spec: str = None,
        app_name: str = None,
        array_index: int = None,
        block_duration: int = None,
        create_time: str = None,
        end_time: str = None,
        executor_id: str = None,
        expiration_time: str = None,
        external_ip_address: List[str] = None,
        host_name: List[str] = None,
        image: str = None,
        ip_address: List[str] = None,
        job_id: str = None,
        job_name: str = None,
        preemptible: bool = None,
        resource: main_models.ListExecutorsResponseBodyExecutorsResource = None,
        resource_type: str = None,
        start_time: str = None,
        status: str = None,
        status_reason: str = None,
        tags: List[main_models.ListExecutorsResponseBodyExecutorsTags] = None,
        task_name: str = None,
        task_sustainable: bool = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        self.allocation_spec = allocation_spec
        self.app_name = app_name
        # The executor number.
        self.array_index = array_index
        self.block_duration = block_duration
        # The time when the instance was created.
        self.create_time = create_time
        # The end time.
        self.end_time = end_time
        # The executor ID. The format is JobId-TaskName-ArrayIndex.
        self.executor_id = executor_id
        self.expiration_time = expiration_time
        # The list of public IP addresses of the nodes.
        self.external_ip_address = external_ip_address
        # The list of hostnames.
        self.host_name = host_name
        # Executor image.
        self.image = image
        # The list of internal IP addresses.
        self.ip_address = ip_address
        # The job ID.
        self.job_id = job_id
        # The job name.
        self.job_name = job_name
        self.preemptible = preemptible
        # The resource information.
        self.resource = resource
        # The type of the resource.
        self.resource_type = resource_type
        # The start time.
        self.start_time = start_time
        # The status of the executor. Valid values:
        # 
        # *   Pending
        # *   Initing
        # *   Succeed
        # *   Failed
        # *   Running
        # *   Unknown
        # *   Exception
        # *   Retrying
        # *   Expired
        # *   Deleted
        self.status = status
        # The description of the status reason.
        self.status_reason = status_reason
        # The list of executor tags.
        self.tags = tags
        # The name of the task.
        self.task_name = task_name
        # Indicate whether the job is a long-running job.
        self.task_sustainable = task_sustainable
        self.vpc_id = vpc_id
        # The ID of the vSwitch.
        self.vswitch_id = vswitch_id

    def validate(self):
        if self.resource:
            self.resource.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_spec is not None:
            result['AllocationSpec'] = self.allocation_spec

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.array_index is not None:
            result['ArrayIndex'] = self.array_index

        if self.block_duration is not None:
            result['BlockDuration'] = self.block_duration

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.external_ip_address is not None:
            result['ExternalIpAddress'] = self.external_ip_address

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.image is not None:
            result['Image'] = self.image

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.preemptible is not None:
            result['Preemptible'] = self.preemptible

        if self.resource is not None:
            result['Resource'] = self.resource.to_map()

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_sustainable is not None:
            result['TaskSustainable'] = self.task_sustainable

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationSpec') is not None:
            self.allocation_spec = m.get('AllocationSpec')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ArrayIndex') is not None:
            self.array_index = m.get('ArrayIndex')

        if m.get('BlockDuration') is not None:
            self.block_duration = m.get('BlockDuration')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('ExternalIpAddress') is not None:
            self.external_ip_address = m.get('ExternalIpAddress')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('Preemptible') is not None:
            self.preemptible = m.get('Preemptible')

        if m.get('Resource') is not None:
            temp_model = main_models.ListExecutorsResponseBodyExecutorsResource()
            self.resource = temp_model.from_map(m.get('Resource'))

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListExecutorsResponseBodyExecutorsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskSustainable') is not None:
            self.task_sustainable = m.get('TaskSustainable')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

class ListExecutorsResponseBodyExecutorsTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the executor tag.
        self.tag_key = tag_key
        # The value of the executor tag.
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

class ListExecutorsResponseBodyExecutorsResource(DaraModel):
    def __init__(
        self,
        cores: float = None,
        disks: List[main_models.ListExecutorsResponseBodyExecutorsResourceDisks] = None,
        instance_type: str = None,
        memory: float = None,
    ):
        # The number of running CPUs.
        self.cores = cores
        # The array of the disks.
        self.disks = disks
        self.instance_type = instance_type
        # The total amount of memory resources. Unit: GiB.
        self.memory = memory

    def validate(self):
        if self.disks:
            for v1 in self.disks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cores is not None:
            result['Cores'] = self.cores

        result['Disks'] = []
        if self.disks is not None:
            for k1 in self.disks:
                result['Disks'].append(k1.to_map() if k1 else None)

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.memory is not None:
            result['Memory'] = self.memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        self.disks = []
        if m.get('Disks') is not None:
            for k1 in m.get('Disks'):
                temp_model = main_models.ListExecutorsResponseBodyExecutorsResourceDisks()
                self.disks.append(temp_model.from_map(k1))

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        return self

class ListExecutorsResponseBodyExecutorsResourceDisks(DaraModel):
    def __init__(
        self,
        size: int = None,
        type: str = None,
    ):
        # The size of the disk.
        self.size = size
        # The category of the disk. The following disk categories are supported:
        # 
        # *   System: system disk.
        # *   Data: data disk.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.size is not None:
            result['Size'] = self.size

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

