# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TestNetworkConnectionRequest(DaraModel):
    def __init__(
        self,
        datasource_name: str = None,
        env_type: str = None,
        project_id: int = None,
        resource_group: str = None,
    ):
        # The name of the data source.
        # 
        # This parameter is required.
        self.datasource_name = datasource_name
        # The environment in which the data source resides. Valid values:
        # 
        # *   0: development environment
        # *   1: production environment
        # 
        # This parameter is required.
        self.env_type = env_type
        # The ID of the DataWorks workspace to which the data source belongs. You can call the [ListProjects](https://help.aliyun.com/document_detail/178393.html) operation to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The identifier of the resource group. You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/173913.html) operation to query the identifier of the resource group.
        # 
        # This parameter is required.
        self.resource_group = resource_group

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

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        return self

