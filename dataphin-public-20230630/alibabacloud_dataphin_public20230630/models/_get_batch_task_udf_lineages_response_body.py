# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetBatchTaskUdfLineagesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetBatchTaskUdfLineagesResponseBodyData = None,
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
            temp_model = main_models.GetBatchTaskUdfLineagesResponseBodyData()
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

class GetBatchTaskUdfLineagesResponseBodyData(DaraModel):
    def __init__(
        self,
        lineage_group_list: List[main_models.GetBatchTaskUdfLineagesResponseBodyDataLineageGroupList] = None,
    ):
        self.lineage_group_list = lineage_group_list

    def validate(self):
        if self.lineage_group_list:
            for v1 in self.lineage_group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LineageGroupList'] = []
        if self.lineage_group_list is not None:
            for k1 in self.lineage_group_list:
                result['LineageGroupList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lineage_group_list = []
        if m.get('LineageGroupList') is not None:
            for k1 in m.get('LineageGroupList'):
                temp_model = main_models.GetBatchTaskUdfLineagesResponseBodyDataLineageGroupList()
                self.lineage_group_list.append(temp_model.from_map(k1))

        return self

class GetBatchTaskUdfLineagesResponseBodyDataLineageGroupList(DaraModel):
    def __init__(
        self,
        input_lineage_list: List[main_models.GetBatchTaskUdfLineagesResponseBodyDataLineageGroupListInputLineageList] = None,
        output_lineage_list: List[main_models.GetBatchTaskUdfLineagesResponseBodyDataLineageGroupListOutputLineageList] = None,
    ):
        self.input_lineage_list = input_lineage_list
        self.output_lineage_list = output_lineage_list

    def validate(self):
        if self.input_lineage_list:
            for v1 in self.input_lineage_list:
                 if v1:
                    v1.validate()
        if self.output_lineage_list:
            for v1 in self.output_lineage_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InputLineageList'] = []
        if self.input_lineage_list is not None:
            for k1 in self.input_lineage_list:
                result['InputLineageList'].append(k1.to_map() if k1 else None)

        result['OutputLineageList'] = []
        if self.output_lineage_list is not None:
            for k1 in self.output_lineage_list:
                result['OutputLineageList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.input_lineage_list = []
        if m.get('InputLineageList') is not None:
            for k1 in m.get('InputLineageList'):
                temp_model = main_models.GetBatchTaskUdfLineagesResponseBodyDataLineageGroupListInputLineageList()
                self.input_lineage_list.append(temp_model.from_map(k1))

        self.output_lineage_list = []
        if m.get('OutputLineageList') is not None:
            for k1 in m.get('OutputLineageList'):
                temp_model = main_models.GetBatchTaskUdfLineagesResponseBodyDataLineageGroupListOutputLineageList()
                self.output_lineage_list.append(temp_model.from_map(k1))

        return self

class GetBatchTaskUdfLineagesResponseBodyDataLineageGroupListOutputLineageList(DaraModel):
    def __init__(
        self,
        biz_unit_id: str = None,
        biz_unit_name: str = None,
        column_list: List[main_models.GetBatchTaskUdfLineagesResponseBodyDataLineageGroupListOutputLineageListColumnList] = None,
        description: str = None,
        display_name: str = None,
        env: str = None,
        full_table: bool = None,
        guid: str = None,
        name: str = None,
        owner_name: str = None,
        owner_user_id: str = None,
        project_id: str = None,
        project_name: str = None,
        sub_type: str = None,
    ):
        self.biz_unit_id = biz_unit_id
        self.biz_unit_name = biz_unit_name
        self.column_list = column_list
        self.description = description
        self.display_name = display_name
        self.env = env
        self.full_table = full_table
        self.guid = guid
        self.name = name
        self.owner_name = owner_name
        self.owner_user_id = owner_user_id
        self.project_id = project_id
        self.project_name = project_name
        self.sub_type = sub_type

    def validate(self):
        if self.column_list:
            for v1 in self.column_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id

        if self.biz_unit_name is not None:
            result['BizUnitName'] = self.biz_unit_name

        result['ColumnList'] = []
        if self.column_list is not None:
            for k1 in self.column_list:
                result['ColumnList'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.env is not None:
            result['Env'] = self.env

        if self.full_table is not None:
            result['FullTable'] = self.full_table

        if self.guid is not None:
            result['Guid'] = self.guid

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('BizUnitName') is not None:
            self.biz_unit_name = m.get('BizUnitName')

        self.column_list = []
        if m.get('ColumnList') is not None:
            for k1 in m.get('ColumnList'):
                temp_model = main_models.GetBatchTaskUdfLineagesResponseBodyDataLineageGroupListOutputLineageListColumnList()
                self.column_list.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('FullTable') is not None:
            self.full_table = m.get('FullTable')

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        return self

class GetBatchTaskUdfLineagesResponseBodyDataLineageGroupListOutputLineageListColumnList(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        partition_key: bool = None,
        primary_key: bool = None,
    ):
        self.data_type = data_type
        self.description = description
        self.id = id
        self.name = name
        self.partition_key = partition_key
        self.primary_key = primary_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.partition_key is not None:
            result['PartitionKey'] = self.partition_key

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PartitionKey') is not None:
            self.partition_key = m.get('PartitionKey')

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        return self

class GetBatchTaskUdfLineagesResponseBodyDataLineageGroupListInputLineageList(DaraModel):
    def __init__(
        self,
        biz_unit_id: str = None,
        biz_unit_name: str = None,
        column_list: List[main_models.GetBatchTaskUdfLineagesResponseBodyDataLineageGroupListInputLineageListColumnList] = None,
        description: str = None,
        display_name: str = None,
        env: str = None,
        full_table: bool = None,
        guid: str = None,
        name: str = None,
        owner_name: str = None,
        owner_user_id: str = None,
        project_id: str = None,
        project_name: str = None,
        sub_type: str = None,
    ):
        self.biz_unit_id = biz_unit_id
        self.biz_unit_name = biz_unit_name
        self.column_list = column_list
        self.description = description
        self.display_name = display_name
        self.env = env
        self.full_table = full_table
        self.guid = guid
        self.name = name
        self.owner_name = owner_name
        self.owner_user_id = owner_user_id
        self.project_id = project_id
        self.project_name = project_name
        self.sub_type = sub_type

    def validate(self):
        if self.column_list:
            for v1 in self.column_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id

        if self.biz_unit_name is not None:
            result['BizUnitName'] = self.biz_unit_name

        result['ColumnList'] = []
        if self.column_list is not None:
            for k1 in self.column_list:
                result['ColumnList'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.env is not None:
            result['Env'] = self.env

        if self.full_table is not None:
            result['FullTable'] = self.full_table

        if self.guid is not None:
            result['Guid'] = self.guid

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('BizUnitName') is not None:
            self.biz_unit_name = m.get('BizUnitName')

        self.column_list = []
        if m.get('ColumnList') is not None:
            for k1 in m.get('ColumnList'):
                temp_model = main_models.GetBatchTaskUdfLineagesResponseBodyDataLineageGroupListInputLineageListColumnList()
                self.column_list.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('FullTable') is not None:
            self.full_table = m.get('FullTable')

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        return self

class GetBatchTaskUdfLineagesResponseBodyDataLineageGroupListInputLineageListColumnList(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        partition_key: bool = None,
        primary_key: bool = None,
    ):
        self.data_type = data_type
        self.description = description
        self.id = id
        self.name = name
        self.partition_key = partition_key
        self.primary_key = primary_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.partition_key is not None:
            result['PartitionKey'] = self.partition_key

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PartitionKey') is not None:
            self.partition_key = m.get('PartitionKey')

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        return self

