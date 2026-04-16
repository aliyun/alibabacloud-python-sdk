# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterCreateClientRequest(DaraModel):
    def __init__(
        self,
        address: str = None,
        allowed_models: str = None,
        contact: str = None,
        discount: float = None,
        name: str = None,
        parent_id: int = None,
        remark: str = None,
    ):
        self.address = address
        self.allowed_models = allowed_models
        self.contact = contact
        self.discount = discount
        self.name = name
        self.parent_id = parent_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.allowed_models is not None:
            result['allowedModels'] = self.allowed_models

        if self.contact is not None:
            result['contact'] = self.contact

        if self.discount is not None:
            result['discount'] = self.discount

        if self.name is not None:
            result['name'] = self.name

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        if self.remark is not None:
            result['remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('allowedModels') is not None:
            self.allowed_models = m.get('allowedModels')

        if m.get('contact') is not None:
            self.contact = m.get('contact')

        if m.get('discount') is not None:
            self.discount = m.get('discount')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        return self

