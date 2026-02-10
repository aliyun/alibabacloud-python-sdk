# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddUninstallClientsByUuidsRequest(DaraModel):
    def __init__(
        self,
        call_method: str = None,
        feedback: str = None,
        region: str = None,
        source_ip: str = None,
        uuids: str = None,
    ):
        # The method name. Default value: init.
        self.call_method = call_method
        # The feedback.
        self.feedback = feedback
        # The region in which the server resides.
        self.region = region
        # The source IP address of the request. You do not need to specify this parameter. It is automatically obtained by the system.
        self.source_ip = source_ip
        # The UUID of the server that you want to unbind. Separate multiple UUIDs with commas (,).
        # 
        # >  You can call the [DescribeCloudCenterInstances](https://help.aliyun.com/document_detail/141932.html) operation to query the UUIDs of servers.
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
        if self.call_method is not None:
            result['CallMethod'] = self.call_method

        if self.feedback is not None:
            result['Feedback'] = self.feedback

        if self.region is not None:
            result['Region'] = self.region

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallMethod') is not None:
            self.call_method = m.get('CallMethod')

        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

