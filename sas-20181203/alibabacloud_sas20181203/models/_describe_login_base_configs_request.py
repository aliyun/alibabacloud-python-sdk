# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLoginBaseConfigsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        target: str = None,
        type: str = None,
    ):
        # The page number of the page to return. Default value: **1**.
        self.current_page = current_page
        # Settings for paged query. The number of logon configuration entries to display on each page when paging is used. Default value: **5**.
        self.page_size = page_size
        # The selection mode for the assets on which the policy takes effect. This parameter is in JSON format and contains the following fields:
        # 
        # - **Target**: The UUID of the server to add or delete, or the ID of the server group.
        # 
        # > If the targetType parameter is set to uuid, this parameter specifies the UUID of the server. If the targetType parameter is set to groupId, this parameter specifies the ID of the server group. If the targetType parameter is set to global, set this parameter to a hyphen (-).
        # 
        # - **targetType**: The selection mode for the assets on which the policy takes effect. Valid values:
        #     - **uuid**: queries by individual server.
        #     - **groupId**: queries by server group.
        #     - **global**: queries all servers.
        self.target = target
        # The type of logon configuration to query. Valid values:
        # - **login_common_location**: common logon location.
        # - **login_common_ip**: common logon IP address.
        # - **login_common_time**: common logon time.
        # - **login_common_account**: common logon account.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.target is not None:
            result['Target'] = self.target

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

