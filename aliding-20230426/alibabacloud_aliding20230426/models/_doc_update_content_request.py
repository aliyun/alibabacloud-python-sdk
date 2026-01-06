# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class DocUpdateContentRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        data_type: str = None,
        doc_key: str = None,
        tenant_context: main_models.DocUpdateContentRequestTenantContext = None,
    ):
        # This parameter is required.
        self.content = content
        self.data_type = data_type
        # This parameter is required.
        self.doc_key = doc_key
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

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.doc_key is not None:
            result['DocKey'] = self.doc_key

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('DocKey') is not None:
            self.doc_key = m.get('DocKey')

        if m.get('TenantContext') is not None:
            temp_model = main_models.DocUpdateContentRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class DocUpdateContentRequestTenantContext(DaraModel):
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

