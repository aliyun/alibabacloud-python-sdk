# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetMetaTablePartitionRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_source_type: str = None,
        database_name: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_criterion: main_models.GetMetaTablePartitionRequestSortCriterion = None,
        table_guid: str = None,
        table_name: str = None,
    ):
        # The ID of the EMR cluster. This parameter is required only if you set the DataSourceType parameter to emr.
        # 
        # You can log on to the [EMR console](https://emr.console.aliyun.com/?spm=a2c4g.11186623.0.0.965cc5c2GeiHet#/cn-hangzhou) to obtain the ID.
        self.cluster_id = cluster_id
        # The type of the data source. Valid values: odps and emr.
        self.data_source_type = data_source_type
        # The name of the database. This parameter is required only if you set the DataSourceType parameter to emr.
        # 
        # You can call the [ListMetaDB](https://help.aliyun.com/document_detail/2780105.html) operation to query the name of the metadatabase.
        self.database_name = database_name
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The logic for sorting partitions in the metatable.
        self.sort_criterion = sort_criterion
        # The unique identifier of the metatable.
        self.table_guid = table_guid
        # The name of the metatable in the EMR cluster. This parameter is required only if you set the DataSourceType parameter to emr.
        # 
        # You can call the [GetMetaDBTableList](https://help.aliyun.com/document_detail/2780086.html) operation to query the name of the metatable.
        self.table_name = table_name

    def validate(self):
        if self.sort_criterion:
            self.sort_criterion.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_criterion is not None:
            result['SortCriterion'] = self.sort_criterion.to_map()

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortCriterion') is not None:
            temp_model = main_models.GetMetaTablePartitionRequestSortCriterion()
            self.sort_criterion = temp_model.from_map(m.get('SortCriterion'))

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class GetMetaTablePartitionRequestSortCriterion(DaraModel):
    def __init__(
        self,
        order: str = None,
        sort_field: str = None,
    ):
        # The order in which partitions in the metatable are sorted. Valid values: asc and desc. Default value: desc.
        self.order = order
        # The field that is used to sort partitions in the metatable. Valid values: name and modify_time. By default, partitions in the metatable are sorted based on their creation time.
        self.sort_field = sort_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order is not None:
            result['Order'] = self.order

        if self.sort_field is not None:
            result['SortField'] = self.sort_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')

        return self

