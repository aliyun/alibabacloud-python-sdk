# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateSemanticJobResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateSemanticJobResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The saved semantic task definition. Use Data.Name to call RunSemanticJob, DeleteSemanticJob, ListSemanticJobRuns, and DownloadSemanticResults.
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
            temp_model = main_models.CreateSemanticJobResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateSemanticJobResponseBodyData(DaraModel):
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
        # The task creator identifier, equivalent to UserId, used to display creation ownership.
        self.creator = creator
        # The creation time of the task definition, as a UNIX timestamp in milliseconds.
        self.gmt_create = gmt_create
        # The last modification time of the task definition, as a UNIX timestamp in milliseconds.
        self.gmt_modified = gmt_modified
        # The internal unique ID of the task definition, which identifies the task created by this call.
        self.id = id
        # The saved task name. Use this value for subsequent run, delete, list runs, and download results operations.
        self.name = name
        # The DataWorks workspace ID to which the task belongs. Use this value as the ProjectId for GetSemanticJobDetail, GetSemanticJobLog, and KillSemanticJob.
        self.project_id = project_id
        # The list of associated uploaded file IDs. For singleTableFile, the single file in this list is read at runtime.
        self.reference_file_ids = reference_file_ids
        # The list of associated external reference file URIs. For singleTableFile, the single file in this list is read at runtime.
        self.reference_file_uris = reference_file_uris
        # The ID of the resource group that will be used when running this task.
        self.resource_group_id = resource_group_id
        # The saved input datasource config, corresponding to the Source in the creation request. The data scope to be analyzed is determined based on this configuration at runtime.
        self.source = source
        # The saved Source.type data source type, used to quickly identify the task input type.
        self.type = type
        # The identifier of the user who created the task.
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

