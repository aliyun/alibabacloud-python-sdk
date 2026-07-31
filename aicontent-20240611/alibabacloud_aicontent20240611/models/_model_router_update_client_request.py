# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterUpdateClientRequest(DaraModel):
    def __init__(
        self,
        address: str = None,
        allowed_model_group_config: str = None,
        allowed_models: str = None,
        contact: str = None,
        discount: float = None,
        name: str = None,
        remark: str = None,
        status: int = None,
    ):
        # The company address.
        self.address = address
        # The allowed model group configuration.
        self.allowed_model_group_config = allowed_model_group_config
        # The list of allowed model IDs, separated by commas. An empty value indicates all models are allowed.
        self.allowed_models = allowed_models
        # The contact information.
        self.contact = contact
        # The discount coefficient.
        self.discount = discount
        # The customer name.
        self.name = name
        # The remarks.
        self.remark = remark
        # The status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.allowed_model_group_config is not None:
            result['allowedModelGroupConfig'] = self.allowed_model_group_config

        if self.allowed_models is not None:
            result['allowedModels'] = self.allowed_models

        if self.contact is not None:
            result['contact'] = self.contact

        if self.discount is not None:
            result['discount'] = self.discount

        if self.name is not None:
            result['name'] = self.name

        if self.remark is not None:
            result['remark'] = self.remark

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('allowedModelGroupConfig') is not None:
            self.allowed_model_group_config = m.get('allowedModelGroupConfig')

        if m.get('allowedModels') is not None:
            self.allowed_models = m.get('allowedModels')

        if m.get('contact') is not None:
            self.contact = m.get('contact')

        if m.get('discount') is not None:
            self.discount = m.get('discount')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

