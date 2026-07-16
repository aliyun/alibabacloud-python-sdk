# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNodesRequest(DaraModel):
    def __init__(
        self,
        container_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        recurrence: str = None,
        rerun_mode: str = None,
        scene: str = None,
    ):
        # The ID of the container. If you specify this parameter, only nodes in the specified container are returned. This parameter is independent of the resource group (ResourceGroupId).
        # 
        # >Notice: 
        # 
        # This parameter is of the Long type in SDK versions earlier than 8.0.0 and of the String type in SDK 8.0.0 and later. **This change does not affect SDK usage. The parameter is returned in the type defined for your SDK version.** The type change may cause compilation errors only when you upgrade the SDK across version 8.0.0. In this case, you must manually correct the data type.
        self.container_id = container_id
        # The node name. Fuzzy search is supported.
        self.name = name
        # The page number of the results to return.
        self.page_number = page_number
        # The number of entries per page. Default: 10. Maximum: 100.
        self.page_size = page_size
        # The ID of the DataWorks workspace. To find this ID, log in to the [DataWorks console](https://workbench.data.aliyun.com/console) and navigate to the workspace configuration page.
        # 
        # This parameter is required.
        self.project_id = project_id
        # Filters nodes by their scheduling type. Valid values:
        # 
        # - Normal: The node runs as scheduled.
        # 
        # - Pause: The node is paused and blocks its dependent downstream nodes.
        # 
        # - Skip: The node is skipped, and the system immediately returns a success status with a 0-second execution time. This action does not block downstream nodes or consume resources.
        self.recurrence = recurrence
        # The rerun mode. Valid values:
        # 
        # - Allowed: The node can be rerun regardless of whether it succeeded or failed.
        # 
        # - FailureAllowed: The node can be rerun only if its previous run failed.
        # 
        # - Denied: The node cannot be rerun regardless of whether it succeeded or failed.
        self.rerun_mode = rerun_mode
        # The context for filtering nodes. In data development, this corresponds to the sections in the directory tree on the left. If you omit this parameter, no filtering is applied. Valid values:
        # 
        # - DataworksProject: Nodes in the project directory.
        # 
        # - DataworksManualWorkflow: manual workflow
        # 
        # - DataworksManualTask: manual task
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.recurrence is not None:
            result['Recurrence'] = self.recurrence

        if self.rerun_mode is not None:
            result['RerunMode'] = self.rerun_mode

        if self.scene is not None:
            result['Scene'] = self.scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Recurrence') is not None:
            self.recurrence = m.get('Recurrence')

        if m.get('RerunMode') is not None:
            self.rerun_mode = m.get('RerunMode')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        return self

