# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWorkflowDefinitionRequest(DaraModel):
    def __init__(
        self,
        project_id: int = None,
        spec: str = None,
    ):
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace Configuration page to obtain the workspace ID. You can also call the ListProjects operation to query the workspace ID of the current tenant.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The FlowSpec information that describes the workflow. For more information about the specifications, see [FlowSpec](https://github.com/aliyun/alibabacloud-dataworks-tool-dflow).
        # 
        # > How do I quickly obtain a FlowSpec template?
        # > - Open a workflow in DataStudio and click Show Spec in the upper-right corner to obtain the FlowSpec description for the current workflow. You can quickly build a compliant template based on this FlowSpec description.
        # 
        # >Notice: This operation only supports creating workflows. Internal nodes described in the FlowSpec are not created.</notice>
        # 
        # This parameter is required.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

