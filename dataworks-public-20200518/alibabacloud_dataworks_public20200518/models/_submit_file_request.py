# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitFileRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        file_id: int = None,
        project_id: int = None,
        project_identifier: str = None,
        skip_all_deploy_file_extensions: bool = None,
    ):
        # The comment for the submission.
        self.comment = comment
        # The ID of the file. Obtain this ID by calling the [ListFiles](https://help.aliyun.com/document_detail/173942.html) operation.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The ID of the DataWorks workspace. You can log on to the DataWorks Console and go to the Workspace Configurations page to obtain the workspace ID. Specify either this parameter or `ProjectIdentifier` to identify the DataWorks workspace.
        self.project_id = project_id
        # The name of the DataWorks workspace. You can log on to the DataWorks Console and go to the Workspace Configurations page to obtain the workspace name. Specify either this parameter or `ProjectId` to identify the DataWorks workspace.
        self.project_identifier = project_identifier
        # Specifies whether to skip the pre-deployment check after the file is submitted.
        # 
        # - false: Do not skip. After the file is submitted, the pre-deployment check process is automatically triggered. The file becomes deployable only after it passes the check.
        # 
        # - true: Skip. The pre-deployment check process is not triggered after the file is submitted. You can proceed directly with the deployment process.
        self.skip_all_deploy_file_extensions = skip_all_deploy_file_extensions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier

        if self.skip_all_deploy_file_extensions is not None:
            result['SkipAllDeployFileExtensions'] = self.skip_all_deploy_file_extensions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')

        if m.get('SkipAllDeployFileExtensions') is not None:
            self.skip_all_deploy_file_extensions = m.get('SkipAllDeployFileExtensions')

        return self

