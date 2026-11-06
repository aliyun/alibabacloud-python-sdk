# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePluginWorkspaceRequest(DaraModel):
    def __init__(
        self,
        gateway_type: str = None,
        organization_id: str = None,
        repo_name: str = None,
        workspace_name: str = None,
    ):
        # The gateway type. If this parameter is not specified, the server defaults to API.
        self.gateway_type = gateway_type
        # The Codeup organization ID for the Yunxiao DevOps organization. The frontend obtains this ID by parsing the ListPluginRepositories response or after creating an organization.
        # 
        # This parameter is required.
        self.organization_id = organization_id
        # The repository name, which also serves as the English ID of the plugin. The backend does not validate the format. The frontend restricts the value to the regular expression /^(?![-.])[a-z0-9.-]{1,20}(?<![-.])$/, which allows 1 to 20 lowercase letters, digits, periods, or hyphens, and must not start or end with a period or a hyphen.
        # 
        # This parameter is required.
        self.repo_name = repo_name
        # The workspace name, which is the Chinese name of the plugin. Note: This parameter is required. If it is omitted, the API returns a 400 InvalidParameter.IsEmpty error.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

        if self.organization_id is not None:
            result['organizationId'] = self.organization_id

        if self.repo_name is not None:
            result['repoName'] = self.repo_name

        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

        if m.get('organizationId') is not None:
            self.organization_id = m.get('organizationId')

        if m.get('repoName') is not None:
            self.repo_name = m.get('repoName')

        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')

        return self

