# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLayer4RulesRequest(DaraModel):
    def __init__(
        self,
        forward_protocol: str = None,
        frontend_port: int = None,
        instance_id: str = None,
        offset: int = None,
        page_size: str = None,
        source_ip: str = None,
    ):
        # The type of forwarding protocol. Values:
        # - **tcp**: Indicates TCP protocol.
        # - **udp**: Indicates UDP protocol.
        self.forward_protocol = forward_protocol
        # The forwarding port.
        self.frontend_port = frontend_port
        # The ID of the DDoS protection instance to be queried.
        # 
        # > You can call [DescribeInstances](https://help.aliyun.com/document_detail/91478.html) to query all DDoS protection instance IDs.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # In paginated queries, specifies which page of data to return. The minimum value is **1**, indicating the first page of data.
        # 
        # This parameter is required.
        self.offset = offset
        # In paginated queries, specifies the number of results per page. The maximum value is **50**, indicating that each page can contain up to 50 results.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The source IP address of the request. You do not need to fill this in; it is automatically obtained by the system.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol

        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')

        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

