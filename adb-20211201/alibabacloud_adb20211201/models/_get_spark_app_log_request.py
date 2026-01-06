# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSparkAppLogRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        dbcluster_id: str = None,
        log_length: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The Spark application ID.
        # 
        # > You can call the [ListSparkApps](https://help.aliyun.com/document_detail/612475.html) operation to query the Spark application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition cluster.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/454250.html) operation to query the IDs of all AnalyticDB for MySQL clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The number of log entries to return. Valid values: 1 to 500. Default value: 300.
        self.log_length = log_length
        # The page number.
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
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.log_length is not None:
            result['LogLength'] = self.log_length

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

        if m.get('LogLength') is not None:
            self.log_length = m.get('LogLength')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

