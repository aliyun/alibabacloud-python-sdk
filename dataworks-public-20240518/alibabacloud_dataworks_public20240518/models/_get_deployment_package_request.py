# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDeploymentPackageRequest(DaraModel):
    def __init__(
        self,
        deployment_id: int = None,
        project_id: int = None,
        project_identifier: str = None,
    ):
        # The ID of the deployment package.
        # 
        # A deployment package ID is generated when you call [SubmitFile](https://help.aliyun.com/document_detail/173944.html) or [DeployFile](https://help.aliyun.com/document_detail/173956.html).
        # 
        # This parameter is required.
        self.deployment_id = deployment_id
        # The ID of the DataWorks workspace.
        # 
        # You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the workspace configuration page to obtain the workspace ID.
        # 
        # This parameter specifies the DataWorks workspace for this API call.
        self.project_id = project_id
        # The unique identifier of the DataWorks workspace, which is the English identifier displayed at the top of the DataStudio page for switching workspaces.
        # 
        # You must specify either this parameter or ProjectId to determine the DataWorks workspace for this API call.
        self.project_identifier = project_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_id is not None:
            result['DeploymentId'] = self.deployment_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentId') is not None:
            self.deployment_id = m.get('DeploymentId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')

        return self

