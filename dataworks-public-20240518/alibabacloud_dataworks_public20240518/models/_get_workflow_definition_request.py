# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWorkflowDefinitionRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        include_script_content: bool = None,
        project_id: int = None,
    ):
        # The ID of the workflow.
        # 
        # This parameter is required.
        self.id = id
        # 查询结果是否包含工作流内部节点的脚本内容（对于内容较多的节点，可能存在较长的网络传输延时）。
        self.include_script_content = include_script_content
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.include_script_content is not None:
            result['IncludeScriptContent'] = self.include_script_content

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IncludeScriptContent') is not None:
            self.include_script_content = m.get('IncludeScriptContent')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

