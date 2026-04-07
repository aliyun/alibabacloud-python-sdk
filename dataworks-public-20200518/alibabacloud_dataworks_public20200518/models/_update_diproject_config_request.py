# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDIProjectConfigRequest(DaraModel):
    def __init__(
        self,
        destination_type: str = None,
        project_config: str = None,
        project_id: int = None,
        source_type: str = None,
    ):
        # The type of the destinations of the synchronization solutions. This parameter cannot be left empty. Valid values: analyticdb_for_mysql, odps, elasticsearch, holo, mysql, and polardb.
        # 
        # This parameter is required.
        self.destination_type = destination_type
        # The new default global configuration of the synchronization solutions. The value indicates the processing rules of different types of DDL messages. The value must be in the JSON format. Example: {"RENAMECOLUMN":"WARNING","DROPTABLE":"WARNING","CREATETABLE":"WARNING","MODIFYCOLUMN":"WARNING","TRUNCATETABLE":"WARNING","DROPCOLUMN":"WARNING","ADDCOLUMN":"WARNING","RENAMETABLE":"WARNING"}.
        # 
        # Field description:
        # 
        # *   RENAMECOLUMN: renames a column.
        # *   DROPTABLE: deletes a table.
        # *   CREATETABLE: creates a table.
        # *   MODIFYCOLUMN: changes the data type of a column.
        # *   TRUNCATETABLE: clears a table.
        # *   DROPCOLUMN: deletes a column.
        # *   ADDCOLUMN: creates a column.
        # *   RENAMETABLE: renames a table.
        # 
        # DataWorks processes a DDL message of a specific type based on the following rules:
        # 
        # *   WARNING: ignores the message and records an alert in real-time synchronization logs. The alert contains information about the situation that the message is ignored because of an execution error.
        # *   IGNORE: discards the message and does not send it to the destination.
        # *   CRITICAL: terminates the real-time synchronization task and sets the node status to Failed.
        # *   NORMAL: sends the message to the destination to process the message. Each destination processes DDL messages based on its own business logic. If DataWorks adopts the NORMAL policy, DataWorks only forwards DDL messages.
        # 
        # This parameter is required.
        self.project_config = project_config
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to obtain the workspace ID.
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

        if self.project_config is not None:
            result['ProjectConfig'] = self.project_config

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

        if m.get('ProjectConfig') is not None:
            self.project_config = m.get('ProjectConfig')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

