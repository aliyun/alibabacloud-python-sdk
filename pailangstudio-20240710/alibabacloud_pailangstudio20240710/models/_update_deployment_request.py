# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDeploymentRequest(DaraModel):
    def __init__(
        self,
        auto_approval: bool = None,
        deployment_config: str = None,
        description: str = None,
        stage_action: str = None,
        workspace_id: str = None,
    ):
        # Indicates whether to automatically skip the deployment confirmation step.
        self.auto_approval = auto_approval
        # Service Configuration for deployment. For more information, see the [deployment configuration](https://help.aliyun.com/zh/pai/user-guide/parameters-of-model-services) of PAI-EAS.
        self.deployment_config = deployment_config
        # Deployment description.
        self.description = description
        # Deployment stage operation information. The JSON format is as follows:  
        # {"Stage":3,"Action":"Confirm"}. Valid values for Action are:  
        # * Confirm: confirm.  
        # * Cancel: cancel.
        self.stage_action = stage_action
        # Workspace ID. For information about how to obtain a workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_approval is not None:
            result['AutoApproval'] = self.auto_approval

        if self.deployment_config is not None:
            result['DeploymentConfig'] = self.deployment_config

        if self.description is not None:
            result['Description'] = self.description

        if self.stage_action is not None:
            result['StageAction'] = self.stage_action

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoApproval') is not None:
            self.auto_approval = m.get('AutoApproval')

        if m.get('DeploymentConfig') is not None:
            self.deployment_config = m.get('DeploymentConfig')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('StageAction') is not None:
            self.stage_action = m.get('StageAction')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

