# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInvadeEventPayloadRequest(DaraModel):
    def __init__(
        self,
        assets_instance_id: str = None,
        end_time: str = None,
        event_uuid: str = None,
        lang: str = None,
        private_ip: str = None,
        public_ip: str = None,
        source_ip: str = None,
        start_time: str = None,
    ):
        # The instance ID of the asset where the intrusion event occurred.
        self.assets_instance_id = assets_instance_id
        # The end time of the time range during which the event occurred. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The UUID of the event.
        self.event_uuid = event_uuid
        # The language of the request and response. Valid values: - **zh**: Chinese. - **en**: English.
        self.lang = lang
        # The private IP address of the asset where the intrusion event occurred.
        self.private_ip = private_ip
        # The public IP address of the asset where the intrusion event occurred.
        self.public_ip = public_ip
        # The source IP address of the caller.
        self.source_ip = source_ip
        # The start time of the time range during which the event occurred. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assets_instance_id is not None:
            result['AssetsInstanceId'] = self.assets_instance_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_uuid is not None:
            result['EventUuid'] = self.event_uuid

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.private_ip is not None:
            result['PrivateIP'] = self.private_ip

        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetsInstanceId') is not None:
            self.assets_instance_id = m.get('AssetsInstanceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventUuid') is not None:
            self.event_uuid = m.get('EventUuid')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PrivateIP') is not None:
            self.private_ip = m.get('PrivateIP')

        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

