# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateImportMigrationRequest(DaraModel):
    def __init__(
        self,
        calculate_engine_map: str = None,
        commit_rule: str = None,
        description: str = None,
        name: str = None,
        package_file: str = None,
        package_type: str = None,
        project_id: int = None,
        resource_group_map: str = None,
        workspace_map: str = None,
    ):
        # The mapping between the source compute engine instance and the destination compute engine instance. The following types of compute engine instances are supported: MaxCompute, E-MapReduce (EMR), Hadoop CDH, and Hologres.
        self.calculate_engine_map = calculate_engine_map
        # The rule configured for automatically committing and deploying the import task. The rule contains the following parameters:
        # 
        # *   resourceAutoCommit: specifies whether resources are automatically committed. The value true indicates yes and the value false indicates no.
        # *   resourceAutoDeploy: specifies whether resources are automatically deployed. The value true indicates yes and the value false indicates no.
        # *   functionAutoCommit: specifies whether the function is automatically committed. The value true indicates yes and the value false indicates no.
        # *   functionAutoDeploy: specifies whether the function is automatically deployed. The value true indicates yes and the value false indicates no.
        # *   tableAutoCommitToDev: specifies whether the table is automatically committed to the development environment. The value true indicates yes and the value false indicates no.
        # *   tableAutoCommitToProd: specifies whether the table is automatically committed to the production environment. The value true indicates yes and the value false indicates no.
        # *   ignoreLock: specifies whether the lock is automatically ignored when an import task is locked. The value true indicates yes and the value false indicates no. If you set this parameter to true for an import task, you can forcefully update the task even if the task is locked.
        # *   fileAutoCommit: specifies whether the file is automatically committed. The value true indicates yes and the value false indicates no.
        # *   fileAutoDeploy: specifies whether the file is automatically deployed. The value true indicates yes and the value false indicates no.
        self.commit_rule = commit_rule
        # The description of the import package.
        self.description = description
        # The name of the import task. The name must be unique within the workspace.
        # 
        # This parameter is required.
        self.name = name
        # The path of the import package. **The import package must be uploaded. Example of the upload method:**
        # 
        # ```java
        #         Config config = new Config();
        #         config.setAccessKeyId(accessId);
        #         config.setAccessKeySecret(accessKey);
        #         config.setEndpoint(popEndpoint);
        #         config.setRegionId(regionId);
        # 
        #         Client client = new Client(config);
        # 
        #         CreateImportMigrationAdvanceRequest request = new CreateImportMigrationAdvanceRequest();
        #         request.setName("test_migration_api_" + System.currentTimeMillis());
        #         request.setProjectId(123456L); 
        #         request.setPackageType("DATAWORKS_MODEL");
        #         request.setPackageFileObject(new FileInputStream("/home/admin/Downloads/test.zip"));
        # 
        #         RuntimeOptions runtime = new RuntimeOptions();
        #         CreateImportMigrationResponse response = client.createImportMigrationAdvance(request, runtime);
        # ```
        # 
        # This parameter is required.
        self.package_file = package_file
        # The type of the import package. Valid values:
        # 
        # *   DATAWORKS_MODEL (standard format)
        # *   DATAWORKS_V2 (Apsara Stack DataWorks V3.6.1 to V3.11)
        # *   DATAWORKS_V3 (Apsara Stack DataWorks V3.12 and later)
        # 
        # This parameter is required.
        self.package_type = package_type
        # The DataWorks workspace ID. You can log on to the DataWorks console and go to the Workspace page to obtain the workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The mapping between the resource group for scheduling and the resource group for Data Integration. The keys and values in the mapping are the identifiers of the resource groups. Specify the mapping in the following format:
        # 
        # ```json
        # {
        #     "SCHEDULER_RESOURCE_GROUP": {
        #         "xxx": "yyy"
        #     },
        #     "DI_RESOURCE_GROUP": {
        #         "ccc": "dfdd"
        #     }
        # }
        # ```
        self.resource_group_map = resource_group_map
        # The mapping between the prefixes for the names of the source and destination workspaces. When the system performs the import operation, the prefix for the name of the source workspace in the import package is replaced based on the mapping.
        self.workspace_map = workspace_map

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calculate_engine_map is not None:
            result['CalculateEngineMap'] = self.calculate_engine_map

        if self.commit_rule is not None:
            result['CommitRule'] = self.commit_rule

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.package_file is not None:
            result['PackageFile'] = self.package_file

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.resource_group_map is not None:
            result['ResourceGroupMap'] = self.resource_group_map

        if self.workspace_map is not None:
            result['WorkspaceMap'] = self.workspace_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalculateEngineMap') is not None:
            self.calculate_engine_map = m.get('CalculateEngineMap')

        if m.get('CommitRule') is not None:
            self.commit_rule = m.get('CommitRule')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PackageFile') is not None:
            self.package_file = m.get('PackageFile')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ResourceGroupMap') is not None:
            self.resource_group_map = m.get('ResourceGroupMap')

        if m.get('WorkspaceMap') is not None:
            self.workspace_map = m.get('WorkspaceMap')

        return self

