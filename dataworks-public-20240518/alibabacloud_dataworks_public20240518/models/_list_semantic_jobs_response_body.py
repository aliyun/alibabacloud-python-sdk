# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListSemanticJobsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListSemanticJobsResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The paginated result of task definitions. Use the Name field of a list item to run, delete, query run records, or download results. Use the ProjectId field to query run details, view logs, or stop a run.
        self.data = data
        # The request ID. Used for locating logs and troubleshooting issues.
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
            temp_model = main_models.ListSemanticJobsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListSemanticJobsResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        semantic_jobs: List[main_models.ListSemanticJobsResponseBodyDataSemanticJobs] = None,
        total_count: int = None,
    ):
        # The page number of the returned page, starting from 1.
        self.page_number = page_number
        # The number of task definitions per page in the current response.
        self.page_size = page_size
        # The list of task definitions.
        self.semantic_jobs = semantic_jobs
        # The total number of task definitions that meet the conditions within the current tenant.
        self.total_count = total_count

    def validate(self):
        if self.semantic_jobs:
            for v1 in self.semantic_jobs:
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

        result['SemanticJobs'] = []
        if self.semantic_jobs is not None:
            for k1 in self.semantic_jobs:
                result['SemanticJobs'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.semantic_jobs = []
        if m.get('SemanticJobs') is not None:
            for k1 in m.get('SemanticJobs'):
                temp_model = main_models.ListSemanticJobsResponseBodyDataSemanticJobs()
                self.semantic_jobs.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSemanticJobsResponseBodyDataSemanticJobs(DaraModel):
    def __init__(
        self,
        creator: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        name: str = None,
        project_id: int = None,
        reference_file_ids: List[str] = None,
        reference_file_uris: List[str] = None,
        resource_group_id: str = None,
        source: Dict[str, Any] = None,
        type: str = None,
        user_id: str = None,
    ):
        # The user ID of the semantic task creator.
        self.creator = creator
        # The creation time, expressed as a UNIX timestamp in milliseconds.
        self.gmt_create = gmt_create
        # The last modification time, expressed as a UNIX timestamp in milliseconds.
        self.gmt_modified = gmt_modified
        # The internal unique ID of the task definition.
        self.id = id
        # The task name. Used for RunSemanticJob, DeleteSemanticJob, ListSemanticJobRuns, and DownloadSemanticResults.
        self.name = name
        # The workspace ID to which the task belongs. Used for GetSemanticJobDetail, GetSemanticJobLog, and KillSemanticJob.
        self.project_id = project_id
        # The list of uploaded file IDs associated with the task.
        self.reference_file_ids = reference_file_ids
        # The list of external reference file URIs associated with the task.
        self.reference_file_uris = reference_file_uris
        # The ID of the resource group used to run this task.
        self.resource_group_id = resource_group_id
        # The input datasource config saved in the node. This configuration determines the analysis scope at runtime.
        self.source = source
        # The Source.type data source type saved in the task.
        self.type = type
        # The user ID of the semantic task creator.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.reference_file_ids is not None:
            result['ReferenceFileIds'] = self.reference_file_ids

        if self.reference_file_uris is not None:
            result['ReferenceFileUris'] = self.reference_file_uris

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source is not None:
            result['Source'] = self.source

        if self.type is not None:
            result['Type'] = self.type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ReferenceFileIds') is not None:
            self.reference_file_ids = m.get('ReferenceFileIds')

        if m.get('ReferenceFileUris') is not None:
            self.reference_file_uris = m.get('ReferenceFileUris')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

