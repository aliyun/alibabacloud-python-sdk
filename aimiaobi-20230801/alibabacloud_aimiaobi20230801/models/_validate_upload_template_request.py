# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ValidateUploadTemplateRequest(DaraModel):
    def __init__(
        self,
        file_key: str = None,
        task_type: str = None,
        template_type: str = None,
        workspace_id: str = None,
    ):
        # File key.
        # 
        # This parameter is required.
        self.file_key = file_key
        # Task type. Valid values: lightAppSass (SaaS page call) or sdkBatchTask (SDK batch task).
        self.task_type = task_type
        # Template type. Valid values: Content (content asset template) or PositiveSample (positive sample template).
        # 
        # This parameter is required.
        self.template_type = template_type
        # Unique identifier of your Alibaba Cloud Model Studio workspace. To get this ID, see [Workspace ID](https://help.aliyun.com/document_detail/2782167.html).
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_key is not None:
            result['FileKey'] = self.file_key

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

