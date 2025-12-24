# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DeregisterManagedInstanceResponseBody(DaraModel):
    def __init__(
        self,
        instance: main_models.DeregisterManagedInstanceResponseBodyInstance = None,
        request_id: str = None,
    ):
        # Details of the managed instances.
        self.instance = instance
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instance') is not None:
            temp_model = main_models.DeregisterManagedInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m.get('Instance'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DeregisterManagedInstanceResponseBodyInstance(DaraModel):
    def __init__(
        self,
        activation_id: str = None,
        agent_version: str = None,
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
    ):
        # The activation code ID.
        self.activation_id = activation_id
        # The version number of Cloud Assistant Agent.
        self.agent_version = agent_version
        # The hostname of the managed instance.
        self.hostname = hostname
        # The managed instance ID.
        self.instance_id = instance_id
        # The name of the managed instance.
        self.instance_name = instance_name
        # The public IP address of the managed instance.
        self.internet_ip = internet_ip
        # The internal IP address of the managed instance.
        self.intranet_ip = intranet_ip
        # The number of times that Cloud Assistant tasks were executed on the managed instance.
        self.invocation_count = invocation_count
        # The time when the Cloud Assistant task was last executed.
        self.last_invoked_time = last_invoked_time
        # The machine code of the managed instance.
        self.machine_id = machine_id
        # The operating system type of the managed instance.
        self.os_type = os_type
        # The version information about the operating system.
        self.os_version = os_version
        # The time when the managed instance was registered.
        self.registration_time = registration_time
        # The ID of the resource group to which the managed instance belongs.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activation_id is not None:
            result['ActivationId'] = self.activation_id

        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivationId') is not None:
            self.activation_id = m.get('ActivationId')

        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

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

        return self

