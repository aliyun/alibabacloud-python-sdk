# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PdpServiceUpdateCmd(DaraModel):
    def __init__(
        self,
        alias: str = None,
        code_branch: str = None,
        description: str = None,
        extra_info: str = None,
        git_repo: str = None,
        id: int = None,
        jump_url: str = None,
    ):
        self.alias = alias
        self.code_branch = code_branch
        self.description = description
        self.extra_info = extra_info
        self.git_repo = git_repo
        # This parameter is required.
        self.id = id
        self.jump_url = jump_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.code_branch is not None:
            result['codeBranch'] = self.code_branch

        if self.description is not None:
            result['description'] = self.description

        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info

        if self.git_repo is not None:
            result['gitRepo'] = self.git_repo

        if self.id is not None:
            result['id'] = self.id

        if self.jump_url is not None:
            result['jumpUrl'] = self.jump_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('codeBranch') is not None:
            self.code_branch = m.get('codeBranch')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')

        if m.get('gitRepo') is not None:
            self.git_repo = m.get('gitRepo')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('jumpUrl') is not None:
            self.jump_url = m.get('jumpUrl')

        return self

