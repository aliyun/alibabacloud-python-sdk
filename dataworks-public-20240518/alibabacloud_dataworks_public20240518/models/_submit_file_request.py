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
        # The description of the submission.
        self.comment = comment
        # The file ID. You can call the [ListFiles](https://help.aliyun.com/document_detail/173942.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The DataWorks workspace ID. You can log on to the DataWorks console and go to the Workspace page to query the ID. You must specify either this parameter or the ProjectIdentifier parameter to identify the DataWorks workspace when you call this operation.
        self.project_id = project_id
        # The name of the DataWorks workspace. You can log on to the DataWorks console and go to the Workspace page to query the workspace name. You must specify either this parameter or the ProjectId parameter to identify the DataWorks workspace when you call this operation.
        self.project_identifier = project_identifier
        # Whether to skip the pre-deployment check after the file is submitted:
        # 
        # *   false: Do not skip. After the file is submitted, the system automatically triggers the pre-deployment check. The file becomes available for deployment only after the check is passed.
        # *   true: Skip. After the file is submitted, the system does not trigger the pre-deployment check. The file can proceed directly to deployment.
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

