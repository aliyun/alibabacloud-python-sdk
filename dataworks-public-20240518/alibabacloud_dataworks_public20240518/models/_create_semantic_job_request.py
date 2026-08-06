# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class CreateSemanticJobRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        project_id: int = None,
        reference_file_ids: List[str] = None,
        reference_file_uris: List[str] = None,
        resource_group_id: str = None,
        source: Dict[str, Any] = None,
    ):
        # The semantic job name, which also serves as the job identifier for subsequent calls to RunSemanticJob, DeleteSemanticJob, ListSemanticJobRuns, and DownloadSemanticResults. The name must be unique within the current tenant.
        # 
        # This parameter is required.
        self.name = name
        # The DataWorks workspace ID. This parameter is required for all Source.type values except singleTableFile. The Data.ProjectId in the creation result can be reused for GetSemanticJobDetail, GetSemanticJobLog, and KillSemanticJob.
        self.project_id = project_id
        # The list of uploaded reference file IDs. When Source.type=singleTableFile, use either this parameter or ReferenceFileUris, and the selected array must contain exactly one non-empty element. The ID must come from Data.FileId returned by UploadSemanticFile, and only CSV or XLSX files are supported. For other Source.type values, you can pass multiple IDs. The service validates each ID during creation, and you can also pass ReferenceFileUris at the same time.
        self.reference_file_ids = reference_file_ids
        # The list of reference file URIs accessible by the caller. When Source.type=singleTableFile, use either this parameter or ReferenceFileIds, and the selected array must contain exactly one non-empty URI. For other Source.type values, you can pass multiple URIs and also pass ReferenceFileIds at the same time. When using the upload path from UploadSemanticFile, pass Data.FileId after the PUT upload is complete instead of the short-lived UploadUrl.
        self.reference_file_uris = reference_file_uris
        # The ID of the resource group used to run the semantic job. RunSemanticJob does not accept this parameter and instead uses the resource group saved during creation.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # The input datasource config for the semantic node. The type field is required. This parameter specifies the data to be analyzed and is not the semantic_model YAML output. The domain field is a character string that serves as the identity of the business domain and focus of the node, such as sales. Supported types: 1) maxcompute: Use pinnedScopeInfo to specify the scope. Array elements contain type and name. When type=project, name is the MaxCompute project name. When type=schema, project is the project name and name is the schema name. For table-level scope, project is the project name, schema is optional, and name is the table name. 2) holo or starrocks: In addition to type, you must specify dataSourceName and dataSourceEnv, and pass ProjectId at the top level of the request. You can use pinnedScopeInfo to limit the scope to schemas or tables. The name element is the schema or table name, and the schema element for table-level scope is the database or schema. 3) singleTableFile: ProjectId is not required. For file reference rules, see ReferenceFileIds and ReferenceFileUris. After the node runs successfully, use DownloadSemanticResults to retrieve the semantic_model YAML and other result files. The example shows a MaxCompute project-level scope.
        # 
        # This parameter is required.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        return self

