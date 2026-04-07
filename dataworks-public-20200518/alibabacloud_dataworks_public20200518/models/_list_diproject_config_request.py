# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDIProjectConfigRequest(DaraModel):
    def __init__(
        self,
        destination_type: str = None,
        project_id: int = None,
        source_type: str = None,
    ):
        # The type of the destinations of the synchronization solutions. This parameter cannot be left empty. Valid values: analyticdb_for_mysql, odps, elasticsearch, holo, mysql, and polardb.
        # 
        # This parameter is required.
        self.destination_type = destination_type
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to obtain the ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The type of the sources of the synchronization solutions. Valid values: oracle, mysql, polardb, datahub, drds, and analyticdb_for_mysql. If you do not configure this parameter, DataWorks applies the default global configuration to all sources.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

