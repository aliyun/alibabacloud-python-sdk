# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportWorkflowDefinitionRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        project_id: int = None,
        spec: str = None,
    ):
        # Specifies whether to call this operation in validation mode. If this parameter is set to true, only the legality of the input workflow spec is validated. The same preprocessing and validation logic as the actual import is reused (with identical rules), but no data is persisted and no write operations are performed. The validation result is returned through an asynchronous task. If validation fails, the asynchronous task fails, and the error details include the error code, error message, and a JSONPath that locates the specific node (such as $.spec.workflows[0].nodes[1]).
        # 
        # Default value: false. In this case, the workflow is imported normally.
        self.dry_run = dry_run
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the workspace management page to obtain the ID.
        # 
        # This parameter specifies the DataWorks workspace used for this API invoke.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The FlowSpec information that describes the workflow. For the specification details, see [FlowSpec](https://github.com/aliyun/alibabacloud-dataworks-tool-dflow/).
        # 
        # > How to quickly obtain a FlowSpec template?
        # > - Open a workflow in DataStudio, and then click "Show Spec" in the upper-right corner to obtain the FlowSpec description of the current workflow. You can use this FlowSpec description to quickly build a template that meets your requirements.
        # 
        # >Notice: This operation supports creating a workflow and its internal nodes at the same time. Pay attention to the IDs specified in the FlowSpec. If a specified ID already exists, the operation becomes an update. Only when no ID is specified or the ID does not exist does the operation become a create.
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
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

