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
        # Specify this parameter if you want to create the node inside a container. This parameter represents the unique identifier of the container, which can be a workflow or a container node.
        # 
        # >  If this parameter is specified, the path field defined in FlowSpec is ignored.
        # 
        # >  Prior to SDK version 8.0.0, this field is of type Long. In SDK version 8.0.0 and later, it is of type String. This change does not affect the normal use of the SDK. The parameter is returned based on the type defined in the SDK. Compilation failures caused by the type change may occur only when you upgrade the SDK across version 8.0.0. In this case, you must manually update the data type.
        self.container_id = container_id
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id
        # Specify this parameter if you want to create the node inside a container. This parameter represents the unique identifier of the container, which can be a workflow or a container node.
        # 
        # >  If this parameter is specified, the path field defined in FlowSpec is ignored.
        # 
        # >  Prior to SDK version 8.0.0, this field is of type Long. In SDK version 8.0.0 and later, it is of type String. This change does not affect the normal use of the SDK. The parameter is returned based on the type defined in the SDK. Compilation failures caused by the type change may occur only when you upgrade the SDK across version 8.0.0. In this case, you must manually update the data type.
        # 
        # This parameter is required.
        self.scene = scene
        # The FlowSpec information that describes the node. For more information, see [FlowSpec](https://github.com/aliyun/alibabacloud-dataworks-tool-dflow).
        # 
        # >  How do I quickly obtain a FlowSpec template?
        # 
        # *   Go to Data Studio, open a node, click Version on the right side, find the latest version, and then click Scheduling Settings to obtain the FlowSpec description of the current node. You can use the FlowSpec description in the version to quickly build a template that meets your requirements.
        # 
        # >  How do I configure the node content?
        # 
        # *   Enter the code for the node in the $.spec.nodes[].script.content field.
        # 
        # >  How do I configure a batch synchronization node?
        # 
        # *   Write the script by referring to Step 4 in [Configure an offline sync task in the code editor](https://help.aliyun.com/zh/dataworks/user-guide/configure-a-batch-synchronization-node-by-using-the-code-editor), and then enter the script content in the $.spec.nodes[\\*].script.content field. Alternatively, you can create a batch synchronization node in the console and view its version information to obtain the script content.
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

