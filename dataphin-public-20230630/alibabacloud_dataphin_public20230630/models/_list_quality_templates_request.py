# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListQualityTemplatesRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListQualityTemplatesRequestListQuery = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The paged query conditions.
        self.list_query = list_query
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator user.
        self.op_user_id = op_user_id

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

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = main_models.ListQualityTemplatesRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class ListQualityTemplatesRequestListQuery(DaraModel):
    def __init__(
        self,
        catalog_list: List[str] = None,
        current_user_owned: bool = None,
        keyword: str = None,
        page_no: int = None,
        page_size: int = None,
        support_data_source_type_list: List[str] = None,
        template_owner_list: List[str] = None,
        template_source_list: List[str] = None,
        template_type_list: List[str] = None,
        watch_type_list: List[str] = None,
    ):
        # The rule types. Valid values:
        # - CONSISTENT: Consistency.
        # - EFFECTIVE: Effectiveness.
        # - TIMELINESE: Timeliness.
        # - ACCURATE: Accuracy.
        # - UNIQUENESS: Uniqueness.
        # - COMPLETENESS: Completeness.
        # - STABILITY: Stability.
        # - CUSTOM: Custom.
        self.catalog_list = catalog_list
        # Specifies whether the template is owned by the current user.
        self.current_user_owned = current_user_owned
        # The search keyword filter, which supports template names.
        self.keyword = keyword
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The supported data source types, such as MAX_COMPUTE, MYSQL, and HIVE.
        self.support_data_source_type_list = support_data_source_type_list
        # The template owners.
        self.template_owner_list = template_owner_list
        # The template sources. Valid values:
        # - SYSTEM: System template.
        # - CUSTOM: Custom template.
        self.template_source_list = template_source_list
        # The templatetype. Valid values:
        # - FIELD_NULL_VALUE_VALIDATE: Field null value check.
        # - FIELD_EMPTY_STRING_VALIDATE: Field empty character check.
        # - FIELD_UNIQUE_VALIDATE: Field uniqueness check.
        # - FIELD_GROUP_COUNT_VALIDATE: Field unique value count check.
        # - FIELD_DUPLICATE_VALUE_COUNT_VALIDATE: Field duplicate value count check.
        # - FUNCTION_TIME_COMPARE: Time function comparison.
        # - SINGLE_TABLE_TIME_COMPARE: Non-partitioned table time field comparison.
        # - DOUBLE_TABLE_TIME_COMPARE: Two-table time field comparison.
        # - FIELD_FORMAT_VALIDATE: Field format check.
        # - FIELD_LENGTH_VALIDATE: Field length check.
        # - FIELD_VALUE_RANGE_VALIDATE: Field value range check.
        # - CODE_TABLE_COMPARE: Lookup table reference comparison.
        # - STANDARD_CODE_TABLE_COMPARE: Data standard lookup table reference comparison.
        # - SINGLE_TABLE_FIELD_VALUE_COMPARE: Non-partitioned table field value consistency comparison.
        # - SINGLE_TABLE_FIELD_STATISTICAL_COMPARE: Non-partitioned table field statistical value consistency comparison.
        # - SINGLE_TABLE_FIELD_EXP_COMPARE: Non-partitioned table field business logic consistency comparison.
        # - DOUBLE_TABLE_FIELD_VALUE_COMPARE: Two-table field value consistency comparison.
        # - DOUBLE_TABLE_FIELD_STATISTICAL_COMPARE: Two-table field statistical value consistency comparison.
        # - CROSS_DOUBLE_TABLE_FIELD_STATISTICAL_COMPARE: Cross-source two-table field statistical value consistency comparison.
        # - DOUBLE_TABLE_FIELD_EXP_COMPARE: Two-table field business logic consistency comparison.
        # - TABLE_STABILITY_VALIDATE: Table stability check.
        # - TABLE_FLUCTUATION_VALIDATE: Table fluctuation check.
        # - FIELD_STABILITY_VALIDATE: Field stability check.
        # - FIELD_FLUCTUATION_VALIDATE: Field fluctuation check.
        # - CUSTOM_STATISTICAL_VALIDATE: Custom statistical metric check.
        # - CUSTOM_DATA_DETAILS_VALIDATE: Custom data details check.
        # - DATASOURCE_AVAILABLE_CHECK: Data source connectivity monitoring.
        # - TABLE_SCHEMA_CHECK: Table schema change monitoring.
        # - REAL_TIME_OFFLINE_COMPARE: Real-time and offline comparison.
        # - REAL_TIME_STATISTICAL_VALIDATE: Real-time statistical value monitoring.
        # - REAL_TIME_MULTI_CHAIN_COMPARE: Real-time multi-link comparison.
        self.template_type_list = template_type_list
        # The monitored object types. Valid values:
        # - TABLE: Dataphin table.
        # - DATASOURCE_TABLE: Global table.
        # - DATASOURCE: Data source.
        # - INDEX: Metric.
        # - REALTIME_LOGICAL_TABLE: Real-time metadata table.
        self.watch_type_list = watch_type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_list is not None:
            result['CatalogList'] = self.catalog_list

        if self.current_user_owned is not None:
            result['CurrentUserOwned'] = self.current_user_owned

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.support_data_source_type_list is not None:
            result['SupportDataSourceTypeList'] = self.support_data_source_type_list

        if self.template_owner_list is not None:
            result['TemplateOwnerList'] = self.template_owner_list

        if self.template_source_list is not None:
            result['TemplateSourceList'] = self.template_source_list

        if self.template_type_list is not None:
            result['TemplateTypeList'] = self.template_type_list

        if self.watch_type_list is not None:
            result['WatchTypeList'] = self.watch_type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogList') is not None:
            self.catalog_list = m.get('CatalogList')

        if m.get('CurrentUserOwned') is not None:
            self.current_user_owned = m.get('CurrentUserOwned')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SupportDataSourceTypeList') is not None:
            self.support_data_source_type_list = m.get('SupportDataSourceTypeList')

        if m.get('TemplateOwnerList') is not None:
            self.template_owner_list = m.get('TemplateOwnerList')

        if m.get('TemplateSourceList') is not None:
            self.template_source_list = m.get('TemplateSourceList')

        if m.get('TemplateTypeList') is not None:
            self.template_type_list = m.get('TemplateTypeList')

        if m.get('WatchTypeList') is not None:
            self.watch_type_list = m.get('WatchTypeList')

        return self

