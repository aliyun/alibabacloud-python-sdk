# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloneDataSourceRequest(DaraModel):
    def __init__(
        self,
        clone_data_source_name: str = None,
        id: int = None,
    ):
        # The name of the target data source. The name can contain letters, digits, and underscores (_), and cannot start with a digit or an underscore. The name can be up to 60 characters in length.
        # 
        # This parameter is required.
        self.clone_data_source_name = clone_data_source_name
        # The ID of the data source, which is the unique identifier of the data source. You can call the ListDataSources operation to query existing data sources and their unique IDs.
        # 
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clone_data_source_name is not None:
            result['CloneDataSourceName'] = self.clone_data_source_name

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloneDataSourceName') is not None:
            self.clone_data_source_name = m.get('CloneDataSourceName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

