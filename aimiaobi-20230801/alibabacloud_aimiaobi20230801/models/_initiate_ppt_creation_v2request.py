# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InitiatePptCreationV2Request(DaraModel):
    def __init__(
        self,
        external_user_id: str = None,
        is_mobile: bool = None,
        outline: str = None,
        ppt_template_id: int = None,
        ppt_template_type: int = None,
        ppt_title: str = None,
        process_type: int = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        # The unique ID of the external user.
        self.external_user_id = external_user_id
        # Specifies whether the request originates from a mobile client.
        self.is_mobile = is_mobile
        # The presentation outline, formatted in Markdown.
        self.outline = outline
        # The ID of the PPT template.
        self.ppt_template_id = ppt_template_id
        # The template type. The default value is `1`. Valid values: `1` (system template) and `2` (enterprise template).
        self.ppt_template_type = ppt_template_type
        self.ppt_title = ppt_title
        # The type of process to initiate. Valid values:<br>
        # `0`: Generates only a signature to initialize the front-end SDK for the full creation process.<br>
        # `1`: Generates a signature and a process ID. Use this option if you have a custom front-end page for templates before you initialize the SDK.<br>
        # `2`: Generates an artifact ID, which allows for direct editing of the artifact.<br>
        # `3`: Generates an export task ID. You can poll this ID to retrieve the export result.<br><br><br><br>
        self.process_type = process_type
        # The ID of the task.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The ID of the workspace.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_user_id is not None:
            result['ExternalUserId'] = self.external_user_id

        if self.is_mobile is not None:
            result['IsMobile'] = self.is_mobile

        if self.outline is not None:
            result['Outline'] = self.outline

        if self.ppt_template_id is not None:
            result['PptTemplateId'] = self.ppt_template_id

        if self.ppt_template_type is not None:
            result['PptTemplateType'] = self.ppt_template_type

        if self.ppt_title is not None:
            result['PptTitle'] = self.ppt_title

        if self.process_type is not None:
            result['ProcessType'] = self.process_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalUserId') is not None:
            self.external_user_id = m.get('ExternalUserId')

        if m.get('IsMobile') is not None:
            self.is_mobile = m.get('IsMobile')

        if m.get('Outline') is not None:
            self.outline = m.get('Outline')

        if m.get('PptTemplateId') is not None:
            self.ppt_template_id = m.get('PptTemplateId')

        if m.get('PptTemplateType') is not None:
            self.ppt_template_type = m.get('PptTemplateType')

        if m.get('PptTitle') is not None:
            self.ppt_title = m.get('PptTitle')

        if m.get('ProcessType') is not None:
            self.process_type = m.get('ProcessType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

