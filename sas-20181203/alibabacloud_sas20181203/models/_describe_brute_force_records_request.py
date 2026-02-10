# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBruteForceRecordsRequest(DaraModel):
    def __init__(
        self,
        block_ip: str = None,
        current_page: int = None,
        instance_id: str = None,
        page_size: int = None,
        remark: str = None,
        resource_owner_id: int = None,
        status: int = None,
    ):
        # The IP address that is blocked.
        self.block_ip = block_ip
        # The number of the page to return.
        self.current_page = current_page
        # The ID of the server.
        self.instance_id = instance_id
        # The number of entries to return on each page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page. We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The name or IP address of the server to query.
        self.remark = remark
        self.resource_owner_id = resource_owner_id
        # The status of the defense rule. Valid values:
        # 
        # *   **0**: invalid
        # *   **1**: enabled
        # *   **2**: failed
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_ip is not None:
            result['BlockIp'] = self.block_ip

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockIp') is not None:
            self.block_ip = m.get('BlockIp')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

