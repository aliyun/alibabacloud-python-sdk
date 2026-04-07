# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDataSourceShareRequest(DaraModel):
    def __init__(
        self,
        datasource_name: str = None,
        env_type: str = None,
        project_id: int = None,
        project_permissions: str = None,
        user_permissions: str = None,
    ):
        # The name of the data source that you want to share.
        # 
        # This parameter is required.
        self.datasource_name = datasource_name
        # The environment in which the data source is used. Valid values:
        # 
        # *   0: development environment
        # *   1: production environment
        self.env_type = env_type
        # The ID of the DataWorks workspace to which the data source belongs. You can call the [ListProjects](https://help.aliyun.com/document_detail/178393.html) operation to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The DataWorks workspace to which you want to share the data source. If you configure this parameter, all members of the specified DataWorks workspace can view and use the data source. The value of this parameter is a JSON array. Example: [{"projectId":1000,"permission":"WRITE","sharedName":"PX_DATAHUB1.shared_name"}], Parameter description:
        # 
        # *   projectId: the ID of the DataWorks workspace to which you want to share the data source.
        # *   permission: the mode in which the data source is shared. Valid values: READ and WRITE. The value READ indicates that all members of the specified workspace can read data from the data source, but cannot modify the data. The value WRITE indicates that all members of the specified workspace can modify the data in the data source.
        # *   sharedName: the name of the data source that you want to share.
        self.project_permissions = project_permissions
        # The user to whom you want to share the data source. If you configure this parameter, the specified user can view or use the data source. The value of this parameter is a JSON array. Example: [{"projectId":10000,"users":[{"userId":"276184575345452131","permission":"WRITE"}],"sharedName":"PX_DATAHUB1.shared_name"}], Parameter description:
        # 
        # *   projectId: the ID of the DataWorks workspace. If you configure the UserPermissions parameter, the specified user can view or use the data source only in the specified DataWorks workspace.
        # *   userId: the ID of the user to whom you want to share the data source.
        # *   permission: the mode in which the data source is shared. Valid values: READ and WRITE. The value READ indicates that the specified user can read data from the data source, but cannot modify the data. The value WRITE indicates that the specified user can modify the data in the data source.
        # *   sharedName: the name of the data source that you want to share.
        # 
        # If the ProjectPermissions and UserPermissions parameters are both left empty, the specified data source is not shared to any DataWorks workspace or user. If neither of the parameters is left empty, both parameters take effect.
        self.user_permissions = user_permissions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_permissions is not None:
            result['ProjectPermissions'] = self.project_permissions

        if self.user_permissions is not None:
            result['UserPermissions'] = self.user_permissions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectPermissions') is not None:
            self.project_permissions = m.get('ProjectPermissions')

        if m.get('UserPermissions') is not None:
            self.user_permissions = m.get('UserPermissions')

        return self

