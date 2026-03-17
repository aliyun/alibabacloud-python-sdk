# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySagRemoteAccessResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        remote_access_ip: str = None,
        request_id: str = None,
        serial_number: str = None,
        success: bool = None,
    ):
        # The returned status code.
        self.code = code
        # The message returned after calling the API.
        self.message = message
        # The remote access IP address.
        self.remote_access_ip = remote_access_ip
        # The ID of the request.
        self.request_id = request_id
        # The SN of the SAG device.
        self.serial_number = serial_number
        # Indicates whether the API call is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.remote_access_ip is not None:
            result['RemoteAccessIp'] = self.remote_access_ip

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RemoteAccessIp') is not None:
            self.remote_access_ip = m.get('RemoteAccessIp')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

