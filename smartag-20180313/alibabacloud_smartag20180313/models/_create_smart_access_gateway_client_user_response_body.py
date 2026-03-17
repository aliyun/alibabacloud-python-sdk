# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSmartAccessGatewayClientUserResponseBody(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        client_ip: str = None,
        request_id: str = None,
        user_mail: str = None,
        user_name: str = None,
    ):
        # The maximum bandwidth value. Unit: Kbit/s.
        self.bandwidth = bandwidth
        # The IP address of the client app.
        self.client_ip = client_ip
        # The ID of the request.
        self.request_id = request_id
        # The email address of the client account.
        self.user_mail = user_mail
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_mail is not None:
            result['UserMail'] = self.user_mail

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserMail') is not None:
            self.user_mail = m.get('UserMail')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

