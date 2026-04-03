# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class BatchEvaluateWorkspacePermissionsOutput(DaraModel):
    def __init__(
        self,
        results: List[main_models.WorkspacePermissionEvaluateResult] = None,
    ):
        # 各 workspace 的权限校验结果列表；顺序与请求 workspaceIds 一致
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('results') is not None:
            for k1 in m.get('results'):
                temp_model = main_models.WorkspacePermissionEvaluateResult()
                self.results.append(temp_model.from_map(k1))

        return self

