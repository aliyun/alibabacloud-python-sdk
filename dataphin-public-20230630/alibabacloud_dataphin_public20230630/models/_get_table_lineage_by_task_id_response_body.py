# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetTableLineageByTaskIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetTableLineageByTaskIdResponseBodyData] = None,
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
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetTableLineageByTaskIdResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetTableLineageByTaskIdResponseBodyData(DaraModel):
    def __init__(
        self,
        input_biz_unit_id: int = None,
        input_data_source_id: int = None,
        input_data_source_type: str = None,
        input_db_type: str = None,
        input_env: str = None,
        input_project_id: int = None,
        input_table_deleted: bool = None,
        input_table_id: str = None,
        input_table_name: str = None,
        input_table_type: str = None,
        output_biz_unit_id: int = None,
        output_data_source_id: int = None,
        output_data_source_type: str = None,
        output_db_type: str = None,
        output_env: str = None,
        output_project_id: int = None,
        output_table_deleted: bool = None,
        output_table_id: str = None,
        output_table_name: str = None,
        output_table_type: str = None,
        task_env: str = None,
        task_id: str = None,
        tenant_id: int = None,
    ):
        self.input_biz_unit_id = input_biz_unit_id
        self.input_data_source_id = input_data_source_id
        self.input_data_source_type = input_data_source_type
        self.input_db_type = input_db_type
        self.input_env = input_env
        self.input_project_id = input_project_id
        self.input_table_deleted = input_table_deleted
        self.input_table_id = input_table_id
        self.input_table_name = input_table_name
        self.input_table_type = input_table_type
        self.output_biz_unit_id = output_biz_unit_id
        self.output_data_source_id = output_data_source_id
        self.output_data_source_type = output_data_source_type
        self.output_db_type = output_db_type
        self.output_env = output_env
        self.output_project_id = output_project_id
        self.output_table_deleted = output_table_deleted
        self.output_table_id = output_table_id
        self.output_table_name = output_table_name
        self.output_table_type = output_table_type
        self.task_env = task_env
        self.task_id = task_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_biz_unit_id is not None:
            result['InputBizUnitId'] = self.input_biz_unit_id

        if self.input_data_source_id is not None:
            result['InputDataSourceId'] = self.input_data_source_id

        if self.input_data_source_type is not None:
            result['InputDataSourceType'] = self.input_data_source_type

        if self.input_db_type is not None:
            result['InputDbType'] = self.input_db_type

        if self.input_env is not None:
            result['InputEnv'] = self.input_env

        if self.input_project_id is not None:
            result['InputProjectId'] = self.input_project_id

        if self.input_table_deleted is not None:
            result['InputTableDeleted'] = self.input_table_deleted

        if self.input_table_id is not None:
            result['InputTableId'] = self.input_table_id

        if self.input_table_name is not None:
            result['InputTableName'] = self.input_table_name

        if self.input_table_type is not None:
            result['InputTableType'] = self.input_table_type

        if self.output_biz_unit_id is not None:
            result['OutputBizUnitId'] = self.output_biz_unit_id

        if self.output_data_source_id is not None:
            result['OutputDataSourceId'] = self.output_data_source_id

        if self.output_data_source_type is not None:
            result['OutputDataSourceType'] = self.output_data_source_type

        if self.output_db_type is not None:
            result['OutputDbType'] = self.output_db_type

        if self.output_env is not None:
            result['OutputEnv'] = self.output_env

        if self.output_project_id is not None:
            result['OutputProjectId'] = self.output_project_id

        if self.output_table_deleted is not None:
            result['OutputTableDeleted'] = self.output_table_deleted

        if self.output_table_id is not None:
            result['OutputTableId'] = self.output_table_id

        if self.output_table_name is not None:
            result['OutputTableName'] = self.output_table_name

        if self.output_table_type is not None:
            result['OutputTableType'] = self.output_table_type

        if self.task_env is not None:
            result['TaskEnv'] = self.task_env

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputBizUnitId') is not None:
            self.input_biz_unit_id = m.get('InputBizUnitId')

        if m.get('InputDataSourceId') is not None:
            self.input_data_source_id = m.get('InputDataSourceId')

        if m.get('InputDataSourceType') is not None:
            self.input_data_source_type = m.get('InputDataSourceType')

        if m.get('InputDbType') is not None:
            self.input_db_type = m.get('InputDbType')

        if m.get('InputEnv') is not None:
            self.input_env = m.get('InputEnv')

        if m.get('InputProjectId') is not None:
            self.input_project_id = m.get('InputProjectId')

        if m.get('InputTableDeleted') is not None:
            self.input_table_deleted = m.get('InputTableDeleted')

        if m.get('InputTableId') is not None:
            self.input_table_id = m.get('InputTableId')

        if m.get('InputTableName') is not None:
            self.input_table_name = m.get('InputTableName')

        if m.get('InputTableType') is not None:
            self.input_table_type = m.get('InputTableType')

        if m.get('OutputBizUnitId') is not None:
            self.output_biz_unit_id = m.get('OutputBizUnitId')

        if m.get('OutputDataSourceId') is not None:
            self.output_data_source_id = m.get('OutputDataSourceId')

        if m.get('OutputDataSourceType') is not None:
            self.output_data_source_type = m.get('OutputDataSourceType')

        if m.get('OutputDbType') is not None:
            self.output_db_type = m.get('OutputDbType')

        if m.get('OutputEnv') is not None:
            self.output_env = m.get('OutputEnv')

        if m.get('OutputProjectId') is not None:
            self.output_project_id = m.get('OutputProjectId')

        if m.get('OutputTableDeleted') is not None:
            self.output_table_deleted = m.get('OutputTableDeleted')

        if m.get('OutputTableId') is not None:
            self.output_table_id = m.get('OutputTableId')

        if m.get('OutputTableName') is not None:
            self.output_table_name = m.get('OutputTableName')

        if m.get('OutputTableType') is not None:
            self.output_table_type = m.get('OutputTableType')

        if m.get('TaskEnv') is not None:
            self.task_env = m.get('TaskEnv')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

