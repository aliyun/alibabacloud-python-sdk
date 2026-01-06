# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class AddHDMInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.AddHDMInstanceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The detailed information, including the error codes and the number of entries that are returned.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The reserved parameter.
        self.synchro = synchro

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.AddHDMInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self



class AddHDMInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        caller_uid: str = None,
        code: int = None,
        error: str = None,
        instance_id: str = None,
        ip: str = None,
        owner_id: str = None,
        port: int = None,
        role: str = None,
        tenant_id: str = None,
        token: str = None,
        uuid: str = None,
        vpc_id: str = None,
    ):
        # The user ID of the caller.
        self.caller_uid = caller_uid
        # The HTTP status code returned.
        self.code = code
        # The error message returned if the request failed.
        self.error = error
        # The instance ID.
        self.instance_id = instance_id
        # The endpoint of the instance.
        self.ip = ip
        # The ID of the instance owner.
        self.owner_id = owner_id
        # The port number of the instance that you want to access.
        self.port = port
        # The role of the current API caller.
        self.role = role
        # The tenant ID.
        self.tenant_id = tenant_id
        # The client token that is used to ensure the idempotence of the request.
        self.token = token
        # The unique identifier of the instance.
        self.uuid = uuid
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid

        if self.code is not None:
            result['Code'] = self.code

        if self.error is not None:
            result['Error'] = self.error

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.port is not None:
            result['Port'] = self.port

        if self.role is not None:
            result['Role'] = self.role

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.token is not None:
            result['Token'] = self.token

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

