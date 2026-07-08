# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EditBiddingDocRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_format: str = None,
        content_type: str = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        # The text content.
        self.content = content
        # The format.
        self.content_format = content_format
        # The content type.
        self.content_type = content_type
        # The task ID.
        self.task_id = task_id
        # [The workspace ID.](https://help.aliyun.com/document_detail/2782167.html)
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.content_format is not None:
            result['ContentFormat'] = self.content_format

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentFormat') is not None:
            self.content_format = m.get('ContentFormat')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

