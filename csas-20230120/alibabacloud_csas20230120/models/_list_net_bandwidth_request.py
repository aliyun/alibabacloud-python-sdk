# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListNetBandwidthRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        instance_ids: List[str] = None,
        net_type: str = None,
        page_size: int = None,
    ):
        # The current page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The list of instance IDs.
        self.instance_ids = instance_ids
        # The network type. If this parameter is left empty, both VPC and Connector instances are queried.
        self.net_type = net_type
        # The number of entries per page.
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

