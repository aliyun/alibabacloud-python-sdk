# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetSemanticJobDetailResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetSemanticJobDetailResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The job details returned by the executor. Used to determine the run status and view the actual runtime configuration.
        self.data = data
        # The request ID. Used for locating logs and troubleshooting issues.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetSemanticJobDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSemanticJobDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        advance_settings: Dict[str, Any] = None,
        code_parameters: str = None,
        current_sql_index: int = None,
        customer_name: str = None,
        datasource: str = None,
        env: str = None,
        exec_types: List[int] = None,
        executor_job_id: str = None,
        file_type: int = None,
        project_id: int = None,
        resource_group_id: str = None,
        resource_urls: List[Dict[str, Any]] = None,
        statuses: List[int] = None,
    ):
        # The advanced runtime settings returned by the executor.
        self.advance_settings = advance_settings
        # The code parameter information returned by the executor. Used for troubleshooting the runtime configuration of this run.
        self.code_parameters = code_parameters
        # The index of the SQL fragment currently being processed by the executor.
        self.current_sql_index = current_sql_index
        # The customer identifier of the executor job.
        self.customer_name = customer_name
        # The data source identifier used by the executor job.
        self.datasource = datasource
        # The runtime environment identifier returned by the executor.
        self.env = env
        # The list of execution type codes returned by the executor.
        self.exec_types = exec_types
        # The executor job ID.
        self.executor_job_id = executor_job_id
        # The node type code of the executor. Semantic jobs use Shell node code 6.
        self.file_type = file_type
        # The DataWorks workspace ID associated with the executor job.
        self.project_id = project_id
        # The ID of the resource group that actually executed the job.
        self.resource_group_id = resource_group_id
        # The list of resource URLs associated with the executor job.
        self.resource_urls = resource_urls
        # The list of status codes returned by the executor. Used to determine the current or final status of the job.
        self.statuses = statuses

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advance_settings is not None:
            result['AdvanceSettings'] = self.advance_settings

        if self.code_parameters is not None:
            result['CodeParameters'] = self.code_parameters

        if self.current_sql_index is not None:
            result['CurrentSqlIndex'] = self.current_sql_index

        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name

        if self.datasource is not None:
            result['Datasource'] = self.datasource

        if self.env is not None:
            result['Env'] = self.env

        if self.exec_types is not None:
            result['ExecTypes'] = self.exec_types

        if self.executor_job_id is not None:
            result['ExecutorJobId'] = self.executor_job_id

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_urls is not None:
            result['ResourceUrls'] = self.resource_urls

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvanceSettings') is not None:
            self.advance_settings = m.get('AdvanceSettings')

        if m.get('CodeParameters') is not None:
            self.code_parameters = m.get('CodeParameters')

        if m.get('CurrentSqlIndex') is not None:
            self.current_sql_index = m.get('CurrentSqlIndex')

        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')

        if m.get('Datasource') is not None:
            self.datasource = m.get('Datasource')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('ExecTypes') is not None:
            self.exec_types = m.get('ExecTypes')

        if m.get('ExecutorJobId') is not None:
            self.executor_job_id = m.get('ExecutorJobId')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceUrls') is not None:
            self.resource_urls = m.get('ResourceUrls')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        return self

