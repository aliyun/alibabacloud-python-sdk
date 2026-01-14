# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class AppOperationAddress(DaraModel):
    def __init__(
        self,
        actions: List[main_models.AppOperateAction] = None,
    ):
        self.actions = actions

    def validate(self):
        if self.actions:
            for v1 in self.actions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Actions'] = []
        if self.actions is not None:
            for k1 in self.actions:
                result['Actions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k1 in m.get('Actions'):
                temp_model = main_models.AppOperateAction()
                self.actions.append(temp_model.from_map(k1))

        return self

