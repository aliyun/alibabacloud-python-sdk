# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSparkAppAttemptsRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        dbcluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the Spark application.
        # 
        # > You can call the [ListSparkApps](https://help.aliyun.com/document_detail/455888.html) operation to query all application IDs.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition cluster.
        self.dbcluster_id = dbcluster_id
        # The page number. The value must be an integer that is greater than 0. Default value: **1**.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **10** (default)
        # *   **50**
        # *   **100**
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

