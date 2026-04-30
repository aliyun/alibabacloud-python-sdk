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
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
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
        self.asset_list = asset_list
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
        self.api_call_mode = api_call_mode
        self.api_group_name = api_group_name
        self.api_id = api_id
        self.api_request_method = api_request_method
        self.asset_description = asset_description
        self.asset_display_name = asset_display_name
        self.asset_from = asset_from
        self.asset_full_name = asset_full_name
        self.asset_name = asset_name
        self.asset_tags = asset_tags
        self.asset_type = asset_type
        self.bi_catalog = bi_catalog
        self.biz_unit_id = biz_unit_id
        self.biz_unit_name = biz_unit_name
        self.chart_count = chart_count
        self.data_cell_id = data_cell_id
        self.data_cell_name = data_cell_name
        self.data_source_name = data_source_name
        self.datasource_id = datasource_id
        self.directories = directories
        self.granularity = granularity
        self.guid = guid
        self.is_deleted = is_deleted
        self.max_security_level = max_security_level
        self.project_id = project_id
        self.project_name = project_name
        self.sub_type = sub_type
        self.sum_table_guid = sum_table_guid
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
        self.directory_id = directory_id
        self.directory_name = directory_name
        self.topic_id = topic_id
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

