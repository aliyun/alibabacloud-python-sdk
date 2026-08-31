# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetCatalogAssetDetailsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetCatalogAssetDetailsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The data catalog asset details.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend response exception details.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetCatalogAssetDetailsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCatalogAssetDetailsResponseBodyData(DaraModel):
    def __init__(
        self,
        api_call_mode: str = None,
        api_group_name: str = None,
        api_id: int = None,
        api_request_method: str = None,
        asset_description: str = None,
        asset_detail_url: str = None,
        asset_display_name: str = None,
        asset_from: str = None,
        asset_full_name: str = None,
        asset_name: str = None,
        asset_tags: List[str] = None,
        asset_type: str = None,
        bi_catalog: str = None,
        biz_unit_id: int = None,
        biz_unit_name: str = None,
        chart_count: int = None,
        collection_count: int = None,
        columns: List[main_models.GetCatalogAssetDetailsResponseBodyDataColumns] = None,
        create_time: str = None,
        custom_attributes: List[main_models.GetCatalogAssetDetailsResponseBodyDataCustomAttributes] = None,
        data_cell_id: str = None,
        data_cell_name: str = None,
        data_source_name: str = None,
        datasource_id: int = None,
        directories: List[main_models.GetCatalogAssetDetailsResponseBodyDataDirectories] = None,
        first_on_shelve_time: str = None,
        first_on_shelve_user: main_models.GetCatalogAssetDetailsResponseBodyDataFirstOnShelveUser = None,
        granularity: str = None,
        guid: str = None,
        instruction: str = None,
        is_deleted: bool = None,
        is_partition_table: bool = None,
        last_ddl_time: str = None,
        last_dml_time: str = None,
        last_on_shelve_time: str = None,
        last_on_shelve_user: main_models.GetCatalogAssetDetailsResponseBodyDataLastOnShelveUser = None,
        maintain_user_groups: List[str] = None,
        maintain_user_ids: List[str] = None,
        max_security_level: str = None,
        modify_time: str = None,
        owner: main_models.GetCatalogAssetDetailsResponseBodyDataOwner = None,
        partition_key: str = None,
        primary_key: str = None,
        profiling_report_view_scope_type: str = None,
        profiling_report_view_scope_user_groups: List[str] = None,
        profiling_report_view_scope_user_ids: List[str] = None,
        project_id: int = None,
        project_name: str = None,
        quality_score_radar: main_models.GetCatalogAssetDetailsResponseBodyDataQualityScoreRadar = None,
        read_count: int = None,
        shelve_view_scope_type: str = None,
        shelve_view_scope_user_groups: List[str] = None,
        shelve_view_scope_user_ids: List[str] = None,
        simple_node_infos: List[main_models.GetCatalogAssetDetailsResponseBodyDataSimpleNodeInfos] = None,
        sub_type: str = None,
        sum_table_guid: str = None,
        sum_table_name: str = None,
        table_life_cycle: str = None,
        table_size_in_bytes: int = None,
    ):
        # The API call mode. Returned when the asset type is API. Valid values: 1=Synchronous call, 2=Asynchronous call.
        self.api_call_mode = api_call_mode
        # The API group name. Returned when the asset type is API.
        self.api_group_name = api_group_name
        # The API ID. Returned when the asset type is API.
        self.api_id = api_id
        # The API operation type. Returned when the asset type is API. Valid values: 1=Get, 2=List, 3=Create, 4=Update, 5=Delete.
        self.api_request_method = api_request_method
        # The description of the asset.
        self.asset_description = asset_description
        # The URL of the asset catalog detail page.
        self.asset_detail_url = asset_detail_url
        # The display name of the asset. This parameter is returned when the asset type is TABLE, INDEX, or BIZ_INDEX.
        self.asset_display_name = asset_display_name
        # The source of the asset. TABLE (physical table) returns "Dataphin-workspace type-project Chinese name (project English name)". TABLE (logical table) returns "Dataphin-workspace type-data domain Chinese name (data domain English name)". TABLE (data source table) returns "source system name-data source name-database/schema name". INDEX (standard modeling metric) returns the asset source of the associated aggregate logical table. INDEX (custom metric) returns the asset source of the source table. API returns "data service project name". PAGE returns "application system name".
        self.asset_from = asset_from
        # The full name of the asset. This parameter is returned when the asset type is TABLE or INDEX.
        self.asset_full_name = asset_full_name
        # The name of the asset.
        self.asset_name = asset_name
        # The tags of the asset.
        self.asset_tags = asset_tags
        # The asset type. Valid values:
        # - TABLE: table, including views and materialized views.
        # - INDEX: technical metric.
        # - BIZ_INDEX: business metric.
        # - API: API.
        # - PAGE: dashboard.
        self.asset_type = asset_type
        # The BI workspace or folder to which the asset belongs. Returned when the asset type is PAGE (dashboard).
        self.bi_catalog = bi_catalog
        # The ID of the data domain to which the asset belongs. This parameter is returned when the asset type is TABLE (logical tables only) or INDEX (technical metrics whose source table is a logical table only).
        self.biz_unit_id = biz_unit_id
        # The name of the data domain to which the asset belongs. This parameter is returned when the asset type is TABLE (logical tables only) or INDEX (technical metrics whose source table is a logical table only).
        self.biz_unit_name = biz_unit_name
        # The total number of charts. Returned when the asset type is PAGE (dashboard).
        self.chart_count = chart_count
        # The collection count.
        self.collection_count = collection_count
        # The list of columns. This parameter is returned when the asset type is TABLE.
        self.columns = columns
        # The creation time.
        self.create_time = create_time
        # The custom attributes. Returned when includeDetailedAttributes is set to true.
        self.custom_attributes = custom_attributes
        # The ID of the data domain. Returned when the asset type is TABLE (logical tables only) or INDEX (technical metrics whose source table is a logical table only).
        self.data_cell_id = data_cell_id
        # The name of the data domain. Returned when the asset type is TABLE (logical tables only) or INDEX (technical metrics whose source table is a logical table only).
        self.data_cell_name = data_cell_name
        # The name of the data source to which the asset belongs. This parameter is returned when the asset type is TABLE (data source tables only) or INDEX (technical metrics whose source table is a data source table only).
        self.data_source_name = data_source_name
        # The ID of the data source to which the asset belongs. This parameter is returned when the asset type is TABLE (data source tables only) or INDEX (technical metrics whose source table is a data source table only).
        self.datasource_id = datasource_id
        # The directories to which the asset belongs, including topic ID, topic name, directory ID, and directory name.
        self.directories = directories
        # The time of the first listing.
        self.first_on_shelve_time = first_on_shelve_time
        # The user who performed the first listing.
        self.first_on_shelve_user = first_on_shelve_user
        # The statistical granularity name of the technical metric. Returned when the asset type is INDEX.
        self.granularity = granularity
        # The GUID of the asset, which serves as the unique identifier of the asset.
        self.guid = guid
        # The usage instructions.
        self.instruction = instruction
        # Indicates whether the asset is deleted.
        self.is_deleted = is_deleted
        # Indicates whether the table is a partitioned table. Returned when the asset type is TABLE. Valid values:
        # - true: The table is a partitioned table.
        # - false: The table is not a partitioned table.
        self.is_partition_table = is_partition_table
        # The time of the last DDL change.
        self.last_ddl_time = last_ddl_time
        # The time of the last DML update.
        self.last_dml_time = last_dml_time
        # The time of the last listing.
        self.last_on_shelve_time = last_on_shelve_time
        # The user who performed the last listing.
        self.last_on_shelve_user = last_on_shelve_user
        # The listing maintenance user groups.
        self.maintain_user_groups = maintain_user_groups
        # The IDs of the listing maintenance users.
        self.maintain_user_ids = maintain_user_ids
        # The maximum sensitivity level. This parameter is returned when the asset type is TABLE.
        self.max_security_level = max_security_level
        # The modification time.
        self.modify_time = modify_time
        # The owner.
        self.owner = owner
        # The partition key. Returned when the asset type is TABLE.
        self.partition_key = partition_key
        # The primary key. Returned when the asset type is TABLE.
        self.primary_key = primary_key
        # The visibility scope type of the profiling report. This parameter is returned only when the asset type is TABLE or INDEX. Valid values:
        # - ALL_USERS_CAN_VIEW: Visible to all users.
        # - PART_USERS_CAN_VIEW: Visible to some users.
        # - ALL_USERS_CAN_NOT_VIEW: Not visible to any users.
        self.profiling_report_view_scope_type = profiling_report_view_scope_type
        # The user groups within the profiling report visibility scope.
        self.profiling_report_view_scope_user_groups = profiling_report_view_scope_user_groups
        # The users within the profiling report visibility scope.
        self.profiling_report_view_scope_user_ids = profiling_report_view_scope_user_ids
        # The ID of the project to which the asset belongs. This parameter is returned when the asset type is TABLE (physical tables only) or INDEX (technical metrics whose source table is a physical table only).
        self.project_id = project_id
        # The name of the project to which the asset belongs. This parameter is returned when the asset type is TABLE (physical tables only) or INDEX (technical metrics whose source table is a physical table only).
        self.project_name = project_name
        # The quality score radar chart information. This parameter is returned only when includeDetailedAttributes is set to true. It contains the total score, the number of passed/validated rules, and the score details for each dimension.
        self.quality_score_radar = quality_score_radar
        # The view count.
        self.read_count = read_count
        # The visibility scope type. Valid values:
        # - ALL_USERS_CAN_VIEW: Visible to all users.
        # - PART_USERS_CAN_VIEW: Visible to some users.
        # - PART_USERS_CAN_NOT_VIEW: Not visible to some users.
        self.shelve_view_scope_type = shelve_view_scope_type
        # The user groups within the visibility scope.
        self.shelve_view_scope_user_groups = shelve_view_scope_user_groups
        # The users within the visibility scope.
        self.shelve_view_scope_user_ids = shelve_view_scope_user_ids
        # The output nodes. Returned when the asset type is TABLE.
        self.simple_node_infos = simple_node_infos
        # The subtype. Valid values:
        # - DIM_NORMAL: common logical dimension table.
        # - DIM_ENUM: enumeration logical dimension table.
        # - DIM_VIRTUAL: virtual logical dimension table.
        # - SUM_BIZ_UNIT: aggregate logical table.
        # - FACT_EVENT: event fact logical table.
        # - FACT_SNAPSHOT: snapshot fact logical table.
        # - DATASOURCE_TABLE: data source table.
        # - PHYSICAL_TABLE: physical table.
        # - DATASOURCE_VIEW: view (data source view).
        # - PHYSICAL_VIEW: physical view.
        # - MATERIALIZED_VIEW: materialized view.
        # - BIZ_INDEX: business metric.
        # - INDEX: technical metric (standard modeling metric).
        # - CUSTOM_INDEX: technical metric (custom metric).
        self.sub_type = sub_type
        # The GUID of the aggregate table to which the asset belongs. Returned when the asset type is INDEX.
        self.sum_table_guid = sum_table_guid
        # The name of the aggregate table to which the asset belongs. Returned when the asset type is INDEX.
        self.sum_table_name = sum_table_name
        # The lifecycle. Returned when the asset type is TABLE.
        self.table_life_cycle = table_life_cycle
        # The storage size. This parameter is returned only when the asset type is TABLE.
        self.table_size_in_bytes = table_size_in_bytes

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()
        if self.custom_attributes:
            for v1 in self.custom_attributes:
                 if v1:
                    v1.validate()
        if self.directories:
            for v1 in self.directories:
                 if v1:
                    v1.validate()
        if self.first_on_shelve_user:
            self.first_on_shelve_user.validate()
        if self.last_on_shelve_user:
            self.last_on_shelve_user.validate()
        if self.owner:
            self.owner.validate()
        if self.quality_score_radar:
            self.quality_score_radar.validate()
        if self.simple_node_infos:
            for v1 in self.simple_node_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_call_mode is not None:
            result['ApiCallMode'] = self.api_call_mode

        if self.api_group_name is not None:
            result['ApiGroupName'] = self.api_group_name

        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_request_method is not None:
            result['ApiRequestMethod'] = self.api_request_method

        if self.asset_description is not None:
            result['AssetDescription'] = self.asset_description

        if self.asset_detail_url is not None:
            result['AssetDetailUrl'] = self.asset_detail_url

        if self.asset_display_name is not None:
            result['AssetDisplayName'] = self.asset_display_name

        if self.asset_from is not None:
            result['AssetFrom'] = self.asset_from

        if self.asset_full_name is not None:
            result['AssetFullName'] = self.asset_full_name

        if self.asset_name is not None:
            result['AssetName'] = self.asset_name

        if self.asset_tags is not None:
            result['AssetTags'] = self.asset_tags

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.bi_catalog is not None:
            result['BiCatalog'] = self.bi_catalog

        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id

        if self.biz_unit_name is not None:
            result['BizUnitName'] = self.biz_unit_name

        if self.chart_count is not None:
            result['ChartCount'] = self.chart_count

        if self.collection_count is not None:
            result['CollectionCount'] = self.collection_count

        result['Columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['Columns'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['CustomAttributes'] = []
        if self.custom_attributes is not None:
            for k1 in self.custom_attributes:
                result['CustomAttributes'].append(k1.to_map() if k1 else None)

        if self.data_cell_id is not None:
            result['DataCellId'] = self.data_cell_id

        if self.data_cell_name is not None:
            result['DataCellName'] = self.data_cell_name

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        result['Directories'] = []
        if self.directories is not None:
            for k1 in self.directories:
                result['Directories'].append(k1.to_map() if k1 else None)

        if self.first_on_shelve_time is not None:
            result['FirstOnShelveTime'] = self.first_on_shelve_time

        if self.first_on_shelve_user is not None:
            result['FirstOnShelveUser'] = self.first_on_shelve_user.to_map()

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.guid is not None:
            result['Guid'] = self.guid

        if self.instruction is not None:
            result['Instruction'] = self.instruction

        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted

        if self.is_partition_table is not None:
            result['IsPartitionTable'] = self.is_partition_table

        if self.last_ddl_time is not None:
            result['LastDdlTime'] = self.last_ddl_time

        if self.last_dml_time is not None:
            result['LastDmlTime'] = self.last_dml_time

        if self.last_on_shelve_time is not None:
            result['LastOnShelveTime'] = self.last_on_shelve_time

        if self.last_on_shelve_user is not None:
            result['LastOnShelveUser'] = self.last_on_shelve_user.to_map()

        if self.maintain_user_groups is not None:
            result['MaintainUserGroups'] = self.maintain_user_groups

        if self.maintain_user_ids is not None:
            result['MaintainUserIds'] = self.maintain_user_ids

        if self.max_security_level is not None:
            result['MaxSecurityLevel'] = self.max_security_level

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.owner is not None:
            result['Owner'] = self.owner.to_map()

        if self.partition_key is not None:
            result['PartitionKey'] = self.partition_key

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        if self.profiling_report_view_scope_type is not None:
            result['ProfilingReportViewScopeType'] = self.profiling_report_view_scope_type

        if self.profiling_report_view_scope_user_groups is not None:
            result['ProfilingReportViewScopeUserGroups'] = self.profiling_report_view_scope_user_groups

        if self.profiling_report_view_scope_user_ids is not None:
            result['ProfilingReportViewScopeUserIds'] = self.profiling_report_view_scope_user_ids

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.quality_score_radar is not None:
            result['QualityScoreRadar'] = self.quality_score_radar.to_map()

        if self.read_count is not None:
            result['ReadCount'] = self.read_count

        if self.shelve_view_scope_type is not None:
            result['ShelveViewScopeType'] = self.shelve_view_scope_type

        if self.shelve_view_scope_user_groups is not None:
            result['ShelveViewScopeUserGroups'] = self.shelve_view_scope_user_groups

        if self.shelve_view_scope_user_ids is not None:
            result['ShelveViewScopeUserIds'] = self.shelve_view_scope_user_ids

        result['SimpleNodeInfos'] = []
        if self.simple_node_infos is not None:
            for k1 in self.simple_node_infos:
                result['SimpleNodeInfos'].append(k1.to_map() if k1 else None)

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        if self.sum_table_guid is not None:
            result['SumTableGuid'] = self.sum_table_guid

        if self.sum_table_name is not None:
            result['SumTableName'] = self.sum_table_name

        if self.table_life_cycle is not None:
            result['TableLifeCycle'] = self.table_life_cycle

        if self.table_size_in_bytes is not None:
            result['TableSizeInBytes'] = self.table_size_in_bytes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiCallMode') is not None:
            self.api_call_mode = m.get('ApiCallMode')

        if m.get('ApiGroupName') is not None:
            self.api_group_name = m.get('ApiGroupName')

        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiRequestMethod') is not None:
            self.api_request_method = m.get('ApiRequestMethod')

        if m.get('AssetDescription') is not None:
            self.asset_description = m.get('AssetDescription')

        if m.get('AssetDetailUrl') is not None:
            self.asset_detail_url = m.get('AssetDetailUrl')

        if m.get('AssetDisplayName') is not None:
            self.asset_display_name = m.get('AssetDisplayName')

        if m.get('AssetFrom') is not None:
            self.asset_from = m.get('AssetFrom')

        if m.get('AssetFullName') is not None:
            self.asset_full_name = m.get('AssetFullName')

        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')

        if m.get('AssetTags') is not None:
            self.asset_tags = m.get('AssetTags')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('BiCatalog') is not None:
            self.bi_catalog = m.get('BiCatalog')

        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('BizUnitName') is not None:
            self.biz_unit_name = m.get('BizUnitName')

        if m.get('ChartCount') is not None:
            self.chart_count = m.get('ChartCount')

        if m.get('CollectionCount') is not None:
            self.collection_count = m.get('CollectionCount')

        self.columns = []
        if m.get('Columns') is not None:
            for k1 in m.get('Columns'):
                temp_model = main_models.GetCatalogAssetDetailsResponseBodyDataColumns()
                self.columns.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.custom_attributes = []
        if m.get('CustomAttributes') is not None:
            for k1 in m.get('CustomAttributes'):
                temp_model = main_models.GetCatalogAssetDetailsResponseBodyDataCustomAttributes()
                self.custom_attributes.append(temp_model.from_map(k1))

        if m.get('DataCellId') is not None:
            self.data_cell_id = m.get('DataCellId')

        if m.get('DataCellName') is not None:
            self.data_cell_name = m.get('DataCellName')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        self.directories = []
        if m.get('Directories') is not None:
            for k1 in m.get('Directories'):
                temp_model = main_models.GetCatalogAssetDetailsResponseBodyDataDirectories()
                self.directories.append(temp_model.from_map(k1))

        if m.get('FirstOnShelveTime') is not None:
            self.first_on_shelve_time = m.get('FirstOnShelveTime')

        if m.get('FirstOnShelveUser') is not None:
            temp_model = main_models.GetCatalogAssetDetailsResponseBodyDataFirstOnShelveUser()
            self.first_on_shelve_user = temp_model.from_map(m.get('FirstOnShelveUser'))

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        if m.get('Instruction') is not None:
            self.instruction = m.get('Instruction')

        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')

        if m.get('IsPartitionTable') is not None:
            self.is_partition_table = m.get('IsPartitionTable')

        if m.get('LastDdlTime') is not None:
            self.last_ddl_time = m.get('LastDdlTime')

        if m.get('LastDmlTime') is not None:
            self.last_dml_time = m.get('LastDmlTime')

        if m.get('LastOnShelveTime') is not None:
            self.last_on_shelve_time = m.get('LastOnShelveTime')

        if m.get('LastOnShelveUser') is not None:
            temp_model = main_models.GetCatalogAssetDetailsResponseBodyDataLastOnShelveUser()
            self.last_on_shelve_user = temp_model.from_map(m.get('LastOnShelveUser'))

        if m.get('MaintainUserGroups') is not None:
            self.maintain_user_groups = m.get('MaintainUserGroups')

        if m.get('MaintainUserIds') is not None:
            self.maintain_user_ids = m.get('MaintainUserIds')

        if m.get('MaxSecurityLevel') is not None:
            self.max_security_level = m.get('MaxSecurityLevel')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Owner') is not None:
            temp_model = main_models.GetCatalogAssetDetailsResponseBodyDataOwner()
            self.owner = temp_model.from_map(m.get('Owner'))

        if m.get('PartitionKey') is not None:
            self.partition_key = m.get('PartitionKey')

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        if m.get('ProfilingReportViewScopeType') is not None:
            self.profiling_report_view_scope_type = m.get('ProfilingReportViewScopeType')

        if m.get('ProfilingReportViewScopeUserGroups') is not None:
            self.profiling_report_view_scope_user_groups = m.get('ProfilingReportViewScopeUserGroups')

        if m.get('ProfilingReportViewScopeUserIds') is not None:
            self.profiling_report_view_scope_user_ids = m.get('ProfilingReportViewScopeUserIds')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('QualityScoreRadar') is not None:
            temp_model = main_models.GetCatalogAssetDetailsResponseBodyDataQualityScoreRadar()
            self.quality_score_radar = temp_model.from_map(m.get('QualityScoreRadar'))

        if m.get('ReadCount') is not None:
            self.read_count = m.get('ReadCount')

        if m.get('ShelveViewScopeType') is not None:
            self.shelve_view_scope_type = m.get('ShelveViewScopeType')

        if m.get('ShelveViewScopeUserGroups') is not None:
            self.shelve_view_scope_user_groups = m.get('ShelveViewScopeUserGroups')

        if m.get('ShelveViewScopeUserIds') is not None:
            self.shelve_view_scope_user_ids = m.get('ShelveViewScopeUserIds')

        self.simple_node_infos = []
        if m.get('SimpleNodeInfos') is not None:
            for k1 in m.get('SimpleNodeInfos'):
                temp_model = main_models.GetCatalogAssetDetailsResponseBodyDataSimpleNodeInfos()
                self.simple_node_infos.append(temp_model.from_map(k1))

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('SumTableGuid') is not None:
            self.sum_table_guid = m.get('SumTableGuid')

        if m.get('SumTableName') is not None:
            self.sum_table_name = m.get('SumTableName')

        if m.get('TableLifeCycle') is not None:
            self.table_life_cycle = m.get('TableLifeCycle')

        if m.get('TableSizeInBytes') is not None:
            self.table_size_in_bytes = m.get('TableSizeInBytes')

        return self

class GetCatalogAssetDetailsResponseBodyDataSimpleNodeInfos(DaraModel):
    def __init__(
        self,
        biz_unit: str = None,
        env: str = None,
        node_id: str = None,
        node_name: str = None,
        node_schedule_type: str = None,
        owners: List[main_models.GetCatalogAssetDetailsResponseBodyDataSimpleNodeInfosOwners] = None,
        project: main_models.GetCatalogAssetDetailsResponseBodyDataSimpleNodeInfosProject = None,
        sub_biz_type: str = None,
    ):
        # The business unit to which the node belongs.
        self.biz_unit = biz_unit
        # The environment to which the asset belongs.
        self.env = env
        # The node ID.
        self.node_id = node_id
        # The node name.
        self.node_name = node_name
        # The scheduling type. Valid values: NORMAL (timed scheduling), MANUAL (manual scheduling).
        self.node_schedule_type = node_schedule_type
        # The list of O&M owners.
        self.owners = owners
        # The project to which the node belongs.
        self.project = project
        # The node type. Example valid values: DLINK (offline integration), PYTHON37 (Python compute node).
        self.sub_biz_type = sub_biz_type

    def validate(self):
        if self.owners:
            for v1 in self.owners:
                 if v1:
                    v1.validate()
        if self.project:
            self.project.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_unit is not None:
            result['BizUnit'] = self.biz_unit

        if self.env is not None:
            result['Env'] = self.env

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_schedule_type is not None:
            result['NodeScheduleType'] = self.node_schedule_type

        result['Owners'] = []
        if self.owners is not None:
            for k1 in self.owners:
                result['Owners'].append(k1.to_map() if k1 else None)

        if self.project is not None:
            result['Project'] = self.project.to_map()

        if self.sub_biz_type is not None:
            result['SubBizType'] = self.sub_biz_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnit') is not None:
            self.biz_unit = m.get('BizUnit')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeScheduleType') is not None:
            self.node_schedule_type = m.get('NodeScheduleType')

        self.owners = []
        if m.get('Owners') is not None:
            for k1 in m.get('Owners'):
                temp_model = main_models.GetCatalogAssetDetailsResponseBodyDataSimpleNodeInfosOwners()
                self.owners.append(temp_model.from_map(k1))

        if m.get('Project') is not None:
            temp_model = main_models.GetCatalogAssetDetailsResponseBodyDataSimpleNodeInfosProject()
            self.project = temp_model.from_map(m.get('Project'))

        if m.get('SubBizType') is not None:
            self.sub_biz_type = m.get('SubBizType')

        return self

class GetCatalogAssetDetailsResponseBodyDataSimpleNodeInfosProject(DaraModel):
    def __init__(
        self,
        project_id: str = None,
        project_name: str = None,
    ):
        # The project ID.
        self.project_id = project_id
        # The project name.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

class GetCatalogAssetDetailsResponseBodyDataSimpleNodeInfosOwners(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        user_id: str = None,
    ):
        # The username.
        self.display_name = display_name
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetCatalogAssetDetailsResponseBodyDataQualityScoreRadar(DaraModel):
    def __init__(
        self,
        catalog_scores: List[main_models.GetCatalogAssetDetailsResponseBodyDataQualityScoreRadarCatalogScores] = None,
        pass_rule_count: int = None,
        total_score: float = None,
        validate_rule_count: int = None,
    ):
        # The list of dimension scores.
        self.catalog_scores = catalog_scores
        # The number of passed rules.
        self.pass_rule_count = pass_rule_count
        # The total quality score.
        self.total_score = total_score
        # The number of validated rules.
        self.validate_rule_count = validate_rule_count

    def validate(self):
        if self.catalog_scores:
            for v1 in self.catalog_scores:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CatalogScores'] = []
        if self.catalog_scores is not None:
            for k1 in self.catalog_scores:
                result['CatalogScores'].append(k1.to_map() if k1 else None)

        if self.pass_rule_count is not None:
            result['PassRuleCount'] = self.pass_rule_count

        if self.total_score is not None:
            result['TotalScore'] = self.total_score

        if self.validate_rule_count is not None:
            result['ValidateRuleCount'] = self.validate_rule_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.catalog_scores = []
        if m.get('CatalogScores') is not None:
            for k1 in m.get('CatalogScores'):
                temp_model = main_models.GetCatalogAssetDetailsResponseBodyDataQualityScoreRadarCatalogScores()
                self.catalog_scores.append(temp_model.from_map(k1))

        if m.get('PassRuleCount') is not None:
            self.pass_rule_count = m.get('PassRuleCount')

        if m.get('TotalScore') is not None:
            self.total_score = m.get('TotalScore')

        if m.get('ValidateRuleCount') is not None:
            self.validate_rule_count = m.get('ValidateRuleCount')

        return self

class GetCatalogAssetDetailsResponseBodyDataQualityScoreRadarCatalogScores(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        field_rule_count: int = None,
        pass_rate: float = None,
        pass_rule_count: int = None,
        score: float = None,
        table_rule_count: int = None,
        validate_rule_count: int = None,
    ):
        # The dimension name.
        self.catalog = catalog
        # The number of field-level rules.
        self.field_rule_count = field_rule_count
        # The pass rate.
        self.pass_rate = pass_rate
        # The number of passed rules.
        self.pass_rule_count = pass_rule_count
        # The dimension score.
        self.score = score
        # The number of table-level rules.
        self.table_rule_count = table_rule_count
        # The number of validated rules.
        self.validate_rule_count = validate_rule_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.field_rule_count is not None:
            result['FieldRuleCount'] = self.field_rule_count

        if self.pass_rate is not None:
            result['PassRate'] = self.pass_rate

        if self.pass_rule_count is not None:
            result['PassRuleCount'] = self.pass_rule_count

        if self.score is not None:
            result['Score'] = self.score

        if self.table_rule_count is not None:
            result['TableRuleCount'] = self.table_rule_count

        if self.validate_rule_count is not None:
            result['ValidateRuleCount'] = self.validate_rule_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('FieldRuleCount') is not None:
            self.field_rule_count = m.get('FieldRuleCount')

        if m.get('PassRate') is not None:
            self.pass_rate = m.get('PassRate')

        if m.get('PassRuleCount') is not None:
            self.pass_rule_count = m.get('PassRuleCount')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('TableRuleCount') is not None:
            self.table_rule_count = m.get('TableRuleCount')

        if m.get('ValidateRuleCount') is not None:
            self.validate_rule_count = m.get('ValidateRuleCount')

        return self

class GetCatalogAssetDetailsResponseBodyDataOwner(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        user_id: str = None,
    ):
        # The username.
        self.display_name = display_name
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetCatalogAssetDetailsResponseBodyDataLastOnShelveUser(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        user_id: str = None,
    ):
        # The username.
        self.display_name = display_name
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetCatalogAssetDetailsResponseBodyDataFirstOnShelveUser(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        user_id: str = None,
    ):
        # The username.
        self.display_name = display_name
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetCatalogAssetDetailsResponseBodyDataDirectories(DaraModel):
    def __init__(
        self,
        directory_chain: List[main_models.GetCatalogAssetDetailsResponseBodyDataDirectoriesDirectoryChain] = None,
        directory_description: str = None,
        directory_id: int = None,
        directory_name: str = None,
        topic_description: str = None,
        topic_id: int = None,
        topic_name: str = None,
    ):
        # The complete directory hierarchy chain from the top-level directory to the current directory, including the current directory.
        self.directory_chain = directory_chain
        # The directory description.
        self.directory_description = directory_description
        # The directory ID.
        self.directory_id = directory_id
        # The directory name.
        self.directory_name = directory_name
        # The topic description.
        self.topic_description = topic_description
        # The topic ID.
        self.topic_id = topic_id
        # The topic name.
        self.topic_name = topic_name

    def validate(self):
        if self.directory_chain:
            for v1 in self.directory_chain:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DirectoryChain'] = []
        if self.directory_chain is not None:
            for k1 in self.directory_chain:
                result['DirectoryChain'].append(k1.to_map() if k1 else None)

        if self.directory_description is not None:
            result['DirectoryDescription'] = self.directory_description

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name

        if self.topic_description is not None:
            result['TopicDescription'] = self.topic_description

        if self.topic_id is not None:
            result['TopicId'] = self.topic_id

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.directory_chain = []
        if m.get('DirectoryChain') is not None:
            for k1 in m.get('DirectoryChain'):
                temp_model = main_models.GetCatalogAssetDetailsResponseBodyDataDirectoriesDirectoryChain()
                self.directory_chain.append(temp_model.from_map(k1))

        if m.get('DirectoryDescription') is not None:
            self.directory_description = m.get('DirectoryDescription')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')

        if m.get('TopicDescription') is not None:
            self.topic_description = m.get('TopicDescription')

        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self

class GetCatalogAssetDetailsResponseBodyDataDirectoriesDirectoryChain(DaraModel):
    def __init__(
        self,
        directory_description: str = None,
        directory_id: int = None,
        directory_name: str = None,
        level: int = None,
    ):
        # The directory description.
        self.directory_description = directory_description
        # The directory ID.
        self.directory_id = directory_id
        # The directory name.
        self.directory_name = directory_name
        # The folder level.
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_description is not None:
            result['DirectoryDescription'] = self.directory_description

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name

        if self.level is not None:
            result['Level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryDescription') is not None:
            self.directory_description = m.get('DirectoryDescription')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        return self

class GetCatalogAssetDetailsResponseBodyDataCustomAttributes(DaraModel):
    def __init__(
        self,
        attr_type: str = None,
        code: str = None,
        name: str = None,
        value: str = None,
    ):
        # The attribute type. Valid values: BUSINESS (business attribute), MANAGEMENT (management attribute), TECHNOLOGY (technical attribute).
        self.attr_type = attr_type
        # The attribute code.
        self.code = code
        # The attribute name.
        self.name = name
        # The attribute value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attr_type is not None:
            result['AttrType'] = self.attr_type

        if self.code is not None:
            result['Code'] = self.code

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttrType') is not None:
            self.attr_type = m.get('AttrType')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetCatalogAssetDetailsResponseBodyDataColumns(DaraModel):
    def __init__(
        self,
        associated_entity: main_models.GetCatalogAssetDetailsResponseBodyDataColumnsAssociatedEntity = None,
        biz_type: str = None,
        classify_name: str = None,
        data_type: str = None,
        description: str = None,
        display_name: str = None,
        guid: str = None,
        level_short_name: str = None,
        name: str = None,
        quality_score: float = None,
        standards: List[main_models.GetCatalogAssetDetailsResponseBodyDataColumnsStandards] = None,
    ):
        # The associated entity. This parameter is returned when the business type is DIMENSION.
        self.associated_entity = associated_entity
        # The business type. Valid values:
        # - INDEX: metric.
        # - STAT_PERIOD: statistical period.
        # - DIMENSION: dimension.
        self.biz_type = biz_type
        # The data classification.
        self.classify_name = classify_name
        # The data type of the column.
        self.data_type = data_type
        # The description of the column.
        self.description = description
        # The display name of the column.
        self.display_name = display_name
        # The GUID of the column.
        self.guid = guid
        # The data classification level.
        self.level_short_name = level_short_name
        # The name of the column.
        self.name = name
        # The quality score.
        self.quality_score = quality_score
        # The associated standards.
        self.standards = standards

    def validate(self):
        if self.associated_entity:
            self.associated_entity.validate()
        if self.standards:
            for v1 in self.standards:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_entity is not None:
            result['AssociatedEntity'] = self.associated_entity.to_map()

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.classify_name is not None:
            result['ClassifyName'] = self.classify_name

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.guid is not None:
            result['Guid'] = self.guid

        if self.level_short_name is not None:
            result['LevelShortName'] = self.level_short_name

        if self.name is not None:
            result['Name'] = self.name

        if self.quality_score is not None:
            result['QualityScore'] = self.quality_score

        result['Standards'] = []
        if self.standards is not None:
            for k1 in self.standards:
                result['Standards'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedEntity') is not None:
            temp_model = main_models.GetCatalogAssetDetailsResponseBodyDataColumnsAssociatedEntity()
            self.associated_entity = temp_model.from_map(m.get('AssociatedEntity'))

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ClassifyName') is not None:
            self.classify_name = m.get('ClassifyName')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        if m.get('LevelShortName') is not None:
            self.level_short_name = m.get('LevelShortName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('QualityScore') is not None:
            self.quality_score = m.get('QualityScore')

        self.standards = []
        if m.get('Standards') is not None:
            for k1 in m.get('Standards'):
                temp_model = main_models.GetCatalogAssetDetailsResponseBodyDataColumnsStandards()
                self.standards.append(temp_model.from_map(k1))

        return self

class GetCatalogAssetDetailsResponseBodyDataColumnsStandards(DaraModel):
    def __init__(
        self,
        code: str = None,
        id: int = None,
        name: str = None,
    ):
        # The code of the standard.
        self.code = code
        # The ID of the standard.
        self.id = id
        # The name of the standard.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetCatalogAssetDetailsResponseBodyDataColumnsAssociatedEntity(DaraModel):
    def __init__(
        self,
        biz_unit_id: int = None,
        biz_unit_name: str = None,
        dimension_display_name: str = None,
        dimension_id: int = None,
        dimension_name: str = None,
    ):
        # The ID of the business unit.
        self.biz_unit_id = biz_unit_id
        # The name of the business unit.
        self.biz_unit_name = biz_unit_name
        # The display name of the dimension.
        self.dimension_display_name = dimension_display_name
        # The ID of the dimension.
        self.dimension_id = dimension_id
        # The name of the dimension.
        self.dimension_name = dimension_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id

        if self.biz_unit_name is not None:
            result['BizUnitName'] = self.biz_unit_name

        if self.dimension_display_name is not None:
            result['DimensionDisplayName'] = self.dimension_display_name

        if self.dimension_id is not None:
            result['DimensionId'] = self.dimension_id

        if self.dimension_name is not None:
            result['DimensionName'] = self.dimension_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('BizUnitName') is not None:
            self.biz_unit_name = m.get('BizUnitName')

        if m.get('DimensionDisplayName') is not None:
            self.dimension_display_name = m.get('DimensionDisplayName')

        if m.get('DimensionId') is not None:
            self.dimension_id = m.get('DimensionId')

        if m.get('DimensionName') is not None:
            self.dimension_name = m.get('DimensionName')

        return self

