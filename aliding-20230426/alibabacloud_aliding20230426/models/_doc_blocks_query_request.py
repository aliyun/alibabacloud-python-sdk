# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class DocBlocksQueryRequest(DaraModel):
    def __init__(
        self,
        block_type: str = None,
        doc_key: str = None,
        end_index: int = None,
        start_index: int = None,
        tenant_context: main_models.DocBlocksQueryRequestTenantContext = None,
    ):
        self.block_type = block_type
        # This parameter is required.
        self.doc_key = doc_key
        self.end_index = end_index
        self.start_index = start_index
        self.tenant_context = tenant_context

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_type is not None:
            result['BlockType'] = self.block_type

        if self.doc_key is not None:
            result['DocKey'] = self.doc_key

        if self.end_index is not None:
            result['EndIndex'] = self.end_index

        if self.start_index is not None:
            result['StartIndex'] = self.start_index

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockType') is not None:
            self.block_type = m.get('BlockType')

        if m.get('DocKey') is not None:
            self.doc_key = m.get('DocKey')

        if m.get('EndIndex') is not None:
            self.end_index = m.get('EndIndex')

        if m.get('StartIndex') is not None:
            self.start_index = m.get('StartIndex')

        if m.get('TenantContext') is not None:
            temp_model = main_models.DocBlocksQueryRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class DocBlocksQueryRequestTenantContext(DaraModel):
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

