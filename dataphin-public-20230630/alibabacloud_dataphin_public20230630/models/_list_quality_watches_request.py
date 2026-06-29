# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListQualityWatchesRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListQualityWatchesRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        # The paged query conditions.
        self.list_query = list_query
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = main_models.ListQualityWatchesRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListQualityWatchesRequestListQuery(DaraModel):
    def __init__(
        self,
        biz_unit_name_list: List[str] = None,
        current_user_owned: bool = None,
        data_source_id_list: List[int] = None,
        data_source_owner_list: List[str] = None,
        data_source_scope_list: List[str] = None,
        data_source_type_list: List[str] = None,
        index_compute_type_list: List[str] = None,
        index_owner_list: List[str] = None,
        keyword: str = None,
        latest_watch_task_status_list: List[str] = None,
        page_no: int = None,
        page_size: int = None,
        project_name_list: List[str] = None,
        quality_owner_list: List[str] = None,
        status_list: List[str] = None,
        table_owner_list: List[str] = None,
        table_type_list: List[str] = None,
        watch_type_list: List[str] = None,
    ):
        # The business unit names.
        self.biz_unit_name_list = biz_unit_name_list
        # Specifies whether to query only monitored objects owned by the current user.
        self.current_user_owned = current_user_owned
        # The data source IDs.
        self.data_source_id_list = data_source_id_list
        # The data source owners.
        self.data_source_owner_list = data_source_owner_list
        # The data source scope. Valid values:
        # - STREAMING: real-time only
        # - OFFLINE: offline only
        # - ALL: real-time and offline.
        self.data_source_scope_list = data_source_scope_list
        # The data source type, such as MAX_COMPUTE, HADOOP, or MYSQL.
        self.data_source_type_list = data_source_type_list
        # The metric computation type. Valid values:
        # - AUTO: automated coding
        # - CUSTOM: expert coding
        # - MOUNT: external table registration
        # - COMBINE: derived metric specific.
        self.index_compute_type_list = index_compute_type_list
        # The metric owners.
        self.index_owner_list = index_owner_list
        # The search keyword. This is the name of the monitored table.
        self.keyword = keyword
        # The task status. Valid values:
        # - NOT_RUN: not executed
        # - WAITING: waiting
        # - RUNNING: executing
        # - SUCCESS: executed successfully
        # - FAILED: execution failed
        # - CANCEL: canceled
        # - TIMEOUT: timed out
        # - OFFLINE: offline.
        self.latest_watch_task_status_list = latest_watch_task_status_list
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of records per page. Default value: 20.
        self.page_size = page_size
        # The project names.
        self.project_name_list = project_name_list
        # The quality owners.
        self.quality_owner_list = quality_owner_list
        # The status of the monitored object. Valid values:
        # - ENABLE: enabled
        # - DISABLE: disabled.
        self.status_list = status_list
        # The table owners.
        self.table_owner_list = table_owner_list
        # The table type. Valid values:
        # - LOGIC_DIM_TABLE: logical dimension table
        # - LOGIC_FACT_TABLE: logical fact table
        # - LOGIC_SUM_TABLE: logical aggregate table
        # - LOGIC_LABEL_TABLE: logical label table
        # - PHYSICAL_TABLE: physical table
        # - REALTIME_LOGICAL_TABLE: real-time meta table.
        self.table_type_list = table_type_list
        # The monitored object type. Valid values:
        # - TABLE: Dataphin table
        # - DATASOURCE_TABLE: full-domain table
        # - DATASOURCE: data source
        # - INDEX: metric
        # - REALTIME_LOGICAL_TABLE: real-time meta table.
        self.watch_type_list = watch_type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_unit_name_list is not None:
            result['BizUnitNameList'] = self.biz_unit_name_list

        if self.current_user_owned is not None:
            result['CurrentUserOwned'] = self.current_user_owned

        if self.data_source_id_list is not None:
            result['DataSourceIdList'] = self.data_source_id_list

        if self.data_source_owner_list is not None:
            result['DataSourceOwnerList'] = self.data_source_owner_list

        if self.data_source_scope_list is not None:
            result['DataSourceScopeList'] = self.data_source_scope_list

        if self.data_source_type_list is not None:
            result['DataSourceTypeList'] = self.data_source_type_list

        if self.index_compute_type_list is not None:
            result['IndexComputeTypeList'] = self.index_compute_type_list

        if self.index_owner_list is not None:
            result['IndexOwnerList'] = self.index_owner_list

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.latest_watch_task_status_list is not None:
            result['LatestWatchTaskStatusList'] = self.latest_watch_task_status_list

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_name_list is not None:
            result['ProjectNameList'] = self.project_name_list

        if self.quality_owner_list is not None:
            result['QualityOwnerList'] = self.quality_owner_list

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.table_owner_list is not None:
            result['TableOwnerList'] = self.table_owner_list

        if self.table_type_list is not None:
            result['TableTypeList'] = self.table_type_list

        if self.watch_type_list is not None:
            result['WatchTypeList'] = self.watch_type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitNameList') is not None:
            self.biz_unit_name_list = m.get('BizUnitNameList')

        if m.get('CurrentUserOwned') is not None:
            self.current_user_owned = m.get('CurrentUserOwned')

        if m.get('DataSourceIdList') is not None:
            self.data_source_id_list = m.get('DataSourceIdList')

        if m.get('DataSourceOwnerList') is not None:
            self.data_source_owner_list = m.get('DataSourceOwnerList')

        if m.get('DataSourceScopeList') is not None:
            self.data_source_scope_list = m.get('DataSourceScopeList')

        if m.get('DataSourceTypeList') is not None:
            self.data_source_type_list = m.get('DataSourceTypeList')

        if m.get('IndexComputeTypeList') is not None:
            self.index_compute_type_list = m.get('IndexComputeTypeList')

        if m.get('IndexOwnerList') is not None:
            self.index_owner_list = m.get('IndexOwnerList')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('LatestWatchTaskStatusList') is not None:
            self.latest_watch_task_status_list = m.get('LatestWatchTaskStatusList')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectNameList') is not None:
            self.project_name_list = m.get('ProjectNameList')

        if m.get('QualityOwnerList') is not None:
            self.quality_owner_list = m.get('QualityOwnerList')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('TableOwnerList') is not None:
            self.table_owner_list = m.get('TableOwnerList')

        if m.get('TableTypeList') is not None:
            self.table_type_list = m.get('TableTypeList')

        if m.get('WatchTypeList') is not None:
            self.watch_type_list = m.get('WatchTypeList')

        return self

