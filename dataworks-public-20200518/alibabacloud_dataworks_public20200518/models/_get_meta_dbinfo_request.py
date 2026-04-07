# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMetaDBInfoRequest(DaraModel):
    def __init__(
        self,
        app_guid: str = None,
        cluster_id: str = None,
        data_source_type: str = None,
        database_name: str = None,
    ):
        # The compute engine instance ID. Specify the ID in the `Engine type.Engine name` format.
        self.app_guid = app_guid
        # The E-MapReduce (EMR) cluster ID.
        self.cluster_id = cluster_id
        # The type of the data source. Valid values: odps and emr.
        self.data_source_type = data_source_type
        # The name of the metadatabase of the EMR cluster.
        self.database_name = database_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_guid is not None:
            result['AppGuid'] = self.app_guid

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppGuid') is not None:
            self.app_guid = m.get('AppGuid')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        return self

