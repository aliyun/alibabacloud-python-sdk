# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePortRequest(DaraModel):
    def __init__(
        self,
        frontend_port: int = None,
        frontend_protocol: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The forwarding port to query. Valid values: **0** to **65535**.
        self.frontend_port = frontend_port
        # The type of the forwarding protocol to query. Valid values:
        # 
        # *   **tcp**
        # *   **udp**
        self.frontend_protocol = frontend_protocol
        # The ID of the instance to query.
        # 
        # > You can call the [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) operation to query the IDs of all instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number. For example, if you want to obtain results on the first page, set the value to **1**.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port

        if self.frontend_protocol is not None:
            result['FrontendProtocol'] = self.frontend_protocol

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')

        if m.get('FrontendProtocol') is not None:
            self.frontend_protocol = m.get('FrontendProtocol')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

