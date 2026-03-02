# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RepoMetric(DaraModel):
    def __init__(
        self,
        code_lines: int = None,
        commit_cnt: int = None,
        developer_cnt: int = None,
        refresh_date: str = None,
        repo_short_url: str = None,
        repo_url: str = None,
    ):
        self.code_lines = code_lines
        self.commit_cnt = commit_cnt
        self.developer_cnt = developer_cnt
        self.refresh_date = refresh_date
        self.repo_short_url = repo_short_url
        # This parameter is required.
        self.repo_url = repo_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_lines is not None:
            result['codeLines'] = self.code_lines

        if self.commit_cnt is not None:
            result['commitCnt'] = self.commit_cnt

        if self.developer_cnt is not None:
            result['developerCnt'] = self.developer_cnt

        if self.refresh_date is not None:
            result['refreshDate'] = self.refresh_date

        if self.repo_short_url is not None:
            result['repoShortUrl'] = self.repo_short_url

        if self.repo_url is not None:
            result['repoUrl'] = self.repo_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeLines') is not None:
            self.code_lines = m.get('codeLines')

        if m.get('commitCnt') is not None:
            self.commit_cnt = m.get('commitCnt')

        if m.get('developerCnt') is not None:
            self.developer_cnt = m.get('developerCnt')

        if m.get('refreshDate') is not None:
            self.refresh_date = m.get('refreshDate')

        if m.get('repoShortUrl') is not None:
            self.repo_short_url = m.get('repoShortUrl')

        if m.get('repoUrl') is not None:
            self.repo_url = m.get('repoUrl')

        return self

