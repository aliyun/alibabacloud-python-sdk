# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PdpService(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        alias: str = None,
        code_branch: str = None,
        description: str = None,
        enterprise_id: int = None,
        extra_info: str = None,
        git_repo: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        jump_url: str = None,
        name: str = None,
        org_type: str = None,
        pbc_id: int = None,
        request_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.account_id = account_id
        # This parameter is required.
        self.alias = alias
        self.code_branch = code_branch
        self.description = description
        self.enterprise_id = enterprise_id
        self.extra_info = extra_info
        self.git_repo = git_repo
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.jump_url = jump_url
        # This parameter is required.
        self.name = name
        self.org_type = org_type
        # This parameter is required.
        self.pbc_id = pbc_id
        self.request_id = request_id
        self.status = status
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.alias is not None:
            result['alias'] = self.alias

        if self.code_branch is not None:
            result['codeBranch'] = self.code_branch

        if self.description is not None:
            result['description'] = self.description

        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info

        if self.git_repo is not None:
            result['gitRepo'] = self.git_repo

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.jump_url is not None:
            result['jumpUrl'] = self.jump_url

        if self.name is not None:
            result['name'] = self.name

        if self.org_type is not None:
            result['orgType'] = self.org_type

        if self.pbc_id is not None:
            result['pbcId'] = self.pbc_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('codeBranch') is not None:
            self.code_branch = m.get('codeBranch')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')

        if m.get('gitRepo') is not None:
            self.git_repo = m.get('gitRepo')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('jumpUrl') is not None:
            self.jump_url = m.get('jumpUrl')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('orgType') is not None:
            self.org_type = m.get('orgType')

        if m.get('pbcId') is not None:
            self.pbc_id = m.get('pbcId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

