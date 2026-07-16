# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyImageRegistryRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        id: int = None,
        password: str = None,
        port: int = None,
        registry_host_ip: str = None,
        trans_per_hour: int = None,
        user_name: str = None,
    ):
        # The domain name.
        self.domain_name = domain_name
        # The image registry ID. Call the [ListImageRegistry](https://help.aliyun.com/document_detail/471986.html) operation to obtain this ID.
        self.id = id
        # The password.
        self.password = password
        # The port number.
        self.port = port
        # The registry IP address.
        self.registry_host_ip = registry_host_ip
        # The number of images to scan per hour.
        self.trans_per_hour = trans_per_hour
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.id is not None:
            result['Id'] = self.id

        if self.password is not None:
            result['Password'] = self.password

        if self.port is not None:
            result['Port'] = self.port

        if self.registry_host_ip is not None:
            result['RegistryHostIp'] = self.registry_host_ip

        if self.trans_per_hour is not None:
            result['TransPerHour'] = self.trans_per_hour

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegistryHostIp') is not None:
            self.registry_host_ip = m.get('RegistryHostIp')

        if m.get('TransPerHour') is not None:
            self.trans_per_hour = m.get('TransPerHour')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

