# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateExportMigrationRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        export_mode: str = None,
        export_object_status: str = None,
        incremental_since: int = None,
        name: str = None,
        project_id: int = None,
    ):
        # The description of the export task.
        self.description = description
        # The export mode of the task. Valid values:
        # - FULL: exports the target task in full.
        # - INCREMENTAL: incrementally exports the target task from a specified point in time. If you select this mode, you must also configure the IncrementalSince parameter.
        # 
        # This parameter is required.
        self.export_mode = export_mode
        # The status of the export task. The system exports tasks in the specified status. Valid values:
        # - SAVED: saved. Tasks that have been saved are exported.
        # - SUBMITTED: submitted. Tasks that have been submitted are exported.
        # - DEPLOYED: deployed. Tasks that have been deployed are exported.
        self.export_object_status = export_object_status
        # The start time for incrementally exporting the target node.
        # 
        # This parameter takes effect only when the ExportMode parameter settings is set to INCREMENTAL.
        self.incremental_since = incremental_since
        # The name of the export task.
        # 
        # The name must be unique. No duplicate export task names can exist in the current DataWorks workspace.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the workspace configuration page to obtain the workspace ID.
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
        if self.description is not None:
            result['Description'] = self.description

        if self.export_mode is not None:
            result['ExportMode'] = self.export_mode

        if self.export_object_status is not None:
            result['ExportObjectStatus'] = self.export_object_status

        if self.incremental_since is not None:
            result['IncrementalSince'] = self.incremental_since

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExportMode') is not None:
            self.export_mode = m.get('ExportMode')

        if m.get('ExportObjectStatus') is not None:
            self.export_object_status = m.get('ExportObjectStatus')

        if m.get('IncrementalSince') is not None:
            self.incremental_since = m.get('IncrementalSince')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

