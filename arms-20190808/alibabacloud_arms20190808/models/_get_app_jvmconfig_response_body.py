# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetAppJVMConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        jvm_info_list: List[main_models.GetAppJVMConfigResponseBodyJvmInfoList] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. Valid values: 2XX: The request is successful. 3XX: A redirection message is returned. 4XX: The request is invalid. 5XX: A server error occurs.
        self.code = code
        # The list of JVM information.
        self.jvm_info_list = jvm_info_list
        # The error message returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.jvm_info_list:
            for v1 in self.jvm_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['JvmInfoList'] = []
        if self.jvm_info_list is not None:
            for k1 in self.jvm_info_list:
                result['JvmInfoList'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.jvm_info_list = []
        if m.get('JvmInfoList') is not None:
            for k1 in m.get('JvmInfoList'):
                temp_model = main_models.GetAppJVMConfigResponseBodyJvmInfoList()
                self.jvm_info_list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAppJVMConfigResponseBodyJvmInfoList(DaraModel):
    def __init__(
        self,
        agent_version: str = None,
        host_name: str = None,
        ip: str = None,
        pid: str = None,
        proc_id: str = None,
        vm_args: str = None,
    ):
        # The version of the agent.
        self.agent_version = agent_version
        # The hostname.
        self.host_name = host_name
        # The IP address.
        self.ip = ip
        # The application ID.
        self.pid = pid
        # The process ID.
        self.proc_id = proc_id
        # The VM parameters.
        self.vm_args = vm_args

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.proc_id is not None:
            result['ProcId'] = self.proc_id

        if self.vm_args is not None:
            result['VmArgs'] = self.vm_args

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('ProcId') is not None:
            self.proc_id = m.get('ProcId')

        if m.get('VmArgs') is not None:
            self.vm_args = m.get('VmArgs')

        return self

