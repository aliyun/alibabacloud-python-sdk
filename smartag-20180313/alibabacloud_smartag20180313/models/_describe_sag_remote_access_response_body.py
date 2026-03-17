# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSagRemoteAccessResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        remote_accesses: main_models.DescribeSagRemoteAccessResponseBodyRemoteAccesses = None,
        request_id: str = None,
        smart_agid: str = None,
        success: bool = None,
    ):
        # The error code. The 200 error code indicates that the query task is successful.
        self.code = code
        # The error message. The Successful error message indicates that the query task is successful.
        self.message = message
        self.remote_accesses = remote_accesses
        # The ID of the request.
        self.request_id = request_id
        # The ID of the SAG instance.
        self.smart_agid = smart_agid
        # Indicates whether the query task is successful. Valid values:
        # 
        # *   **true**: The query task is successful.
        # *   **false**: The query task failed.
        self.success = success

    def validate(self):
        if self.remote_accesses:
            self.remote_accesses.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.remote_accesses is not None:
            result['RemoteAccesses'] = self.remote_accesses.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RemoteAccesses') is not None:
            temp_model = main_models.DescribeSagRemoteAccessResponseBodyRemoteAccesses()
            self.remote_accesses = temp_model.from_map(m.get('RemoteAccesses'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSagRemoteAccessResponseBodyRemoteAccesses(DaraModel):
    def __init__(
        self,
        remote_access: List[main_models.DescribeSagRemoteAccessResponseBodyRemoteAccessesRemoteAccess] = None,
    ):
        self.remote_access = remote_access

    def validate(self):
        if self.remote_access:
            for v1 in self.remote_access:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RemoteAccess'] = []
        if self.remote_access is not None:
            for k1 in self.remote_access:
                result['RemoteAccess'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.remote_access = []
        if m.get('RemoteAccess') is not None:
            for k1 in m.get('RemoteAccess'):
                temp_model = main_models.DescribeSagRemoteAccessResponseBodyRemoteAccessesRemoteAccess()
                self.remote_access.append(temp_model.from_map(k1))

        return self

class DescribeSagRemoteAccessResponseBodyRemoteAccessesRemoteAccess(DaraModel):
    def __init__(
        self,
        remote_access_ip: str = None,
        serial_number: str = None,
    ):
        self.remote_access_ip = remote_access_ip
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remote_access_ip is not None:
            result['RemoteAccessIp'] = self.remote_access_ip

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemoteAccessIp') is not None:
            self.remote_access_ip = m.get('RemoteAccessIp')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        return self

