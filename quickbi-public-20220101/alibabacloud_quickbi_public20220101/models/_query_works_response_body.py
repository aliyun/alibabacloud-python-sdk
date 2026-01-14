# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryWorksResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryWorksResponseBodyResult = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the work.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.QueryWorksResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryWorksResponseBodyResult(DaraModel):
    def __init__(
        self,
        auth_3rd_flag: int = None,
        description: str = None,
        directory: main_models.QueryWorksResponseBodyResultDirectory = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        modify_name: str = None,
        owner_id: str = None,
        owner_name: str = None,
        public_flag: bool = None,
        public_invalid_time: int = None,
        security_level: str = None,
        status: int = None,
        work_name: str = None,
        work_type: str = None,
        works_id: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # Third-party embedding status. Valid values:
        # 
        # *   0: The embed service is not enabled.
        # *   1: Embed is enabled.
        self.auth_3rd_flag = auth_3rd_flag
        # Remarks on the work.
        self.description = description
        # The directory to which the work belongs.
        self.directory = directory
        # The timestamp of the creation of the work in milliseconds.
        self.gmt_create = gmt_create
        # The timestamp of the modification of the work in milliseconds.
        self.gmt_modify = gmt_modify
        # The Alibaba Cloud account name of the person who modified the work.
        self.modify_name = modify_name
        # The user ID of the work owner in the Quick BI.
        self.owner_id = owner_id
        # The Alibaba Cloud account name of the work owner.
        self.owner_name = owner_name
        # Is it public
        self.public_flag = public_flag
        # Deadline for the public release of the report
        self.public_invalid_time = public_invalid_time
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
        # The name of the work.
        self.work_name = work_name
        # Queries the types of works. Fill in the blanks to query all types. Valid values:
        # 
        # *   DATAPRODUCT: BI portal
        # *   PAGE: Dashboard
        # *   FULLPAGE: full-screen dashboards
        # *   REPORT: workbook
        # *   dashboardOfflineQuery: self-service data retrieval
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
        if self.auth_3rd_flag is not None:
            result['Auth3rdFlag'] = self.auth_3rd_flag

        if self.description is not None:
            result['Description'] = self.description

        if self.directory is not None:
            result['Directory'] = self.directory.to_map()

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify

        if self.modify_name is not None:
            result['ModifyName'] = self.modify_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.public_flag is not None:
            result['PublicFlag'] = self.public_flag

        if self.public_invalid_time is not None:
            result['PublicInvalidTime'] = self.public_invalid_time

        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level

        if self.status is not None:
            result['Status'] = self.status

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
        if m.get('Auth3rdFlag') is not None:
            self.auth_3rd_flag = m.get('Auth3rdFlag')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Directory') is not None:
            temp_model = main_models.QueryWorksResponseBodyResultDirectory()
            self.directory = temp_model.from_map(m.get('Directory'))

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')

        if m.get('ModifyName') is not None:
            self.modify_name = m.get('ModifyName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('PublicFlag') is not None:
            self.public_flag = m.get('PublicFlag')

        if m.get('PublicInvalidTime') is not None:
            self.public_invalid_time = m.get('PublicInvalidTime')

        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')

        if m.get('Status') is not None:
            self.status = m.get('Status')

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

class QueryWorksResponseBodyResultDirectory(DaraModel):
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
        # The hierarchical structure of the directory ID to which the directory belongs. Separate the hierarchical structure with a /.
        self.path_id = path_id
        # The hierarchical structure of the directory to which the directory belongs. Separate the hierarchical structure with a (/).
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

