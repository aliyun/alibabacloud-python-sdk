# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateContextDatabaseWorkspaceRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        generate_initial_key: bool = None,
        member_name: str = None,
        permission_mode: str = None,
        workspace_name: str = None,
    ):
        # The ID of the cluster to which the workspace belongs. This parameter is optional.
        # - If you do not specify this parameter, the cluster selection logic that prioritizes account-exclusive storage is used.
        # - `default`: The shared cluster is used.
        # - Cluster IDs starting with `acc-`: The associated dedicated cluster is used.
        self.cluster_id = cluster_id
        # Specifies whether to generate an initial API key. This parameter is optional. Default value: `true`.
        # - `true`: Generates the first API key and returns the key name and plaintext key.
        # - `false`: Does not generate an initial API key. The ApiKeyName and ApiKey fields in the response are empty.
        self.generate_initial_key = generate_initial_key
        # The name of the first member when the workspace is created. This parameter is optional.
        self.member_name = member_name
        # The permission mode selected when the workspace is created. Valid values:
        # - `compatibility`: The compatibility mode. This mode is used if you do not specify this parameter.
        # - `advanced`: The advanced permission mode. Only the Alibaba Cloud account can select this mode. It takes effect immediately after the workspace is created and cannot be disabled.
        # 
        # This parameter is a string, not a Boolean switch. Valid values are case-insensitive and ignore leading and trailing whitespace. If you explicitly pass an empty string, pure whitespace, or other values, `InvalidParameter` (HTTP 400) is returned. If a RAM user selects `advanced`, `NoPermission` (HTTP 403) is returned.
        self.permission_mode = permission_mode
        # The name of the workspace.
        # 
        # This parameter is required.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.generate_initial_key is not None:
            result['GenerateInitialKey'] = self.generate_initial_key

        if self.member_name is not None:
            result['MemberName'] = self.member_name

        if self.permission_mode is not None:
            result['PermissionMode'] = self.permission_mode

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('GenerateInitialKey') is not None:
            self.generate_initial_key = m.get('GenerateInitialKey')

        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')

        if m.get('PermissionMode') is not None:
            self.permission_mode = m.get('PermissionMode')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

