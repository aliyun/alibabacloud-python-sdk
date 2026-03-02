# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class ReposFork(DaraModel):
    def __init__(
        self,
        git_group: str = None,
        gmt_create: str = None,
        id: int = None,
        is_origin: bool = None,
        pbc_repo_items: List[main_models.RepoItem] = None,
        request_id: str = None,
        usage: str = None,
    ):
        self.git_group = git_group
        self.gmt_create = gmt_create
        self.id = id
        self.is_origin = is_origin
        self.pbc_repo_items = pbc_repo_items
        self.request_id = request_id
        self.usage = usage

    def validate(self):
        if self.pbc_repo_items:
            for v1 in self.pbc_repo_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.git_group is not None:
            result['gitGroup'] = self.git_group

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.id is not None:
            result['id'] = self.id

        if self.is_origin is not None:
            result['isOrigin'] = self.is_origin

        result['pbcRepoItems'] = []
        if self.pbc_repo_items is not None:
            for k1 in self.pbc_repo_items:
                result['pbcRepoItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.usage is not None:
            result['usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gitGroup') is not None:
            self.git_group = m.get('gitGroup')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isOrigin') is not None:
            self.is_origin = m.get('isOrigin')

        self.pbc_repo_items = []
        if m.get('pbcRepoItems') is not None:
            for k1 in m.get('pbcRepoItems'):
                temp_model = main_models.RepoItem()
                self.pbc_repo_items.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('usage') is not None:
            self.usage = m.get('usage')

        return self

