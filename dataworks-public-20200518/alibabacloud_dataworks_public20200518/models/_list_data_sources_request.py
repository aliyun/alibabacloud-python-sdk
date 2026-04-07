# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataSourcesRequest(DaraModel):
    def __init__(
        self,
        data_source_type: str = None,
        env_type: int = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        status: str = None,
        sub_type: str = None,
    ):
        # The type of the data source. Valid values:
        # 
        # *   odps
        # *   mysql
        # *   rds
        # *   oss
        # *   sqlserver
        # *   polardb
        # *   oracle
        # *   mongodb
        # *   emr
        # *   postgresql
        # *   analyticdb_for_mysql
        # *   hybriddb_for_postgresql
        # *   holo
        self.data_source_type = data_source_type
        # The environment in which the data source is used. Valid values: 0 and 1. The value 0 indicates development environment. The value 1 indicates production environment.
        self.env_type = env_type
        # The name of the data source that you want to query.
        self.name = name
        # The page number. Pages start from page 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The ID of the DataWorks workspace to which the data sources belong. You can call the [ListProjects](https://help.aliyun.com/document_detail/2780068.html) operation to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The status of the data source. Valid values:
        # 
        # *   ENABLED
        # *   DISABLED
        self.status = status
        # The subtype of the data source. This parameter takes effect only when the DataSourceType parameter is set to rds.
        # 
        # If the value of the DataSourceType parameter is rds, the value of this parameter can be mysql, sqlserver, or postgresql.
        self.sub_type = sub_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        return self

