# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNetworkRulesRequest(DaraModel):
    def __init__(
        self,
        forward_protocol: str = None,
        frontend_port: int = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The forwarding protocol. Valid values:
        # - **tcp**
        # - **udp**
        self.forward_protocol = forward_protocol
        # The forward port.
        self.frontend_port = frontend_port
        # The ID of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        # > You can call [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) to query the IDs of all Anti-DDoS Pro or Anti-DDoS Premium instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number to return in a paging query. For example, set this parameter to **1** to return the first page of results.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of records displayed on each page.
        # 
        # This parameter is required.
        self.page_size = page_size

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')

        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

