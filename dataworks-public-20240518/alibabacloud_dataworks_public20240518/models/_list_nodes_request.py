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
        # The ID of the container. This parameter is used as a filter condition to query nodes in a specified container. If you do not specify this parameter, leave it empty. This parameter is independent of the ResourceGroupId parameter.
        # 
        # >Notice: Before SDK version 8.0.0, this field is of the Long type. In SDK version 8.0.0 and later, this field is of the String type. **This change does not affect the normal use of the SDK, and the parameter is still returned based on the type defined in the SDK**. However, if you upgrade the SDK across version 8.0.0, the type change may cause project compilation failures. In this case, you must manually correct the data type.
        self.container_id = container_id
        # The name of the node. Fuzzy match is supported.
        self.name = name
        # The page number of the requested data.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace Management page to obtain the workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The scheduling type. This parameter is used as a filter condition. Valid values: 
        # 
        # - Normal: The node runs as expected.
        # 
        # - Pause: The node is paused, and the execution of its downstream nodes is blocked.
        #  
        # - Skip: The node is set to dry run. The system directly returns a success response with an execution duration of 0 seconds. This does not block the execution of downstream nodes or consume resources.
        self.recurrence = recurrence
        # The rerun mode. If you do not specify this parameter, leave it empty. Valid values: 
        # 
        # - Allowed: The node can be rerun regardless of whether it is successfully run or fails to run.
        #  
        # - FailureAllowed: The node can be rerun only after it fails to run.
        #  
        # - Denied: The node cannot be rerun regardless of whether it is successfully run or fails to run.
        self.rerun_mode = rerun_mode
        # The scenario to which the node belongs. This parameter is used as a filter condition. If you do not specify this parameter, leave it empty. In Data Studio, this parameter corresponds to the partitions in the left-side directory tree. Valid values: 
        # 
        # - DataworksProject: project directory.
        # 
        # - DataworksManualWorkflow: manual workflow. 
        # 
        # - DataworksManualTask: manual task.
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

