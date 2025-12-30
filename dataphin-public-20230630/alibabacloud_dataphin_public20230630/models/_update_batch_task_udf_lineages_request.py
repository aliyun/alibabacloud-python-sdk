# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateBatchTaskUdfLineagesRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: main_models.UpdateBatchTaskUdfLineagesRequestUpdateCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.update_command = update_command

    def validate(self):
        if self.update_command:
            self.update_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.update_command is not None:
            result['UpdateCommand'] = self.update_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('UpdateCommand') is not None:
            temp_model = main_models.UpdateBatchTaskUdfLineagesRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateBatchTaskUdfLineagesRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        file_id: int = None,
        lineage_group_list: List[main_models.UpdateBatchTaskUdfLineagesRequestUpdateCommandLineageGroupList] = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.file_id = file_id
        # This parameter is required.
        self.lineage_group_list = lineage_group_list
        # This parameter is required.
        self.project_id = project_id

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
        if self.file_id is not None:
            result['FileId'] = self.file_id

        result['LineageGroupList'] = []
        if self.lineage_group_list is not None:
            for k1 in self.lineage_group_list:
                result['LineageGroupList'].append(k1.to_map() if k1 else None)

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        self.lineage_group_list = []
        if m.get('LineageGroupList') is not None:
            for k1 in m.get('LineageGroupList'):
                temp_model = main_models.UpdateBatchTaskUdfLineagesRequestUpdateCommandLineageGroupList()
                self.lineage_group_list.append(temp_model.from_map(k1))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class UpdateBatchTaskUdfLineagesRequestUpdateCommandLineageGroupList(DaraModel):
    def __init__(
        self,
        input_lineage_list: List[main_models.UpdateBatchTaskUdfLineagesRequestUpdateCommandLineageGroupListInputLineageList] = None,
        output_lineage_list: List[main_models.UpdateBatchTaskUdfLineagesRequestUpdateCommandLineageGroupListOutputLineageList] = None,
    ):
        # This parameter is required.
        self.input_lineage_list = input_lineage_list
        # This parameter is required.
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
                temp_model = main_models.UpdateBatchTaskUdfLineagesRequestUpdateCommandLineageGroupListInputLineageList()
                self.input_lineage_list.append(temp_model.from_map(k1))

        self.output_lineage_list = []
        if m.get('OutputLineageList') is not None:
            for k1 in m.get('OutputLineageList'):
                temp_model = main_models.UpdateBatchTaskUdfLineagesRequestUpdateCommandLineageGroupListOutputLineageList()
                self.output_lineage_list.append(temp_model.from_map(k1))

        return self

class UpdateBatchTaskUdfLineagesRequestUpdateCommandLineageGroupListOutputLineageList(DaraModel):
    def __init__(
        self,
        column_list: List[str] = None,
        env: str = None,
        full_table: bool = None,
        name: str = None,
    ):
        # This parameter is required.
        self.column_list = column_list
        # This parameter is required.
        self.env = env
        # This parameter is required.
        self.full_table = full_table
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_list is not None:
            result['ColumnList'] = self.column_list

        if self.env is not None:
            result['Env'] = self.env

        if self.full_table is not None:
            result['FullTable'] = self.full_table

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnList') is not None:
            self.column_list = m.get('ColumnList')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('FullTable') is not None:
            self.full_table = m.get('FullTable')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class UpdateBatchTaskUdfLineagesRequestUpdateCommandLineageGroupListInputLineageList(DaraModel):
    def __init__(
        self,
        column_list: List[str] = None,
        env: str = None,
        full_table: bool = None,
        name: str = None,
    ):
        # This parameter is required.
        self.column_list = column_list
        # This parameter is required.
        self.env = env
        # This parameter is required.
        self.full_table = full_table
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_list is not None:
            result['ColumnList'] = self.column_list

        if self.env is not None:
            result['Env'] = self.env

        if self.full_table is not None:
            result['FullTable'] = self.full_table

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnList') is not None:
            self.column_list = m.get('ColumnList')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('FullTable') is not None:
            self.full_table = m.get('FullTable')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

