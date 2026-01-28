# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDatasourceRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        connection_params: str = None,
        datasource_id: int = None,
        description: str = None,
        name: str = None,
        password: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        self.connection_params = connection_params
        # This parameter is required.
        self.datasource_id = datasource_id
        self.description = description
        self.name = name
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.connection_params is not None:
            result['ConnectionParams'] = self.connection_params

        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.password is not None:
            result['Password'] = self.password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ConnectionParams') is not None:
            self.connection_params = m.get('ConnectionParams')

        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        return self

