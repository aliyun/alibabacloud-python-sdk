# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAppsRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        order: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        status: str = None,
    ):
        # The application ID. You can create and query application IDs in the console. Only a single ID is supported. If this parameter is left empty, all application IDs are queried.
        self.app_id = app_id
        # The application version.
        self.app_version = app_version
        # The sort order. Valid values:
        # 
        # - **asc**: Ascending.
        #  
        # - **desc**: Descending. Default value.
        self.order = order
        self.owner_id = owner_id
        # The page number. Default value: **1**.
        self.page_num = page_num
        # The number of entries per page. Default value: **10**.
        self.page_size = page_size
        # The application status. If this parameter is left empty, all statuses are queried. Valid values:
        # - **1**: Available.
        # 
        # - **2**: Disabled.
        # 
        # - **3**: Disabled due to overdue payments.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.order is not None:
            result['Order'] = self.order

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

