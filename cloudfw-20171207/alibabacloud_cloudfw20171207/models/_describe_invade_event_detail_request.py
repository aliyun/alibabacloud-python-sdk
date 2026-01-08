# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInvadeEventDetailRequest(DaraModel):
    def __init__(
        self,
        assets_instance_id: str = None,
        event_uuid: str = None,
        lang: str = None,
        public_ip: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.assets_instance_id = assets_instance_id
        # This parameter is required.
        self.event_uuid = event_uuid
        self.lang = lang
        self.public_ip = public_ip
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assets_instance_id is not None:
            result['AssetsInstanceId'] = self.assets_instance_id

        if self.event_uuid is not None:
            result['EventUuid'] = self.event_uuid

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetsInstanceId') is not None:
            self.assets_instance_id = m.get('AssetsInstanceId')

        if m.get('EventUuid') is not None:
            self.event_uuid = m.get('EventUuid')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

