# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AsyncWritingBiddingDocRequest(DaraModel):
    def __init__(
        self,
        company_keyword: str = None,
        prompt: str = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        self.company_keyword = company_keyword
        self.prompt = prompt
        self.task_id = task_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_keyword is not None:
            result['CompanyKeyword'] = self.company_keyword

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyKeyword') is not None:
            self.company_keyword = m.get('CompanyKeyword')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

