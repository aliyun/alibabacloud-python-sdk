# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class InsertContentWithOptionsRequest(DaraModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        document_id: str = None,
        index: int = None,
        path: List[int] = None,
        tenant_context: main_models.InsertContentWithOptionsRequestTenantContext = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.document_id = document_id
        self.index = index
        self.path = path
        self.tenant_context = tenant_context

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.document_id is not None:
            result['DocumentId'] = self.document_id

        if self.index is not None:
            result['Index'] = self.index

        if self.path is not None:
            result['Path'] = self.path

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DocumentId') is not None:
            self.document_id = m.get('DocumentId')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('TenantContext') is not None:
            temp_model = main_models.InsertContentWithOptionsRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class InsertContentWithOptionsRequestTenantContext(DaraModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

