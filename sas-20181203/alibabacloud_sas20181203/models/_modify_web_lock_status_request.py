# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyWebLockStatusRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
        status: str = None,
        uuid: str = None,
    ):
        # Specifies the language of the request and response messages. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The source IP address.
        self.source_ip = source_ip
        # Specifies the protection status of the server. Valid values:
        # - **on**: Enables protection.
        # - **off**: Initiates a shutdown of protection.    
        # 
        # > After you initiate a shutdown of web tamper-proofing for the current server, a tamper-proofing authorization quota is released.
        # 
        # This parameter is required.
        self.status = status
        # The UUID of the server for which you want to modify the protection status against brute-force attacks.
        # You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to obtain the UUID of the server.
        # 
        # This parameter is required.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

