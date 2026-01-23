# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetTableLineagesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        table_lineage_list: List[main_models.GetTableLineagesResponseBodyTableLineageList] = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.table_lineage_list = table_lineage_list

    def validate(self):
        if self.table_lineage_list:
            for v1 in self.table_lineage_list:
                 if v1:
                    v1.validate()

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        result['TableLineageList'] = []
        if self.table_lineage_list is not None:
            for k1 in self.table_lineage_list:
                result['TableLineageList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.table_lineage_list = []
        if m.get('TableLineageList') is not None:
            for k1 in m.get('TableLineageList'):
                temp_model = main_models.GetTableLineagesResponseBodyTableLineageList()
                self.table_lineage_list.append(temp_model.from_map(k1))

        return self

class GetTableLineagesResponseBodyTableLineageList(DaraModel):
    def __init__(
        self,
        input_biz_unit_id: int = None,
        input_data_source_id: int = None,
        input_data_source_type: str = None,
        input_project_id: int = None,
        input_table_deleted: bool = None,
        input_table_env: str = None,
        input_table_guid: str = None,
        input_table_name: str = None,
        node_env: str = None,
        node_id: str = None,
        output_biz_unit_id: int = None,
        output_data_source_id: int = None,
        output_data_source_type: str = None,
        output_project_id: int = None,
        output_table_deleted: bool = None,
        output_table_env: str = None,
        output_table_guid: str = None,
        output_table_name: str = None,
    ):
        self.input_biz_unit_id = input_biz_unit_id
        self.input_data_source_id = input_data_source_id
        self.input_data_source_type = input_data_source_type
        self.input_project_id = input_project_id
        self.input_table_deleted = input_table_deleted
        self.input_table_env = input_table_env
        self.input_table_guid = input_table_guid
        self.input_table_name = input_table_name
        self.node_env = node_env
        self.node_id = node_id
        self.output_biz_unit_id = output_biz_unit_id
        self.output_data_source_id = output_data_source_id
        self.output_data_source_type = output_data_source_type
        self.output_project_id = output_project_id
        self.output_table_deleted = output_table_deleted
        self.output_table_env = output_table_env
        self.output_table_guid = output_table_guid
        self.output_table_name = output_table_name

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

        if self.input_project_id is not None:
            result['InputProjectId'] = self.input_project_id

        if self.input_table_deleted is not None:
            result['InputTableDeleted'] = self.input_table_deleted

        if self.input_table_env is not None:
            result['InputTableEnv'] = self.input_table_env

        if self.input_table_guid is not None:
            result['InputTableGuid'] = self.input_table_guid

        if self.input_table_name is not None:
            result['InputTableName'] = self.input_table_name

        if self.node_env is not None:
            result['NodeEnv'] = self.node_env

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.output_biz_unit_id is not None:
            result['OutputBizUnitId'] = self.output_biz_unit_id

        if self.output_data_source_id is not None:
            result['OutputDataSourceId'] = self.output_data_source_id

        if self.output_data_source_type is not None:
            result['OutputDataSourceType'] = self.output_data_source_type

        if self.output_project_id is not None:
            result['OutputProjectId'] = self.output_project_id

        if self.output_table_deleted is not None:
            result['OutputTableDeleted'] = self.output_table_deleted

        if self.output_table_env is not None:
            result['OutputTableEnv'] = self.output_table_env

        if self.output_table_guid is not None:
            result['OutputTableGuid'] = self.output_table_guid

        if self.output_table_name is not None:
            result['OutputTableName'] = self.output_table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputBizUnitId') is not None:
            self.input_biz_unit_id = m.get('InputBizUnitId')

        if m.get('InputDataSourceId') is not None:
            self.input_data_source_id = m.get('InputDataSourceId')

        if m.get('InputDataSourceType') is not None:
            self.input_data_source_type = m.get('InputDataSourceType')

        if m.get('InputProjectId') is not None:
            self.input_project_id = m.get('InputProjectId')

        if m.get('InputTableDeleted') is not None:
            self.input_table_deleted = m.get('InputTableDeleted')

        if m.get('InputTableEnv') is not None:
            self.input_table_env = m.get('InputTableEnv')

        if m.get('InputTableGuid') is not None:
            self.input_table_guid = m.get('InputTableGuid')

        if m.get('InputTableName') is not None:
            self.input_table_name = m.get('InputTableName')

        if m.get('NodeEnv') is not None:
            self.node_env = m.get('NodeEnv')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OutputBizUnitId') is not None:
            self.output_biz_unit_id = m.get('OutputBizUnitId')

        if m.get('OutputDataSourceId') is not None:
            self.output_data_source_id = m.get('OutputDataSourceId')

        if m.get('OutputDataSourceType') is not None:
            self.output_data_source_type = m.get('OutputDataSourceType')

        if m.get('OutputProjectId') is not None:
            self.output_project_id = m.get('OutputProjectId')

        if m.get('OutputTableDeleted') is not None:
            self.output_table_deleted = m.get('OutputTableDeleted')

        if m.get('OutputTableEnv') is not None:
            self.output_table_env = m.get('OutputTableEnv')

        if m.get('OutputTableGuid') is not None:
            self.output_table_guid = m.get('OutputTableGuid')

        if m.get('OutputTableName') is not None:
            self.output_table_name = m.get('OutputTableName')

        return self

