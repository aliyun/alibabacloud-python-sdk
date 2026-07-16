# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListCatalogAssetsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListCatalogAssetsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The data catalog asset list.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of the backend response exception.
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
            temp_model = main_models.ListCatalogAssetsResponseBodyData()
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

class ListCatalogAssetsResponseBodyData(DaraModel):
    def __init__(
        self,
        asset_list: List[main_models.ListCatalogAssetsResponseBodyDataAssetList] = None,
        total_count: int = None,
    ):
        # The asset list.
        self.asset_list = asset_list
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.asset_list:
            for v1 in self.asset_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssetList'] = []
        if self.asset_list is not None:
            for k1 in self.asset_list:
                result['AssetList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asset_list = []
        if m.get('AssetList') is not None:
            for k1 in m.get('AssetList'):
                temp_model = main_models.ListCatalogAssetsResponseBodyDataAssetList()
                self.asset_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCatalogAssetsResponseBodyDataAssetList(DaraModel):
    def __init__(
        self,
        api_call_mode: str = None,
        api_group_name: str = None,
        api_id: int = None,
        api_request_method: str = None,
        asset_description: str = None,
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
        data_cell_id: str = None,
        data_cell_name: str = None,
        data_source_name: str = None,
        datasource_id: int = None,
        directories: List[main_models.ListCatalogAssetsResponseBodyDataAssetListDirectories] = None,
        granularity: str = None,
        guid: str = None,
        is_deleted: bool = None,
        max_security_level: str = None,
        project_id: int = None,
        project_name: str = None,
        sub_type: str = None,
        sum_table_guid: str = None,
        sum_table_name: str = None,
    ):
        # The API call mode. Returned when the asset type is API. Valid values:
        # - 1: synchronous call.
        # - 2: asynchronous call.
        self.api_call_mode = api_call_mode
        # The API group name. Returned when the asset type is API.
        self.api_group_name = api_group_name
        # The API ID. Returned when the asset type is API.
        self.api_id = api_id
        # The API operation type. Returned when the asset type is API. Valid values:
        # - 1: Get.
        # - 2: List.
        # - 3: Create.
        # - 4: Update.
        # - 5: Delete.
        self.api_request_method = api_request_method
        # The asset description.
        self.asset_description = asset_description
        # The asset display name. Returned when the asset type is TABLE, INDEX, or BIZ_INDEX.
        self.asset_display_name = asset_display_name
        # The asset source. For TABLE (physical table), the value is in the format "Dataphin-workspace type-project Chinese name (project English name)". For TABLE (logical table), the value is in the format "Dataphin-workspace type-data domain Chinese name (data domain English name)". For TABLE (data source table), the value is in the format "source system name-data source name-database/schema name". For INDEX (standard modeling metric), the value is the asset source of the associated aggregate table. For INDEX (custom metric), the value is the asset source of the source table. For API, the value is the data service project name. For PAGE, the value is the application system name.
        self.asset_from = asset_from
        # The asset full name. Returned when the asset type is TABLE or INDEX.
        self.asset_full_name = asset_full_name
        # The asset name.
        self.asset_name = asset_name
        # The asset tags.
        self.asset_tags = asset_tags
        # The asset type. Valid values: TABLE (table, including views and materialized views), INDEX (technical metric), BIZ_INDEX (business metric), API, and PAGE (dashboard).
        self.asset_type = asset_type
        # The BI workspace or directory to which the asset belongs. Returned when the asset type is PAGE (dashboard).
        self.bi_catalog = bi_catalog
        # The ID of the business unit to which the asset belongs. Returned when the asset type is TABLE (logical tables only) or INDEX (technical metrics whose source table is a logical table only).
        self.biz_unit_id = biz_unit_id
        # The name of the business unit to which the asset belongs. Returned when the asset type is TABLE (logical tables only) or INDEX (technical metrics whose source table is a logical table only).
        self.biz_unit_name = biz_unit_name
        # The total number of charts. Returned when the asset type is PAGE (dashboard).
        self.chart_count = chart_count
        # The ID of the subject domain to which the asset belongs. Returned when the asset type is TABLE (logical tables only) or INDEX (technical metrics whose source table is a logical table only).
        self.data_cell_id = data_cell_id
        # The name of the subject domain to which the asset belongs. Returned when the asset type is TABLE (logical tables only) or INDEX (technical metrics whose source table is a logical table only).
        self.data_cell_name = data_cell_name
        # The name of the data source to which the asset belongs. Returned when the asset type is TABLE (data source tables only) or INDEX (technical metrics whose source table is a data source table only).
        self.data_source_name = data_source_name
        # The ID of the data source to which the asset belongs. Returned when the asset type is TABLE (data source tables only) or INDEX (technical metrics whose source table is a data source table only).
        self.datasource_id = datasource_id
        # The directories to which the asset belongs, including topic ID, topic name, directory ID, and directory name.
        self.directories = directories
        # The statistical granularity name of the technical metric. Returned when the asset type is INDEX.
        self.granularity = granularity
        # The asset GUID, which serves as the unique identifier of the asset.
        self.guid = guid
        # Indicates whether the asset is deleted.
        self.is_deleted = is_deleted
        # The highest sensitivity level. Returned when the asset type is TABLE.
        self.max_security_level = max_security_level
        # The ID of the project to which the asset belongs. Returned when the asset type is TABLE (physical tables only) or INDEX (technical metrics whose source table is a physical table only).
        self.project_id = project_id
        # The name of the project to which the asset belongs. Returned when the asset type is TABLE (physical tables only) or INDEX (technical metrics whose source table is a physical table only).
        self.project_name = project_name
        # The subtype. Valid values: DIM_NORMAL (common logical dimension table), DIM_ENUM (enumeration logical dimension table), DIM_VIRTUAL (virtual logical dimension table), SUM_BIZ_UNIT (aggregate logical table), FACT_EVENT (event fact logical table), FACT_SNAPSHOT (snapshot fact logical table), DATASOURCE_TABLE (data source table), PHYSICAL_TABLE (physical table), DATASOURCE_VIEW (view - data source view), PHYSICAL_VIEW (physical view), MATERIALIZED_VIEW (materialized view), BIZ_INDEX (business metric), INDEX (technical metric - standard modeling metric), and CUSTOM_INDEX (technical metric - custom metric).
        self.sub_type = sub_type
        # The GUID of the aggregate table to which the asset belongs. Returned when the asset type is INDEX.
        self.sum_table_guid = sum_table_guid
        # The name of the aggregate table to which the asset belongs. Returned when the asset type is INDEX.
        self.sum_table_name = sum_table_name

    def validate(self):
        if self.directories:
            for v1 in self.directories:
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

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.guid is not None:
            result['Guid'] = self.guid

        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted

        if self.max_security_level is not None:
            result['MaxSecurityLevel'] = self.max_security_level

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        if self.sum_table_guid is not None:
            result['SumTableGuid'] = self.sum_table_guid

        if self.sum_table_name is not None:
            result['SumTableName'] = self.sum_table_name

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
                temp_model = main_models.ListCatalogAssetsResponseBodyDataAssetListDirectories()
                self.directories.append(temp_model.from_map(k1))

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')

        if m.get('MaxSecurityLevel') is not None:
            self.max_security_level = m.get('MaxSecurityLevel')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('SumTableGuid') is not None:
            self.sum_table_guid = m.get('SumTableGuid')

        if m.get('SumTableName') is not None:
            self.sum_table_name = m.get('SumTableName')

        return self

class ListCatalogAssetsResponseBodyDataAssetListDirectories(DaraModel):
    def __init__(
        self,
        directory_id: int = None,
        directory_name: str = None,
        topic_id: int = None,
        topic_name: str = None,
    ):
        # The directory ID.
        self.directory_id = directory_id
        # The directory name.
        self.directory_name = directory_name
        # The topic ID.
        self.topic_id = topic_id
        # The topic name.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name

        if self.topic_id is not None:
            result['TopicId'] = self.topic_id

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')

        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self

