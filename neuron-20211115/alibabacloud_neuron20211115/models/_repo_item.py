# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RepoItem(DaraModel):
    def __init__(
        self,
        code_lines: int = None,
        git_project_url: str = None,
        owner: str = None,
        repo_short_url: str = None,
        repo_url: str = None,
        summary: str = None,
    ):
        self.code_lines = code_lines
        self.git_project_url = git_project_url
        self.owner = owner
        self.repo_short_url = repo_short_url
        self.repo_url = repo_url
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_lines is not None:
            result['codeLines'] = self.code_lines

        if self.git_project_url is not None:
            result['gitProjectUrl'] = self.git_project_url

        if self.owner is not None:
            result['owner'] = self.owner

        if self.repo_short_url is not None:
            result['repoShortUrl'] = self.repo_short_url

        if self.repo_url is not None:
            result['repoUrl'] = self.repo_url

        if self.summary is not None:
            result['summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeLines') is not None:
            self.code_lines = m.get('codeLines')

        if m.get('gitProjectUrl') is not None:
            self.git_project_url = m.get('gitProjectUrl')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('repoShortUrl') is not None:
            self.repo_short_url = m.get('repoShortUrl')

        if m.get('repoUrl') is not None:
            self.repo_url = m.get('repoUrl')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        return self

