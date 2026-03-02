# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PdpResource(DaraModel):
    def __init__(
        self,
        address: str = None,
        company_id: int = None,
        configuration: str = None,
        credentials: str = None,
        description: str = None,
        env: str = None,
        id: int = None,
        name: str = None,
        namespace: str = None,
        product_id: int = None,
        request_id: str = None,
        type: str = None,
        use_scope: str = None,
        use_type: str = None,
    ):
        # This parameter is required.
        self.address = address
        # This parameter is required.
        self.company_id = company_id
        self.configuration = configuration
        # This parameter is required.
        self.credentials = credentials
        self.description = description
        # This parameter is required.
        self.env = env
        self.id = id
        # This parameter is required.
        self.name = name
        self.namespace = namespace
        # This parameter is required.
        self.product_id = product_id
        self.request_id = request_id
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.use_scope = use_scope
        # This parameter is required.
        self.use_type = use_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.configuration is not None:
            result['configuration'] = self.configuration

        if self.credentials is not None:
            result['credentials'] = self.credentials

        if self.description is not None:
            result['description'] = self.description

        if self.env is not None:
            result['env'] = self.env

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.type is not None:
            result['type'] = self.type

        if self.use_scope is not None:
            result['useScope'] = self.use_scope

        if self.use_type is not None:
            result['useType'] = self.use_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('configuration') is not None:
            self.configuration = m.get('configuration')

        if m.get('credentials') is not None:
            self.credentials = m.get('credentials')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('useScope') is not None:
            self.use_scope = m.get('useScope')

        if m.get('useType') is not None:
            self.use_type = m.get('useType')

        return self

