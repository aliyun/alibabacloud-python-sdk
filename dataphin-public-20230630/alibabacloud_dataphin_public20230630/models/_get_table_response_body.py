# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetTableResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTableResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            temp_model = main_models.GetTableResponseBodyData()
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

class GetTableResponseBodyData(DaraModel):
    def __init__(
        self,
        asset_tags: List[str] = None,
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
        instructions: List[main_models.GetTableResponseBodyDataInstructions] = None,
        is_basic_mode: bool = None,
        is_partition_table: bool = None,
        last_ddl_time: str = None,
        last_dml_time: str = None,
        last_query_time: str = None,
        life_cycle: int = None,
        name: str = None,
        node_ids: List[str] = None,
        owner: str = None,
        parent_model_id: str = None,
        project_id: int = None,
        project_name: str = None,
        security_level: int = None,
        security_level_abbreviation: str = None,
        security_level_name: str = None,
        simple_node_infos: List[main_models.GetTableResponseBodyDataSimpleNodeInfos] = None,
        storage_type: str = None,
        stream_table_config: List[main_models.GetTableResponseBodyDataStreamTableConfig] = None,
        table_size_in_bytes: int = None,
        visit_count_30d: int = None,
    ):
        self.asset_tags = asset_tags
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
        self.instructions = instructions
        self.is_basic_mode = is_basic_mode
        self.is_partition_table = is_partition_table
        self.last_ddl_time = last_ddl_time
        self.last_dml_time = last_dml_time
        self.last_query_time = last_query_time
        self.life_cycle = life_cycle
        self.name = name
        self.node_ids = node_ids
        self.owner = owner
        self.parent_model_id = parent_model_id
        self.project_id = project_id
        self.project_name = project_name
        self.security_level = security_level
        self.security_level_abbreviation = security_level_abbreviation
        self.security_level_name = security_level_name
        self.simple_node_infos = simple_node_infos
        self.storage_type = storage_type
        self.stream_table_config = stream_table_config
        self.table_size_in_bytes = table_size_in_bytes
        self.visit_count_30d = visit_count_30d

    def validate(self):
        if self.instructions:
            for v1 in self.instructions:
                 if v1:
                    v1.validate()
        if self.simple_node_infos:
            for v1 in self.simple_node_infos:
                 if v1:
                    v1.validate()
        if self.stream_table_config:
            for v1 in self.stream_table_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_tags is not None:
            result['AssetTags'] = self.asset_tags

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

        result['Instructions'] = []
        if self.instructions is not None:
            for k1 in self.instructions:
                result['Instructions'].append(k1.to_map() if k1 else None)

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

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

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

        result['SimpleNodeInfos'] = []
        if self.simple_node_infos is not None:
            for k1 in self.simple_node_infos:
                result['SimpleNodeInfos'].append(k1.to_map() if k1 else None)

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
        if m.get('AssetTags') is not None:
            self.asset_tags = m.get('AssetTags')

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

        self.instructions = []
        if m.get('Instructions') is not None:
            for k1 in m.get('Instructions'):
                temp_model = main_models.GetTableResponseBodyDataInstructions()
                self.instructions.append(temp_model.from_map(k1))

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

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

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

        self.simple_node_infos = []
        if m.get('SimpleNodeInfos') is not None:
            for k1 in m.get('SimpleNodeInfos'):
                temp_model = main_models.GetTableResponseBodyDataSimpleNodeInfos()
                self.simple_node_infos.append(temp_model.from_map(k1))

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        self.stream_table_config = []
        if m.get('StreamTableConfig') is not None:
            for k1 in m.get('StreamTableConfig'):
                temp_model = main_models.GetTableResponseBodyDataStreamTableConfig()
                self.stream_table_config.append(temp_model.from_map(k1))

        if m.get('TableSizeInBytes') is not None:
            self.table_size_in_bytes = m.get('TableSizeInBytes')

        if m.get('VisitCount30d') is not None:
            self.visit_count_30d = m.get('VisitCount30d')

        return self

class GetTableResponseBodyDataStreamTableConfig(DaraModel):
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

class GetTableResponseBodyDataSimpleNodeInfos(DaraModel):
    def __init__(
        self,
        biz_unit: main_models.GetTableResponseBodyDataSimpleNodeInfosBizUnit = None,
        env: str = None,
        node_id: str = None,
        node_name: str = None,
        node_schedule_type: str = None,
        owners: List[main_models.GetTableResponseBodyDataSimpleNodeInfosOwners] = None,
        project: main_models.GetTableResponseBodyDataSimpleNodeInfosProject = None,
        sub_biz_type: str = None,
    ):
        self.biz_unit = biz_unit
        self.env = env
        self.node_id = node_id
        self.node_name = node_name
        self.node_schedule_type = node_schedule_type
        self.owners = owners
        self.project = project
        self.sub_biz_type = sub_biz_type

    def validate(self):
        if self.biz_unit:
            self.biz_unit.validate()
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
            result['BizUnit'] = self.biz_unit.to_map()

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
            temp_model = main_models.GetTableResponseBodyDataSimpleNodeInfosBizUnit()
            self.biz_unit = temp_model.from_map(m.get('BizUnit'))

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
                temp_model = main_models.GetTableResponseBodyDataSimpleNodeInfosOwners()
                self.owners.append(temp_model.from_map(k1))

        if m.get('Project') is not None:
            temp_model = main_models.GetTableResponseBodyDataSimpleNodeInfosProject()
            self.project = temp_model.from_map(m.get('Project'))

        if m.get('SubBizType') is not None:
            self.sub_biz_type = m.get('SubBizType')

        return self

class GetTableResponseBodyDataSimpleNodeInfosProject(DaraModel):
    def __init__(
        self,
        project_display_name: str = None,
        project_id: str = None,
        project_name: str = None,
    ):
        self.project_display_name = project_display_name
        self.project_id = project_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_display_name is not None:
            result['ProjectDisplayName'] = self.project_display_name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectDisplayName') is not None:
            self.project_display_name = m.get('ProjectDisplayName')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

class GetTableResponseBodyDataSimpleNodeInfosOwners(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        user_id: str = None,
    ):
        self.display_name = display_name
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

class GetTableResponseBodyDataSimpleNodeInfosBizUnit(DaraModel):
    def __init__(
        self,
        biz_unit_display_name: str = None,
        biz_unit_id: str = None,
        biz_unit_name: str = None,
    ):
        self.biz_unit_display_name = biz_unit_display_name
        self.biz_unit_id = biz_unit_id
        self.biz_unit_name = biz_unit_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_unit_display_name is not None:
            result['BizUnitDisplayName'] = self.biz_unit_display_name

        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id

        if self.biz_unit_name is not None:
            result['BizUnitName'] = self.biz_unit_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitDisplayName') is not None:
            self.biz_unit_display_name = m.get('BizUnitDisplayName')

        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('BizUnitName') is not None:
            self.biz_unit_name = m.get('BizUnitName')

        return self

class GetTableResponseBodyDataInstructions(DaraModel):
    def __init__(
        self,
        content: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        owner_id: str = None,
        owner_nick_name: str = None,
        title: str = None,
    ):
        self.content = content
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.owner_id = owner_id
        self.owner_nick_name = owner_nick_name
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.owner_nick_name is not None:
            result['OwnerNickName'] = self.owner_nick_name

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('OwnerNickName') is not None:
            self.owner_nick_name = m.get('OwnerNickName')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

