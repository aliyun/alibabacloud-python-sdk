# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitAuditTaskRequest(DaraModel):
    def __init__(
        self,
        article_id: str = None,
        content: str = None,
        html_content: str = None,
        title: str = None,
        workspace_id: str = None,
    ):
        self.article_id = article_id
        self.content = content
        self.html_content = html_content
        self.title = title
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.article_id is not None:
            result['ArticleId'] = self.article_id

        if self.content is not None:
            result['Content'] = self.content

        if self.html_content is not None:
            result['HtmlContent'] = self.html_content

        if self.title is not None:
            result['Title'] = self.title

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArticleId') is not None:
            self.article_id = m.get('ArticleId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('HtmlContent') is not None:
            self.html_content = m.get('HtmlContent')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

