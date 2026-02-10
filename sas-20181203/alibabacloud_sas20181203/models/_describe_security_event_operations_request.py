# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSecurityEventOperationsRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        resource_owner_id: int = None,
        security_event_id: int = None,
        source_ip: str = None,
    ):
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        self.resource_owner_id = resource_owner_id
        # The ID of the alert event that you want to handle.
        # 
        # This parameter is required.
        self.security_event_id = security_event_id
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

