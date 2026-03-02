# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class PbcRepoForkListResult(DaraModel):
    def __init__(
        self,
        repos_forks: List[main_models.ReposFork] = None,
        request_id: str = None,
    ):
        self.repos_forks = repos_forks
        self.request_id = request_id

    def validate(self):
        if self.repos_forks:
            for v1 in self.repos_forks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['reposForks'] = []
        if self.repos_forks is not None:
            for k1 in self.repos_forks:
                result['reposForks'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.repos_forks = []
        if m.get('reposForks') is not None:
            for k1 in m.get('reposForks'):
                temp_model = main_models.ReposFork()
                self.repos_forks.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

