# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateSecurityIdentifyResultRequest(DaraModel):
    def __init__(
        self,
        create_command: main_models.CreateSecurityIdentifyResultRequestCreateCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.create_command = create_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = main_models.CreateSecurityIdentifyResultRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class CreateSecurityIdentifyResultRequestCreateCommand(DaraModel):
    def __init__(
        self,
        classify_id: int = None,
        conflict_strategy: str = None,
        datasource_env: str = None,
        datasource_name: str = None,
        enable: bool = None,
        field_name: str = None,
        is_datasource_table: bool = None,
        table_catalog: str = None,
        table_name: str = None,
    ):
        # This parameter is required.
        self.classify_id = classify_id
        # This parameter is required.
        self.conflict_strategy = conflict_strategy
        self.datasource_env = datasource_env
        self.datasource_name = datasource_name
        self.enable = enable
        # This parameter is required.
        self.field_name = field_name
        self.is_datasource_table = is_datasource_table
        # This parameter is required.
        self.table_catalog = table_catalog
        # This parameter is required.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classify_id is not None:
            result['ClassifyId'] = self.classify_id

        if self.conflict_strategy is not None:
            result['ConflictStrategy'] = self.conflict_strategy

        if self.datasource_env is not None:
            result['DatasourceEnv'] = self.datasource_env

        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.is_datasource_table is not None:
            result['IsDatasourceTable'] = self.is_datasource_table

        if self.table_catalog is not None:
            result['TableCatalog'] = self.table_catalog

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassifyId') is not None:
            self.classify_id = m.get('ClassifyId')

        if m.get('ConflictStrategy') is not None:
            self.conflict_strategy = m.get('ConflictStrategy')

        if m.get('DatasourceEnv') is not None:
            self.datasource_env = m.get('DatasourceEnv')

        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('IsDatasourceTable') is not None:
            self.is_datasource_table = m.get('IsDatasourceTable')

        if m.get('TableCatalog') is not None:
            self.table_catalog = m.get('TableCatalog')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

