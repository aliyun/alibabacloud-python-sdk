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
        # An array of up to 100 ConnectorIDs.
        self.connector_ids = connector_ids
        # The number of the page to return. Valid values: 1 to 10,000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The name of the connector. The name must be 1 to 128 characters long and can contain letters, Chinese characters, digits, periods (.), underscores (_), and hyphens (-).
        self.name = name
        # The number of entries per page. Valid values: 1 to 1,000.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The connection status of the connector. Valid values:
        # 
        # - **Online**
        # 
        # - **Offline**
        self.status = status
        # The state of the connector instance. Valid values:
        # 
        # - **Enabled**
        # 
        # - **Disabled**
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

