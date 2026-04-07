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
        # The description of the commit operation.
        self.comment = comment
        # The file ID. You can call the [ListFiles](https://help.aliyun.com/document_detail/173942.html) operation to query the file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The DataWorks workspace ID. You can log on to the DataWorks console and go to the Workspace page to query the ID. You must configure either this parameter or the ProjectIdentifier parameter to determine the DataWorks workspace to which the operation is applied.
        self.project_id = project_id
        # The name of the DataWorks workspace. You can log on to the DataWorks console and go to the Workspace page to obtain the workspace name. You must configure either this parameter or the ProjectId parameter to determine the DataWorks workspace to which the operation is applied.
        self.project_identifier = project_identifier
        # Specifies whether to skip the pre-publish check after the file is committed. Valid values:
        # 
        # *   false: indicates that the pre-publish check is not skipped. After the file is committed, the pre-publish check is automatically triggered. The file can be deployed only after the file passes the check.
        # *   true: indicates that the pre-publish check is skipped. After the file is submitted, the pre-publish check process is not triggered. You can directly deploy the file.
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

