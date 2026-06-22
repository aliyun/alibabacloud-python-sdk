# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAgentInstallStatusRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
        uuids: str = None,
    ):
        # The language type for the request and response messages. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The IP address of the access source.
        self.source_ip = source_ip
        # The UUIDs of the servers to query. Separate multiple UUIDs with commas (,).
        # > You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to obtain the UUIDs of servers.
        # 
        # This parameter is required.
        self.uuids = uuids

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

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

