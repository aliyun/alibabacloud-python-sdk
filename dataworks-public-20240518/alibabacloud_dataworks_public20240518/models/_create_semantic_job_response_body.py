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
        # The saved semantic task definition. Use `Data.Name` to call RunSemanticJob, DeleteSemanticJob, ListSemanticJobRuns, and DownloadSemanticResults.
        self.data = data
        # The request ID. You can use this ID to locate logs and troubleshoot issues.
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
        # The identifier of the task creator, which has the same value as `UserId` and identifies who created the task.
        self.creator = creator
        # The time when the task definition was created. The value is a UNIX timestamp in milliseconds.
        self.gmt_create = gmt_create
        # The time when the task definition was last modified. The value is a UNIX timestamp in milliseconds.
        self.gmt_modified = gmt_modified
        # The internal unique ID of the task definition, which is used to identify the created task.
        self.id = id
        # The saved task name. This value is used for subsequent operations such as running, deleting, querying run records, and downloading results.
        self.name = name
        # The ID of the DataWorks workspace to which the task belongs. This ID is used as the `ProjectId` for GetSemanticJobDetail, GetSemanticJobLog, and KillSemanticJob.
        self.project_id = project_id
        # The list of IDs of associated uploaded files. If the source type is `singleTableFile`, the task reads the only file in the list at runtime.
        self.reference_file_ids = reference_file_ids
        # The list of URIs of associated external reference files. If the source type is `singleTableFile`, the task reads the only file in the list at runtime.
        self.reference_file_uris = reference_file_uris
        # The identifier of the resource group to be used when running this task.
        self.resource_group_id = resource_group_id
        # The saved input data source configuration, which corresponds to `Source` in the creation request. The data scope to be analyzed is selected based on this config during runtime.
        self.source = source
        # The saved `Source.type` data source type, which is used to quickly identify the task input type.
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

