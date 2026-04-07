# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMigrationSummaryRequest(DaraModel):
    def __init__(
        self,
        migration_id: int = None,
        project_id: int = None,
    ):
        # The migration task ID.
        # 
        # You can call the [CreateImportMigration](https://help.aliyun.com/document_detail/2780280.html) operation to obtain the ID of the import task and call the [CreateExportMigration](https://help.aliyun.com/document_detail/2780281.html) operation to obtain the ID of the export task.
        # 
        # This parameter is required.
        self.migration_id = migration_id
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to obtain the workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.migration_id is not None:
            result['MigrationId'] = self.migration_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigrationId') is not None:
            self.migration_id = m.get('MigrationId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

