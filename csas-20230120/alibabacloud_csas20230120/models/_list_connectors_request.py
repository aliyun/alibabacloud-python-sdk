# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListConnectorsRequest(DaraModel):
    def __init__(
        self,
        connector_ids: List[str] = None,
        current_page: int = None,
        name: str = None,
        page_size: int = None,
        status: str = None,
        switch_status: str = None,
    ):
        # Collection of ConnectorIDs. Up to 100 ConnectorIDs can be entered.
        self.connector_ids = connector_ids
        # The page number of the current page in a paginated query. Value: 1~10000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # Connector name. Length: 1~128 characters, supporting Chinese and uppercase/lowercase English letters, and can include numbers, periods (.), underscores (_), and hyphens (-).
        self.name = name
        # The number of items per page in a paginated query. Value: 1~1000.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Connector connection status. Values:
        # - **Online**: Online.
        # - **Offline**: Offline.
        self.status = status
        # Connector instance status. Values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.switch_status = switch_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector_ids is not None:
            result['ConnectorIds'] = self.connector_ids

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorIds') is not None:
            self.connector_ids = m.get('ConnectorIds')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')

        return self

