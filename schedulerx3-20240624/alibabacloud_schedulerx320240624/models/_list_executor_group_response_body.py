# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx320240624 import models as main_models
from darabonba.model import DaraModel

class ListExecutorGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListExecutorGroupResponseBodyData = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The total count of data under the current request conditions. This parameter is optional and is not returned by default.
        self.code = code
        # The query results.
        self.data = data
        # The maximum number of entries to return for this request. Default value: 10.
        self.max_results = max_results
        # The position from which the current call returns data. An empty value indicates that all data has been read.
        # 
        # This parameter is required.
        self.message = message
        # The token that specifies the position from which the current call returns data. An empty value indicates that all data has been read. You do not need to specify this parameter for the first query.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request is successful.
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
            temp_model = main_models.ListExecutorGroupResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListExecutorGroupResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: List[main_models.ListExecutorGroupResponseBodyDataRecords] = None,
        total: int = None,
    ):
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # -
        self.records = records
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.ListExecutorGroupResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListExecutorGroupResponseBodyDataRecords(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        auth_type: str = None,
        auto_scale: bool = None,
        cite_list: List[main_models.ListExecutorGroupResponseBodyDataRecordsCiteList] = None,
        cms_workspace_id: str = None,
        current_jobs: int = None,
        description: str = None,
        enable_jobs: int = None,
        integration_type: str = None,
        max_jobs: int = None,
        name: str = None,
        network: str = None,
        protocol: str = None,
        resolved_workers: str = None,
        worker_id: int = None,
        worker_type: str = None,
        workers: str = None,
        xattrs: str = None,
    ):
        # The client key.
        self.api_key = api_key
        # The authentication type.
        self.auth_type = auth_type
        # Specifies whether to enable **automatic start and stop**. Valid values:
        # - true: Enabled. If no tasks are scheduled for a period of time, the agent automatically hibernates. If tasks are scheduled for a period of time, the agent wakes up in advance.
        # - false: Disabled.
        self.auto_scale = auto_scale
        # The list of referenced applications.
        self.cite_list = cite_list
        # The CloudMonitor workspace.
        self.cms_workspace_id = cms_workspace_id
        # The current number of tasks.
        self.current_jobs = current_jobs
        # The description of the executor group.
        self.description = description
        self.enable_jobs = enable_jobs
        # The integration method. Valid values:
        # - manual
        # - acs_sandbox
        # - k8s_service
        self.integration_type = integration_type
        # The maximum number of tasks.
        self.max_jobs = max_jobs
        # The name of the executor group.
        self.name = name
        # The network configuration.
        self.network = network
        # The protocol.
        self.protocol = protocol
        # The list of resolved workers.
        self.resolved_workers = resolved_workers
        # The ID of the executor group.
        self.worker_id = worker_id
        # The executor type.
        self.worker_type = worker_type
        # The list of specified machines in JSON format.
        self.workers = workers
        # The extended parameters.
        self.xattrs = xattrs

    def validate(self):
        if self.cite_list:
            for v1 in self.cite_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.auto_scale is not None:
            result['AutoScale'] = self.auto_scale

        result['CiteList'] = []
        if self.cite_list is not None:
            for k1 in self.cite_list:
                result['CiteList'].append(k1.to_map() if k1 else None)

        if self.cms_workspace_id is not None:
            result['CmsWorkspaceId'] = self.cms_workspace_id

        if self.current_jobs is not None:
            result['CurrentJobs'] = self.current_jobs

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_jobs is not None:
            result['EnableJobs'] = self.enable_jobs

        if self.integration_type is not None:
            result['IntegrationType'] = self.integration_type

        if self.max_jobs is not None:
            result['MaxJobs'] = self.max_jobs

        if self.name is not None:
            result['Name'] = self.name

        if self.network is not None:
            result['Network'] = self.network

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.resolved_workers is not None:
            result['ResolvedWorkers'] = self.resolved_workers

        if self.worker_id is not None:
            result['WorkerId'] = self.worker_id

        if self.worker_type is not None:
            result['WorkerType'] = self.worker_type

        if self.workers is not None:
            result['Workers'] = self.workers

        if self.xattrs is not None:
            result['XAttrs'] = self.xattrs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('AutoScale') is not None:
            self.auto_scale = m.get('AutoScale')

        self.cite_list = []
        if m.get('CiteList') is not None:
            for k1 in m.get('CiteList'):
                temp_model = main_models.ListExecutorGroupResponseBodyDataRecordsCiteList()
                self.cite_list.append(temp_model.from_map(k1))

        if m.get('CmsWorkspaceId') is not None:
            self.cms_workspace_id = m.get('CmsWorkspaceId')

        if m.get('CurrentJobs') is not None:
            self.current_jobs = m.get('CurrentJobs')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableJobs') is not None:
            self.enable_jobs = m.get('EnableJobs')

        if m.get('IntegrationType') is not None:
            self.integration_type = m.get('IntegrationType')

        if m.get('MaxJobs') is not None:
            self.max_jobs = m.get('MaxJobs')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('ResolvedWorkers') is not None:
            self.resolved_workers = m.get('ResolvedWorkers')

        if m.get('WorkerId') is not None:
            self.worker_id = m.get('WorkerId')

        if m.get('WorkerType') is not None:
            self.worker_type = m.get('WorkerType')

        if m.get('Workers') is not None:
            self.workers = m.get('Workers')

        if m.get('XAttrs') is not None:
            self.xattrs = m.get('XAttrs')

        return self

class ListExecutorGroupResponseBodyDataRecordsCiteList(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        description: str = None,
    ):
        # The name of the application.
        self.app_name = app_name
        # The description of the application.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

