# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWorkspaceRequest(DaraModel):
    def __init__(
        self,
        allow_publish: bool = None,
        allow_share: bool = None,
        allow_view_all: bool = None,
        default_share_to_all: bool = None,
        only_admin_create_datasource: bool = None,
        use_comment: bool = None,
        workspace_description: str = None,
        workspace_name: str = None,
    ):
        # Specifies whether reports in the workspace can be made public. Default value: true.
        self.allow_publish = allow_publish
        # Specifies whether reports in the workspace can be shared. Default value: true.
        self.allow_share = allow_share
        # Specifies whether the workspace is in collaboration mode. Default value: true.
        self.allow_view_all = allow_view_all
        # Specifies whether to grant read permissions on the works in the workspace to all workspace members by default. Default value: false.
        self.default_share_to_all = default_share_to_all
        # Specifies whether only administrators can create data sources in the workspace. Default value: false.
        self.only_admin_create_datasource = only_admin_create_datasource
        # Specifies whether to use table remarks when you create a dataset in the workspace. Default value: true.
        self.use_comment = use_comment
        # The description of the workspace.
        self.workspace_description = workspace_description
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
        if self.allow_publish is not None:
            result['AllowPublish'] = self.allow_publish

        if self.allow_share is not None:
            result['AllowShare'] = self.allow_share

        if self.allow_view_all is not None:
            result['AllowViewAll'] = self.allow_view_all

        if self.default_share_to_all is not None:
            result['DefaultShareToAll'] = self.default_share_to_all

        if self.only_admin_create_datasource is not None:
            result['OnlyAdminCreateDatasource'] = self.only_admin_create_datasource

        if self.use_comment is not None:
            result['UseComment'] = self.use_comment

        if self.workspace_description is not None:
            result['WorkspaceDescription'] = self.workspace_description

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowPublish') is not None:
            self.allow_publish = m.get('AllowPublish')

        if m.get('AllowShare') is not None:
            self.allow_share = m.get('AllowShare')

        if m.get('AllowViewAll') is not None:
            self.allow_view_all = m.get('AllowViewAll')

        if m.get('DefaultShareToAll') is not None:
            self.default_share_to_all = m.get('DefaultShareToAll')

        if m.get('OnlyAdminCreateDatasource') is not None:
            self.only_admin_create_datasource = m.get('OnlyAdminCreateDatasource')

        if m.get('UseComment') is not None:
            self.use_comment = m.get('UseComment')

        if m.get('WorkspaceDescription') is not None:
            self.workspace_description = m.get('WorkspaceDescription')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

