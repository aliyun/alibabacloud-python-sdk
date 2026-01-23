# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetQualityWatchResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        quality_watch_info: main_models.GetQualityWatchResponseBodyQualityWatchInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.quality_watch_info = quality_watch_info
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.quality_watch_info:
            self.quality_watch_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.quality_watch_info is not None:
            result['QualityWatchInfo'] = self.quality_watch_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('QualityWatchInfo') is not None:
            temp_model = main_models.GetQualityWatchResponseBodyQualityWatchInfo()
            self.quality_watch_info = temp_model.from_map(m.get('QualityWatchInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetQualityWatchResponseBodyQualityWatchInfo(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        creator: str = None,
        creator_name: str = None,
        data_source_info: main_models.GetQualityWatchResponseBodyQualityWatchInfoDataSourceInfo = None,
        enabled_rule_count: int = None,
        id: int = None,
        index_info: main_models.GetQualityWatchResponseBodyQualityWatchInfoIndexInfo = None,
        latest_watch_task_id: int = None,
        latest_watch_task_status: str = None,
        modifier: str = None,
        modify_time: str = None,
        name: str = None,
        quality_owner: str = None,
        quality_owner_name: str = None,
        rule_count: int = None,
        status: str = None,
        table_info: main_models.GetQualityWatchResponseBodyQualityWatchInfoTableInfo = None,
        type: str = None,
    ):
        self.create_time = create_time
        self.creator = creator
        self.creator_name = creator_name
        self.data_source_info = data_source_info
        self.enabled_rule_count = enabled_rule_count
        self.id = id
        self.index_info = index_info
        self.latest_watch_task_id = latest_watch_task_id
        self.latest_watch_task_status = latest_watch_task_status
        self.modifier = modifier
        self.modify_time = modify_time
        self.name = name
        self.quality_owner = quality_owner
        self.quality_owner_name = quality_owner_name
        self.rule_count = rule_count
        self.status = status
        self.table_info = table_info
        self.type = type

    def validate(self):
        if self.data_source_info:
            self.data_source_info.validate()
        if self.index_info:
            self.index_info.validate()
        if self.table_info:
            self.table_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.data_source_info is not None:
            result['DataSourceInfo'] = self.data_source_info.to_map()

        if self.enabled_rule_count is not None:
            result['EnabledRuleCount'] = self.enabled_rule_count

        if self.id is not None:
            result['Id'] = self.id

        if self.index_info is not None:
            result['IndexInfo'] = self.index_info.to_map()

        if self.latest_watch_task_id is not None:
            result['LatestWatchTaskId'] = self.latest_watch_task_id

        if self.latest_watch_task_status is not None:
            result['LatestWatchTaskStatus'] = self.latest_watch_task_status

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.quality_owner is not None:
            result['QualityOwner'] = self.quality_owner

        if self.quality_owner_name is not None:
            result['QualityOwnerName'] = self.quality_owner_name

        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count

        if self.status is not None:
            result['Status'] = self.status

        if self.table_info is not None:
            result['TableInfo'] = self.table_info.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('DataSourceInfo') is not None:
            temp_model = main_models.GetQualityWatchResponseBodyQualityWatchInfoDataSourceInfo()
            self.data_source_info = temp_model.from_map(m.get('DataSourceInfo'))

        if m.get('EnabledRuleCount') is not None:
            self.enabled_rule_count = m.get('EnabledRuleCount')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IndexInfo') is not None:
            temp_model = main_models.GetQualityWatchResponseBodyQualityWatchInfoIndexInfo()
            self.index_info = temp_model.from_map(m.get('IndexInfo'))

        if m.get('LatestWatchTaskId') is not None:
            self.latest_watch_task_id = m.get('LatestWatchTaskId')

        if m.get('LatestWatchTaskStatus') is not None:
            self.latest_watch_task_status = m.get('LatestWatchTaskStatus')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('QualityOwner') is not None:
            self.quality_owner = m.get('QualityOwner')

        if m.get('QualityOwnerName') is not None:
            self.quality_owner_name = m.get('QualityOwnerName')

        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TableInfo') is not None:
            temp_model = main_models.GetQualityWatchResponseBodyQualityWatchInfoTableInfo()
            self.table_info = temp_model.from_map(m.get('TableInfo'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetQualityWatchResponseBodyQualityWatchInfoTableInfo(DaraModel):
    def __init__(
        self,
        biz_unit_id: int = None,
        biz_unit_name: str = None,
        catalog: str = None,
        data_source_id: str = None,
        data_source_type: str = None,
        description: str = None,
        env: str = None,
        id: str = None,
        is_partition_table: bool = None,
        name: str = None,
        owner: str = None,
        owner_name: str = None,
        project_id: int = None,
        project_name: str = None,
        type: str = None,
    ):
        self.biz_unit_id = biz_unit_id
        self.biz_unit_name = biz_unit_name
        self.catalog = catalog
        self.data_source_id = data_source_id
        self.data_source_type = data_source_type
        self.description = description
        self.env = env
        self.id = id
        self.is_partition_table = is_partition_table
        self.name = name
        self.owner = owner
        self.owner_name = owner_name
        self.project_id = project_id
        self.project_name = project_name
        self.type = type

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

        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.description is not None:
            result['Description'] = self.description

        if self.env is not None:
            result['Env'] = self.env

        if self.id is not None:
            result['Id'] = self.id

        if self.is_partition_table is not None:
            result['IsPartitionTable'] = self.is_partition_table

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('BizUnitName') is not None:
            self.biz_unit_name = m.get('BizUnitName')

        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsPartitionTable') is not None:
            self.is_partition_table = m.get('IsPartitionTable')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetQualityWatchResponseBodyQualityWatchInfoIndexInfo(DaraModel):
    def __init__(
        self,
        biz_unit_id: int = None,
        biz_unit_name: str = None,
        catalog: str = None,
        cell_sum_logic_table_name: str = None,
        compute_type: str = None,
        date_type: str = None,
        description: str = None,
        display_name: str = None,
        granularity_display_name: str = None,
        granularity_id: int = None,
        guid: str = None,
        id: str = None,
        name: str = None,
        owner: str = None,
        owner_name: str = None,
        project_id: int = None,
        project_name: str = None,
        type: str = None,
    ):
        self.biz_unit_id = biz_unit_id
        self.biz_unit_name = biz_unit_name
        self.catalog = catalog
        self.cell_sum_logic_table_name = cell_sum_logic_table_name
        self.compute_type = compute_type
        self.date_type = date_type
        self.description = description
        self.display_name = display_name
        self.granularity_display_name = granularity_display_name
        self.granularity_id = granularity_id
        self.guid = guid
        self.id = id
        self.name = name
        self.owner = owner
        self.owner_name = owner_name
        self.project_id = project_id
        self.project_name = project_name
        self.type = type

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

        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.cell_sum_logic_table_name is not None:
            result['CellSumLogicTableName'] = self.cell_sum_logic_table_name

        if self.compute_type is not None:
            result['ComputeType'] = self.compute_type

        if self.date_type is not None:
            result['DateType'] = self.date_type

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.granularity_display_name is not None:
            result['GranularityDisplayName'] = self.granularity_display_name

        if self.granularity_id is not None:
            result['GranularityId'] = self.granularity_id

        if self.guid is not None:
            result['Guid'] = self.guid

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('BizUnitName') is not None:
            self.biz_unit_name = m.get('BizUnitName')

        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('CellSumLogicTableName') is not None:
            self.cell_sum_logic_table_name = m.get('CellSumLogicTableName')

        if m.get('ComputeType') is not None:
            self.compute_type = m.get('ComputeType')

        if m.get('DateType') is not None:
            self.date_type = m.get('DateType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('GranularityDisplayName') is not None:
            self.granularity_display_name = m.get('GranularityDisplayName')

        if m.get('GranularityId') is not None:
            self.granularity_id = m.get('GranularityId')

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetQualityWatchResponseBodyQualityWatchInfoDataSourceInfo(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        creator: str = None,
        creator_name: str = None,
        env: str = None,
        id: str = None,
        modify_time: str = None,
        name: str = None,
        owner: str = None,
        owner_name: str = None,
        type: str = None,
    ):
        self.create_time = create_time
        self.creator = creator
        self.creator_name = creator_name
        self.env = env
        self.id = id
        self.modify_time = modify_time
        self.name = name
        self.owner = owner
        self.owner_name = owner_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.env is not None:
            result['Env'] = self.env

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

