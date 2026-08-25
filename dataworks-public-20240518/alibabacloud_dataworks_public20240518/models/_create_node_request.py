# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNodeRequest(DaraModel):
    def __init__(
        self,
        container_id: str = None,
        project_id: int = None,
        scene: str = None,
        spec: str = None,
    ):
        # The unique identifier of a container in which you want to create the node. The container can be a workflow or a container node. Specify this parameter when you need to create the node inside a container.
        # 
        # >Notice: If this parameter is specified, the path field defined in FlowSpec becomes invalid.
        # 
        # >Notice: This field was of the Long type in SDK versions earlier than 8.0.0 and is of the String type in SDK 8.0.0 and later. **This change does not affect normal SDK usage, and the parameter is still returned in the type defined in the SDK**. Only when you upgrade across SDK version 8.0.0, the type change may cause project compilation failures, and you need to manually correct the data type.
        self.container_id = container_id
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace Management page to obtain the ID.
        # 
        # This parameter specifies the DataWorks workspace for this API call operation.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The scenario in which the node is created. This parameter determines whether the node is created in the manual node area or the data development area. DATAWORKS_MANUAL_WORKFLOW can be used only when ContainerId is specified and the container is a manual workflow.
        # 
        # Valid values:
        # 
        # - DATAWORKS_PROJECT: project directory.
        # - DATAWORKS_MANUAL_WORKFLOW: manual workflow.
        # - DATAWORKS_MANUAL_TASK: manual task.
        # 
        # This parameter is required.
        self.scene = scene
        # The FlowSpec information that describes the node. For more information about the specification, see [FlowSpec](https://github.com/aliyun/alibabacloud-dataworks-tool-dflow).
        # 
        # > How to quickly obtain a FlowSpec template?
        # > - In DataStudio, open a node, click Versions on the right side, view the latest version, and then view the scheduling configuration. This provides the FlowSpec description for the current node. You can use the FlowSpec description in the version to quickly build a template that meets your requirements.
        # 
        # > How to specify the node content?
        # > - Specify the node content in the $.spec.nodes[*].script.content field.
        # 
        # > How to configure the content of a batch synchronization node?
        # > - Write a script by following Step 4 in [Configure a batch synchronization node by using the code editor](https://www.alibabacloud.com/help/en/dataworks/user-guide/configure-a-batch-synchronization-node-by-using-the-code-editor), and specify the content in the $.spec.nodes[*].script.content field. Alternatively, create a batch synchronization node on the page and obtain the script content by viewing the version.
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
        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

