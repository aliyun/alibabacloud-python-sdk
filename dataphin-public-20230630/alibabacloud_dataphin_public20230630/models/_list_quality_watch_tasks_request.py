# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListQualityWatchTasksRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListQualityWatchTasksRequestListQuery = None,
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
            temp_model = main_models.ListQualityWatchTasksRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListQualityWatchTasksRequestListQuery(DaraModel):
    def __init__(
        self,
        biz_date: str = None,
        biz_unit_name_list: List[str] = None,
        current_user_owned: bool = None,
        data_source_id_list: List[str] = None,
        data_source_owner_list: List[str] = None,
        data_source_scope_list: List[str] = None,
        data_source_type_list: List[str] = None,
        error_rule_strength_list: List[str] = None,
        keyword: str = None,
        page_no: int = None,
        page_size: int = None,
        project_name_list: List[str] = None,
        quality_owner_list: List[str] = None,
        status_list: List[str] = None,
        table_owner_list: List[str] = None,
        table_type_list: List[str] = None,
        watch_type_list: List[str] = None,
    ):
        # The business date filter.
        self.biz_date = biz_date
        # The business unit names.
        self.biz_unit_name_list = biz_unit_name_list
        # Specifies whether to query only the quality monitoring node objects owned by the current user.
        self.current_user_owned = current_user_owned
        # The data source IDs.
        self.data_source_id_list = data_source_id_list
        # The data source owners.
        self.data_source_owner_list = data_source_owner_list
        # The data source scopes. Valid values:
        # - STREAMING: real-time only.
        # - OFFLINE: offline only.
        # - ALL: real-time and offline.
        self.data_source_scope_list = data_source_scope_list
        # The data source types, such as MAX_COMPUTE, HADOOP, and MYSQL.
        self.data_source_type_list = data_source_type_list
        # The rule exception types. Valid values:
        # - STRONG: strong.
        # - WEAK: weak.
        self.error_rule_strength_list = error_rule_strength_list
        # The search keyword, which is the name of the monitored table.
        self.keyword = keyword
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The project names.
        self.project_name_list = project_name_list
        # The quality owners.
        self.quality_owner_list = quality_owner_list
        # The task statuses. Valid values:
        # - NOT_RUN: not executed.
        # - WAITING: waiting.
        # - RUNNING: running.
        # - SUCCESS: succeeded.
        # - FAILED: failed.
        # - CANCEL: canceled.
        # - TIMEOUT: timed out.
        # - OFFLINE: offline.
        self.status_list = status_list
        # The table owners.
        self.table_owner_list = table_owner_list
        # The table types. Valid values:
        # - LOGIC_DIM_TABLE: logical dimension table.
        # - LOGIC_FACT_TABLE: logical fact table.
        # - LOGIC_SUM_TABLE: logical aggregate table.
        # - LOGIC_LABEL_TABLE: logical label table.
        # - PHYSICAL_TABLE: physical table.
        # - REALTIME_LOGICAL_TABLE: real-time meta table.
        self.table_type_list = table_type_list
        # The monitored object types. Valid values:
        # - TABLE: Dataphin table.
        # - DATASOURCE_TABLE: global table.
        # - DATASOURCE: data source.
        # - INDEX: metric.
        # - REALTIME_LOGICAL_TABLE: real-time meta table.
        self.watch_type_list = watch_type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

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

        if self.error_rule_strength_list is not None:
            result['ErrorRuleStrengthList'] = self.error_rule_strength_list

        if self.keyword is not None:
            result['Keyword'] = self.keyword

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
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

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

        if m.get('ErrorRuleStrengthList') is not None:
            self.error_rule_strength_list = m.get('ErrorRuleStrengthList')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

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

