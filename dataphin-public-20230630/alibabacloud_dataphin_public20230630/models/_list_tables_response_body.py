# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListTablesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListTablesResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

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

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

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

        if m.get('PageResult') is not None:
            temp_model = main_models.ListTablesResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListTablesResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        table_list: List[main_models.ListTablesResponseBodyPageResultTableList] = None,
        total_count: int = None,
    ):
        self.table_list = table_list
        self.total_count = total_count

    def validate(self):
        if self.table_list:
            for v1 in self.table_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TableList'] = []
        if self.table_list is not None:
            for k1 in self.table_list:
                result['TableList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.table_list = []
        if m.get('TableList') is not None:
            for k1 in m.get('TableList'):
                temp_model = main_models.ListTablesResponseBodyPageResultTableList()
                self.table_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTablesResponseBodyPageResultTableList(DaraModel):
    def __init__(
        self,
        asset_tag_list: List[str] = None,
        biz_unit_id: int = None,
        biz_unit_name: str = None,
        comment: str = None,
        create_time: str = None,
        creator: str = None,
        data_domain_id: int = None,
        data_domain_name: str = None,
        data_source_id: int = None,
        display_name: str = None,
        env: str = None,
        file_id: str = None,
        guid: str = None,
        is_basic_mode: bool = None,
        is_partition_table: bool = None,
        last_ddl_time: str = None,
        last_dml_time: str = None,
        last_query_time: str = None,
        life_cycle: int = None,
        name: str = None,
        owner: str = None,
        parent_model_id: str = None,
        project_id: int = None,
        project_name: str = None,
        security_level: int = None,
        security_level_abbreviation: str = None,
        security_level_name: str = None,
        storage_type: str = None,
        stream_table_config: List[main_models.ListTablesResponseBodyPageResultTableListStreamTableConfig] = None,
        table_size_in_bytes: int = None,
        visit_count_30d: int = None,
    ):
        self.asset_tag_list = asset_tag_list
        self.biz_unit_id = biz_unit_id
        self.biz_unit_name = biz_unit_name
        self.comment = comment
        self.create_time = create_time
        self.creator = creator
        self.data_domain_id = data_domain_id
        self.data_domain_name = data_domain_name
        self.data_source_id = data_source_id
        self.display_name = display_name
        self.env = env
        self.file_id = file_id
        self.guid = guid
        self.is_basic_mode = is_basic_mode
        self.is_partition_table = is_partition_table
        self.last_ddl_time = last_ddl_time
        self.last_dml_time = last_dml_time
        self.last_query_time = last_query_time
        self.life_cycle = life_cycle
        self.name = name
        self.owner = owner
        self.parent_model_id = parent_model_id
        self.project_id = project_id
        self.project_name = project_name
        self.security_level = security_level
        self.security_level_abbreviation = security_level_abbreviation
        self.security_level_name = security_level_name
        self.storage_type = storage_type
        self.stream_table_config = stream_table_config
        self.table_size_in_bytes = table_size_in_bytes
        self.visit_count_30d = visit_count_30d

    def validate(self):
        if self.stream_table_config:
            for v1 in self.stream_table_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_tag_list is not None:
            result['AssetTagList'] = self.asset_tag_list

        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id

        if self.biz_unit_name is not None:
            result['BizUnitName'] = self.biz_unit_name

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.data_domain_id is not None:
            result['DataDomainId'] = self.data_domain_id

        if self.data_domain_name is not None:
            result['DataDomainName'] = self.data_domain_name

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.env is not None:
            result['Env'] = self.env

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.guid is not None:
            result['Guid'] = self.guid

        if self.is_basic_mode is not None:
            result['IsBasicMode'] = self.is_basic_mode

        if self.is_partition_table is not None:
            result['IsPartitionTable'] = self.is_partition_table

        if self.last_ddl_time is not None:
            result['LastDdlTime'] = self.last_ddl_time

        if self.last_dml_time is not None:
            result['LastDmlTime'] = self.last_dml_time

        if self.last_query_time is not None:
            result['LastQueryTime'] = self.last_query_time

        if self.life_cycle is not None:
            result['LifeCycle'] = self.life_cycle

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.parent_model_id is not None:
            result['ParentModelId'] = self.parent_model_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level

        if self.security_level_abbreviation is not None:
            result['SecurityLevelAbbreviation'] = self.security_level_abbreviation

        if self.security_level_name is not None:
            result['SecurityLevelName'] = self.security_level_name

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        result['StreamTableConfig'] = []
        if self.stream_table_config is not None:
            for k1 in self.stream_table_config:
                result['StreamTableConfig'].append(k1.to_map() if k1 else None)

        if self.table_size_in_bytes is not None:
            result['TableSizeInBytes'] = self.table_size_in_bytes

        if self.visit_count_30d is not None:
            result['VisitCount30d'] = self.visit_count_30d

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetTagList') is not None:
            self.asset_tag_list = m.get('AssetTagList')

        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('BizUnitName') is not None:
            self.biz_unit_name = m.get('BizUnitName')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DataDomainId') is not None:
            self.data_domain_id = m.get('DataDomainId')

        if m.get('DataDomainName') is not None:
            self.data_domain_name = m.get('DataDomainName')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        if m.get('IsBasicMode') is not None:
            self.is_basic_mode = m.get('IsBasicMode')

        if m.get('IsPartitionTable') is not None:
            self.is_partition_table = m.get('IsPartitionTable')

        if m.get('LastDdlTime') is not None:
            self.last_ddl_time = m.get('LastDdlTime')

        if m.get('LastDmlTime') is not None:
            self.last_dml_time = m.get('LastDmlTime')

        if m.get('LastQueryTime') is not None:
            self.last_query_time = m.get('LastQueryTime')

        if m.get('LifeCycle') is not None:
            self.life_cycle = m.get('LifeCycle')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ParentModelId') is not None:
            self.parent_model_id = m.get('ParentModelId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')

        if m.get('SecurityLevelAbbreviation') is not None:
            self.security_level_abbreviation = m.get('SecurityLevelAbbreviation')

        if m.get('SecurityLevelName') is not None:
            self.security_level_name = m.get('SecurityLevelName')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        self.stream_table_config = []
        if m.get('StreamTableConfig') is not None:
            for k1 in m.get('StreamTableConfig'):
                temp_model = main_models.ListTablesResponseBodyPageResultTableListStreamTableConfig()
                self.stream_table_config.append(temp_model.from_map(k1))

        if m.get('TableSizeInBytes') is not None:
            self.table_size_in_bytes = m.get('TableSizeInBytes')

        if m.get('VisitCount30d') is not None:
            self.visit_count_30d = m.get('VisitCount30d')

        return self

class ListTablesResponseBodyPageResultTableListStreamTableConfig(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

