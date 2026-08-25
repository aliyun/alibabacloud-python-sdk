# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListDeploymentPackageFilesResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListDeploymentPackageFilesResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListDeploymentPackageFilesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDeploymentPackageFilesResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        deployment_package_files: List[main_models.ListDeploymentPackageFilesResponseBodyPagingInfoDeploymentPackageFiles] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of file versions pending deployment.
        self.deployment_package_files = deployment_package_files
        # The page number, starting from 1.
        self.page_number = page_number
        # The page size. Default value: 10.
        self.page_size = page_size
        # The total number of entries that meet the conditions.
        self.total_count = total_count

    def validate(self):
        if self.deployment_package_files:
            for v1 in self.deployment_package_files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeploymentPackageFiles'] = []
        if self.deployment_package_files is not None:
            for k1 in self.deployment_package_files:
                result['DeploymentPackageFiles'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deployment_package_files = []
        if m.get('DeploymentPackageFiles') is not None:
            for k1 in m.get('DeploymentPackageFiles'):
                temp_model = main_models.ListDeploymentPackageFilesResponseBodyPagingInfoDeploymentPackageFiles()
                self.deployment_package_files.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDeploymentPackageFilesResponseBodyPagingInfoDeploymentPackageFiles(DaraModel):
    def __init__(
        self,
        change_type: int = None,
        comment: str = None,
        commit_time: str = None,
        commit_user: str = None,
        commit_user_name: str = None,
        file_id: int = None,
        file_name: str = None,
        file_type: int = None,
        file_version: int = None,
        id: int = None,
        is_same_as_production_version: bool = None,
        node_configuration: str = None,
        node_id: int = None,
        project_id: int = None,
        smoke_test_status: str = None,
        status: int = None,
        tenant_id: int = None,
        use_type: str = None,
    ):
        # The change type. Valid values: 
        # - 0: added.
        # - 1: updated.
        # - 2: deleted.
        self.change_type = change_type
        # The comment provided at the time of commit.
        self.comment = comment
        # The commit time.
        # 
        # The format is `yyyy-MM-dd HH:mm:ss`, for example, `2025-04-10 15:55:47`. This example does not include a time zone identifier.
        self.commit_time = commit_time
        # The Alibaba Cloud account ID of the committer.
        self.commit_user = commit_user
        # The Alibaba Cloud account name of the committer.
        self.commit_user_name = commit_user_name
        # The ID of the file.
        self.file_id = file_id
        # The name of the file that generated this file version.
        self.file_name = file_name
        # The file type. Different file types have different codes. For more information, see [DataWorks nodes](https://help.aliyun.com/document_detail/600169.html).
        self.file_type = file_type
        # The version number of the file.
        self.file_version = file_version
        # The unique identifier.
        self.id = id
        # Indicates whether this version is the same as the current production version in scheduling.
        self.is_same_as_production_version = is_same_as_production_version
        # The scheduling property configuration of the scheduling node to which this file belongs, stored as a JSON string.
        self.node_configuration = node_configuration
        # The node ID in scheduling that corresponds to this file.
        self.node_id = node_id
        # The workspace ID.
        self.project_id = project_id
        # The testing status in the development environment.
        self.smoke_test_status = smoke_test_status
        # The status of the code file for this version. Valid values: 
        # - 2: commit check in progress.
        # - 3: commit check succeeded.
        # - 4: commit check rejected.
        # - 10: committing. 
        # - 11: committed to the scheduling development environment. 
        # - 20: review approved.
        # - 21: review failed.
        # - 22: check has warnings.
        # - 23: code review in progress.
        # - 24: code review rejected.
        # - 80: deployment package created. 
        # - 100: deploying. 
        # - 101: deployed to production. 
        # - 200: canceled.
        self.status = status
        # The DataWorks tenant ID.
        self.tenant_id = tenant_id
        # The functional module to which the file belongs. Valid values:
        # - NORMAL: data development.
        # - MANUAL: manual task.
        # - MANUAL_BIZ: manual workflow.
        # - SKIP: dry-run scheduling in data development.
        # - ADHOCQUERY: ad hoc query.
        # - COMPONENT: component management.
        self.use_type = use_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_type is not None:
            result['ChangeType'] = self.change_type

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.commit_time is not None:
            result['CommitTime'] = self.commit_time

        if self.commit_user is not None:
            result['CommitUser'] = self.commit_user

        if self.commit_user_name is not None:
            result['CommitUserName'] = self.commit_user_name

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.file_version is not None:
            result['FileVersion'] = self.file_version

        if self.id is not None:
            result['Id'] = self.id

        if self.is_same_as_production_version is not None:
            result['IsSameAsProductionVersion'] = self.is_same_as_production_version

        if self.node_configuration is not None:
            result['NodeConfiguration'] = self.node_configuration

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.smoke_test_status is not None:
            result['SmokeTestStatus'] = self.smoke_test_status

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.use_type is not None:
            result['UseType'] = self.use_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeType') is not None:
            self.change_type = m.get('ChangeType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CommitTime') is not None:
            self.commit_time = m.get('CommitTime')

        if m.get('CommitUser') is not None:
            self.commit_user = m.get('CommitUser')

        if m.get('CommitUserName') is not None:
            self.commit_user_name = m.get('CommitUserName')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('FileVersion') is not None:
            self.file_version = m.get('FileVersion')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsSameAsProductionVersion') is not None:
            self.is_same_as_production_version = m.get('IsSameAsProductionVersion')

        if m.get('NodeConfiguration') is not None:
            self.node_configuration = m.get('NodeConfiguration')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SmokeTestStatus') is not None:
            self.smoke_test_status = m.get('SmokeTestStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UseType') is not None:
            self.use_type = m.get('UseType')

        return self

