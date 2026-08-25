# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeployFileRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        file_id: int = None,
        node_id: int = None,
        project_id: int = None,
        project_identifier: str = None,
    ):
        # The description of the deployment.
        self.comment = comment
        # The ID of the file. You can call [ListFiles](https://help.aliyun.com/document_detail/173942.html) to query the file ID. You need to specify only one of this parameter and the NodeId parameter settings.
        self.file_id = file_id
        # The ID of the node in the scheduling system that corresponds to the file to be published.
        # 
        # You need to specify only one of this parameter and the FileId parameter settings.
        self.node_id = node_id
        # The ID of the DataWorks workspace.
        # 
        # You can log on to the DataWorks console and go to the workspace configuration page to obtain the workspace ID. You must specify either this parameter or ProjectIdentifier to determine the DataWorks workspace for this API call.
        self.project_id = project_id
        # The name of the DataWorks workspace.
        # 
        # You can log on to the DataWorks console and go to the workspace configuration page to obtain the workspace name. You must specify either this parameter or ProjectId to determine the DataWorks workspace for this API call.
        self.project_identifier = project_identifier

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

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')

        return self

