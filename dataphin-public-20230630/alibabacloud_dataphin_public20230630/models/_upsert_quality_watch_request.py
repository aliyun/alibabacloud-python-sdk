# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpsertQualityWatchRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        upsert_command: main_models.UpsertQualityWatchRequestUpsertCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.upsert_command = upsert_command

    def validate(self):
        if self.upsert_command:
            self.upsert_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.upsert_command is not None:
            result['UpsertCommand'] = self.upsert_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('UpsertCommand') is not None:
            temp_model = main_models.UpsertQualityWatchRequestUpsertCommand()
            self.upsert_command = temp_model.from_map(m.get('UpsertCommand'))

        return self

class UpsertQualityWatchRequestUpsertCommand(DaraModel):
    def __init__(
        self,
        data_source_info: main_models.UpsertQualityWatchRequestUpsertCommandDataSourceInfo = None,
        id: int = None,
        index_info: main_models.UpsertQualityWatchRequestUpsertCommandIndexInfo = None,
        quality_owner: str = None,
        table_info: main_models.UpsertQualityWatchRequestUpsertCommandTableInfo = None,
        type: str = None,
    ):
        self.data_source_info = data_source_info
        self.id = id
        self.index_info = index_info
        # This parameter is required.
        self.quality_owner = quality_owner
        self.table_info = table_info
        # This parameter is required.
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
        if self.data_source_info is not None:
            result['DataSourceInfo'] = self.data_source_info.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.index_info is not None:
            result['IndexInfo'] = self.index_info.to_map()

        if self.quality_owner is not None:
            result['QualityOwner'] = self.quality_owner

        if self.table_info is not None:
            result['TableInfo'] = self.table_info.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceInfo') is not None:
            temp_model = main_models.UpsertQualityWatchRequestUpsertCommandDataSourceInfo()
            self.data_source_info = temp_model.from_map(m.get('DataSourceInfo'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IndexInfo') is not None:
            temp_model = main_models.UpsertQualityWatchRequestUpsertCommandIndexInfo()
            self.index_info = temp_model.from_map(m.get('IndexInfo'))

        if m.get('QualityOwner') is not None:
            self.quality_owner = m.get('QualityOwner')

        if m.get('TableInfo') is not None:
            temp_model = main_models.UpsertQualityWatchRequestUpsertCommandTableInfo()
            self.table_info = temp_model.from_map(m.get('TableInfo'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpsertQualityWatchRequestUpsertCommandTableInfo(DaraModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class UpsertQualityWatchRequestUpsertCommandIndexInfo(DaraModel):
    def __init__(
        self,
        biz_unit_id: int = None,
        cell_sum_logic_table_name: str = None,
        compute_type: str = None,
        date_type: str = None,
        description: str = None,
        display_name: str = None,
        granularity_display_name: str = None,
        granularity_id: int = None,
        id: str = None,
        name: str = None,
        project_id: int = None,
        type: str = None,
    ):
        self.biz_unit_id = biz_unit_id
        self.cell_sum_logic_table_name = cell_sum_logic_table_name
        self.compute_type = compute_type
        self.date_type = date_type
        self.description = description
        self.display_name = display_name
        self.granularity_display_name = granularity_display_name
        self.granularity_id = granularity_id
        self.id = id
        self.name = name
        self.project_id = project_id
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

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

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

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpsertQualityWatchRequestUpsertCommandDataSourceInfo(DaraModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

