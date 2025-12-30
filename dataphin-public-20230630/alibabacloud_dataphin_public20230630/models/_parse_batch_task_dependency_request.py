# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ParseBatchTaskDependencyRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        parse_command: main_models.ParseBatchTaskDependencyRequestParseCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.parse_command = parse_command

    def validate(self):
        if self.parse_command:
            self.parse_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.parse_command is not None:
            result['ParseCommand'] = self.parse_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('ParseCommand') is not None:
            temp_model = main_models.ParseBatchTaskDependencyRequestParseCommand()
            self.parse_command = temp_model.from_map(m.get('ParseCommand'))

        return self

class ParseBatchTaskDependencyRequestParseCommand(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_source_catalog: str = None,
        data_source_id: int = None,
        data_source_schema: str = None,
        include_all_input_tables: bool = None,
        need_query_lineages: bool = None,
        operator_type: str = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.code = code
        self.data_source_catalog = data_source_catalog
        self.data_source_id = data_source_id
        self.data_source_schema = data_source_schema
        self.include_all_input_tables = include_all_input_tables
        self.need_query_lineages = need_query_lineages
        # This parameter is required.
        self.operator_type = operator_type
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data_source_catalog is not None:
            result['DataSourceCatalog'] = self.data_source_catalog

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_schema is not None:
            result['DataSourceSchema'] = self.data_source_schema

        if self.include_all_input_tables is not None:
            result['IncludeAllInputTables'] = self.include_all_input_tables

        if self.need_query_lineages is not None:
            result['NeedQueryLineages'] = self.need_query_lineages

        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DataSourceCatalog') is not None:
            self.data_source_catalog = m.get('DataSourceCatalog')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceSchema') is not None:
            self.data_source_schema = m.get('DataSourceSchema')

        if m.get('IncludeAllInputTables') is not None:
            self.include_all_input_tables = m.get('IncludeAllInputTables')

        if m.get('NeedQueryLineages') is not None:
            self.need_query_lineages = m.get('NeedQueryLineages')

        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

