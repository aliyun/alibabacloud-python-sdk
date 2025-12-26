# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class WorkspaceSpecs(DaraModel):
    def __init__(
        self,
        product: str = None,
        specs: List[main_models.WorkspaceSpec] = None,
        workspace_id: str = None,
    ):
        self.product = product
        self.specs = specs
        self.workspace_id = workspace_id

    def validate(self):
        if self.specs:
            for v1 in self.specs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product is not None:
            result['Product'] = self.product

        result['Specs'] = []
        if self.specs is not None:
            for k1 in self.specs:
                result['Specs'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')

        self.specs = []
        if m.get('Specs') is not None:
            for k1 in m.get('Specs'):
                temp_model = main_models.WorkspaceSpec()
                self.specs.append(temp_model.from_map(k1))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

