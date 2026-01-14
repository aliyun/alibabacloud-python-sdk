# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryReadableResourcesListByUserIdResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.QueryReadableResourcesListByUserIdResponseBodyResult] = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The list of works that the user has permission to view.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.QueryReadableResourcesListByUserIdResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryReadableResourcesListByUserIdResponseBodyResult(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        directory: main_models.QueryReadableResourcesListByUserIdResponseBodyResultDirectory = None,
        modify_name: str = None,
        modify_time: str = None,
        owner_id: str = None,
        owner_name: str = None,
        security_level: str = None,
        status: int = None,
        third_part_auth_flag: int = None,
        work_name: str = None,
        work_type: str = None,
        works_id: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The timestamp of the creation time in milliseconds.
        self.create_time = create_time
        # Remarks on the work.
        self.description = description
        # The directory structure in which the work is located.
        self.directory = directory
        # The name of the Alibaba Cloud account to which the modifier belongs.
        self.modify_name = modify_name
        # The timestamp of the modification time in milliseconds.
        self.modify_time = modify_time
        # The Quick BI UserID of the work owner.
        self.owner_id = owner_id
        # The Alibaba Cloud account name of the owner.
        self.owner_name = owner_name
        # Security policies for collaborative authorization of works. Valid values:
        # 
        # *   0: private
        # *   12: Authorize specified members
        # *   1 or 11: Authorize all workspace members
        # 
        # > 
        # 
        # *   If you use legacy permissions, the return value is 1.
        # 
        # *   If you use the new permissions, the return value is 11.
        self.security_level = security_level
        # The status of the report. Valid values:
        # 
        # *   0: unpublished
        # *   1: published
        # *   2: modified but not published
        # *   3: unpublished
        self.status = status
        # Third-party embedding status. Valid values:
        # 
        # *   0: The embed service is not enabled.
        # *   1: Embed is enabled.
        self.third_part_auth_flag = third_part_auth_flag
        # The name of the work.
        self.work_name = work_name
        # The type of the work. Valid values:
        # 
        # *   DATAPRODUCT: BI portal
        # *   PAGE: Dashboard
        # *   FULLPAGE: full-screen dashboards
        # *   REPORT: workbook
        self.work_type = work_type
        # The ID of the work.
        self.works_id = works_id
        # The ID of the workspace to which the work belongs.
        self.workspace_id = workspace_id
        # The name of the workspace to which the work belongs.
        self.workspace_name = workspace_name

    def validate(self):
        if self.directory:
            self.directory.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.directory is not None:
            result['Directory'] = self.directory.to_map()

        if self.modify_name is not None:
            result['ModifyName'] = self.modify_name

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level

        if self.status is not None:
            result['Status'] = self.status

        if self.third_part_auth_flag is not None:
            result['ThirdPartAuthFlag'] = self.third_part_auth_flag

        if self.work_name is not None:
            result['WorkName'] = self.work_name

        if self.work_type is not None:
            result['WorkType'] = self.work_type

        if self.works_id is not None:
            result['WorksId'] = self.works_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Directory') is not None:
            temp_model = main_models.QueryReadableResourcesListByUserIdResponseBodyResultDirectory()
            self.directory = temp_model.from_map(m.get('Directory'))

        if m.get('ModifyName') is not None:
            self.modify_name = m.get('ModifyName')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ThirdPartAuthFlag') is not None:
            self.third_part_auth_flag = m.get('ThirdPartAuthFlag')

        if m.get('WorkName') is not None:
            self.work_name = m.get('WorkName')

        if m.get('WorkType') is not None:
            self.work_type = m.get('WorkType')

        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

class QueryReadableResourcesListByUserIdResponseBodyResultDirectory(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        path_id: str = None,
        path_name: str = None,
    ):
        # The ID of the directory.
        self.id = id
        # The name of the directory.
        self.name = name
        # The hierarchical structure of the directory ID, which is separated with \\"/\\".
        self.path_id = path_id
        # The hierarchical structure of the directory name, which is separated with \\"/\\".
        self.path_name = path_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.path_id is not None:
            result['PathId'] = self.path_id

        if self.path_name is not None:
            result['PathName'] = self.path_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')

        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')

        return self

