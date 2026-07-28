# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVpnAttachmentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        create_time: int = None,
        message: str = None,
        name: str = None,
        request_id: str = None,
        success: bool = None,
        vpn_connection_id: str = None,
    ):
        # The status code returned by the current task. **200** indicates that the task is successful.
        self.code = code
        # The timestamp when the IPsec-VPN connection was created. Unit: milliseconds.
        # 
        # The timestamp follows the UNIX format and represents the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The message returned by the current task.
        self.message = message
        # The name of the IPsec-VPN connection.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # Indicates whether the current task is successfully executed.
        # 
        # - **true**: Successfully executed.
        # - **false**: Failed to execute.
        self.success = success
        # The IPsec-VPN connection ID.
        self.vpn_connection_id = vpn_connection_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.vpn_connection_id is not None:
            result['VpnConnectionId'] = self.vpn_connection_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('VpnConnectionId') is not None:
            self.vpn_connection_id = m.get('VpnConnectionId')

        return self

