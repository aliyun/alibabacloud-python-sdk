# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeManagedInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.DescribeManagedInstancesResponseBodyInstances] = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried managed instances.
        self.instances = instances
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of queried managed instances.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

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
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.DescribeManagedInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

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

class DescribeManagedInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        activation_id: str = None,
        agent_version: str = None,
        connected: bool = None,
        hostname: str = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        invocation_count: int = None,
        last_invoked_time: str = None,
        machine_id: str = None,
        os_type: str = None,
        os_version: str = None,
        registration_time: str = None,
        resource_group_id: str = None,
        tags: List[main_models.DescribeManagedInstancesResponseBodyInstancesTags] = None,
    ):
        # The ID of the activation code.
        self.activation_id = activation_id
        # The version number of Cloud Assistant Agent.
        self.agent_version = agent_version
        # Indicates whether the managed instance is connected. Valid values:
        # 
        # *   true: The managed instance is connected. You can manage the instance by using Cloud Assistant.
        # *   false: The managed instance is not connected. The managed instance may be down or Cloud Assistant Agent may be incorrectly installed.
        self.connected = connected
        # The hostname of the managed instance.
        self.hostname = hostname
        # The ID of the managed instance.
        self.instance_id = instance_id
        # The name of the managed instance.
        self.instance_name = instance_name
        # The public IP address of the managed instance.
        self.internet_ip = internet_ip
        # The internal IP address of the managed instance.
        self.intranet_ip = intranet_ip
        # The number of times that Cloud Assistant tasks were executed on the managed instance.
        self.invocation_count = invocation_count
        # The time when the last Cloud Assistant task was executed.
        self.last_invoked_time = last_invoked_time
        # The machine code of the managed instance.
        self.machine_id = machine_id
        # The operating system type of the managed instance.
        self.os_type = os_type
        # The version information of the operating system.
        self.os_version = os_version
        # The time when the managed instance was registered.
        self.registration_time = registration_time
        # The ID of the resource group to which the managed instance belongs.
        self.resource_group_id = resource_group_id
        # The tags of the managed instance.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activation_id is not None:
            result['ActivationId'] = self.activation_id

        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

        if self.connected is not None:
            result['Connected'] = self.connected

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.invocation_count is not None:
            result['InvocationCount'] = self.invocation_count

        if self.last_invoked_time is not None:
            result['LastInvokedTime'] = self.last_invoked_time

        if self.machine_id is not None:
            result['MachineId'] = self.machine_id

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.os_version is not None:
            result['OsVersion'] = self.os_version

        if self.registration_time is not None:
            result['RegistrationTime'] = self.registration_time

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivationId') is not None:
            self.activation_id = m.get('ActivationId')

        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

        if m.get('Connected') is not None:
            self.connected = m.get('Connected')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('InvocationCount') is not None:
            self.invocation_count = m.get('InvocationCount')

        if m.get('LastInvokedTime') is not None:
            self.last_invoked_time = m.get('LastInvokedTime')

        if m.get('MachineId') is not None:
            self.machine_id = m.get('MachineId')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('OsVersion') is not None:
            self.os_version = m.get('OsVersion')

        if m.get('RegistrationTime') is not None:
            self.registration_time = m.get('RegistrationTime')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeManagedInstancesResponseBodyInstancesTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeManagedInstancesResponseBodyInstancesTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of tag N of the managed instance. Valid values of N: 1 to 20. The tag key cannot be an empty string.
        # 
        # If a single tag is specified to query resources, up to 1,000 resources that have this tag added are returned. If multiple tags are specified to query resources, up to 1,000 resources that have all these tags added are returned. To query more than 1,000 resources that have the specified tags, call the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation.
        # 
        # The tag key can be up to 64 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        self.tag_key = tag_key
        # The value of tag N of the managed instance. Valid values of N: 1 to 20. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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

