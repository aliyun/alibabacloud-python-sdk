# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class GetSqlConversionResultResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetSqlConversionResultResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The data list returned by the operation. For the structure of each element, see the child parameters.
        self.data = data
        # The error code. An empty string is returned if the call is successful.
        self.err_code = err_code
        # The error message. An empty string is returned if the call is successful.
        self.err_message = err_message
        # The page number, starting from 1.
        self.page_index = page_index
        # The page size, which is the number of entries returned per page.
        self.page_size = page_size
        # The request ID, which is used to locate and troubleshoot issues with this call.
        self.request_id = request_id
        # Indicates whether the call is successful. A value of true indicates success. A value of false indicates failure. If the call fails, check errCode and errMessage for troubleshooting.
        self.success = success
        # The total number of records that meet the query conditions. This value is used for pagination.
        self.total_count = total_count

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
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetSqlConversionResultResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class GetSqlConversionResultResponseBodyData(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        finish_time: str = None,
        script_id: int = None,
        script_name: str = None,
        script_transform_status: str = None,
        sql_result_content: str = None,
        sql_source_content: str = None,
        table_mapping_list: List[main_models.GetSqlConversionResultResponseBodyDataTableMappingList] = None,
    ):
        # The error reason.
        self.error_message = error_message
        # The completion time.
        self.finish_time = finish_time
        # The script ID.
        self.script_id = script_id
        # The script name.
        self.script_name = script_name
        # The script conversion status. In conversion job scenarios: pass for conversion succeeded, turning for converting, and fail for conversion failed. In some scenarios: success for succeeded, failed for failed, and skipped for skipped.
        self.script_transform_status = script_transform_status
        # The converted script content.
        self.sql_result_content = sql_result_content
        # The original script content.
        self.sql_source_content = sql_source_content
        # The table name mapping.
        self.table_mapping_list = table_mapping_list

    def validate(self):
        if self.table_mapping_list:
            for v1 in self.table_mapping_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.finish_time is not None:
            result['finishTime'] = self.finish_time

        if self.script_id is not None:
            result['scriptId'] = self.script_id

        if self.script_name is not None:
            result['scriptName'] = self.script_name

        if self.script_transform_status is not None:
            result['scriptTransformStatus'] = self.script_transform_status

        if self.sql_result_content is not None:
            result['sqlResultContent'] = self.sql_result_content

        if self.sql_source_content is not None:
            result['sqlSourceContent'] = self.sql_source_content

        result['tableMappingList'] = []
        if self.table_mapping_list is not None:
            for k1 in self.table_mapping_list:
                result['tableMappingList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')

        if m.get('scriptId') is not None:
            self.script_id = m.get('scriptId')

        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')

        if m.get('scriptTransformStatus') is not None:
            self.script_transform_status = m.get('scriptTransformStatus')

        if m.get('sqlResultContent') is not None:
            self.sql_result_content = m.get('sqlResultContent')

        if m.get('sqlSourceContent') is not None:
            self.sql_source_content = m.get('sqlSourceContent')

        self.table_mapping_list = []
        if m.get('tableMappingList') is not None:
            for k1 in m.get('tableMappingList'):
                temp_model = main_models.GetSqlConversionResultResponseBodyDataTableMappingList()
                self.table_mapping_list.append(temp_model.from_map(k1))

        return self

class GetSqlConversionResultResponseBodyDataTableMappingList(DaraModel):
    def __init__(
        self,
        id: int = None,
        source_schema: str = None,
        source_table_name: str = None,
        target_table_name: str = None,
        target_type: str = None,
        task_id: int = None,
        tenant_id: str = None,
        uid: str = None,
    ):
        # The primary key.
        self.id = id
        # The source type. Valid values: DB and Schema.
        self.source_schema = source_schema
        # The source table name.
        self.source_table_name = source_table_name
        # The target table name.
        self.target_table_name = target_table_name
        # The target type. Valid values: DB and Schema.
        self.target_type = target_type
        # The SQL conversion task ID.
        self.task_id = task_id
        # The tenant ID.
        self.tenant_id = tenant_id
        # The user ID.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.source_schema is not None:
            result['sourceSchema'] = self.source_schema

        if self.source_table_name is not None:
            result['sourceTableName'] = self.source_table_name

        if self.target_table_name is not None:
            result['targetTableName'] = self.target_table_name

        if self.target_type is not None:
            result['targetType'] = self.target_type

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.uid is not None:
            result['uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('sourceSchema') is not None:
            self.source_schema = m.get('sourceSchema')

        if m.get('sourceTableName') is not None:
            self.source_table_name = m.get('sourceTableName')

        if m.get('targetTableName') is not None:
            self.target_table_name = m.get('targetTableName')

        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('uid') is not None:
            self.uid = m.get('uid')

        return self

