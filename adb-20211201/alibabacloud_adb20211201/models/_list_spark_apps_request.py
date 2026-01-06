# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSparkAppsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        filters: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_name: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.filters = filters
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10. Valid values:
        # 
        # - **10**
        # - **50**
        # - **100**
        self.page_size = page_size
        # The name of the job resource group.
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.filters is not None:
            result['Filters'] = self.filters

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Filters') is not None:
            self.filters = m.get('Filters')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        return self

