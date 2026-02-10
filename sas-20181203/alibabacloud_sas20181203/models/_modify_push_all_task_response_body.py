# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ModifyPushAllTaskResponseBody(DaraModel):
    def __init__(
        self,
        push_task_rsp: main_models.ModifyPushAllTaskResponseBodyPushTaskRsp = None,
        request_id: str = None,
    ):
        # The results of security check tasks.
        self.push_task_rsp = push_task_rsp
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.push_task_rsp:
            self.push_task_rsp.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.push_task_rsp is not None:
            result['PushTaskRsp'] = self.push_task_rsp.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushTaskRsp') is not None:
            temp_model = main_models.ModifyPushAllTaskResponseBodyPushTaskRsp()
            self.push_task_rsp = temp_model.from_map(m.get('PushTaskRsp'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyPushAllTaskResponseBodyPushTaskRsp(DaraModel):
    def __init__(
        self,
        push_task_result_list: List[main_models.ModifyPushAllTaskResponseBodyPushTaskRspPushTaskResultList] = None,
    ):
        # The information about the server on which security check tasks failed.
        self.push_task_result_list = push_task_result_list

    def validate(self):
        if self.push_task_result_list:
            for v1 in self.push_task_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PushTaskResultList'] = []
        if self.push_task_result_list is not None:
            for k1 in self.push_task_result_list:
                result['PushTaskResultList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.push_task_result_list = []
        if m.get('PushTaskResultList') is not None:
            for k1 in m.get('PushTaskResultList'):
                temp_model = main_models.ModifyPushAllTaskResponseBodyPushTaskRspPushTaskResultList()
                self.push_task_result_list.append(temp_model.from_map(k1))

        return self

class ModifyPushAllTaskResponseBodyPushTaskRspPushTaskResultList(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        instance_id: str = None,
        instance_name: str = None,
        ip: str = None,
        message: str = None,
        online: bool = None,
        os_version: str = None,
        region: str = None,
        success: bool = None,
        uuid: str = None,
    ):
        # The ID of the server group to which the server belongs.
        self.group_id = group_id
        # The ID of the server.
        self.instance_id = instance_id
        # The name of the server.
        self.instance_name = instance_name
        # The IP address of the server.
        self.ip = ip
        # The message that describes the security check failure.
        self.message = message
        # Indicates whether the Security Center agent is online. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        # 
        # >  If the Security Center agent of the server is offline, Security Center does not protect the server.
        self.online = online
        # The operating system version of the server.
        self.os_version = os_version
        # The region in which the server resides.
        self.region = region
        # Indicates whether the security check task is successful. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.success = success
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.message is not None:
            result['Message'] = self.message

        if self.online is not None:
            result['Online'] = self.online

        if self.os_version is not None:
            result['OsVersion'] = self.os_version

        if self.region is not None:
            result['Region'] = self.region

        if self.success is not None:
            result['Success'] = self.success

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('OsVersion') is not None:
            self.os_version = m.get('OsVersion')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

