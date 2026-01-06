# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class SaveContentRequest(DaraModel):
    def __init__(
        self,
        contents: List[main_models.SaveContentRequestContents] = None,
        dd_from: str = None,
        template_id: str = None,
        tenant_context: main_models.SaveContentRequestTenantContext = None,
    ):
        # This parameter is required.
        self.contents = contents
        # This parameter is required.
        self.dd_from = dd_from
        # This parameter is required.
        self.template_id = template_id
        self.tenant_context = tenant_context

    def validate(self):
        if self.contents:
            for v1 in self.contents:
                 if v1:
                    v1.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Contents'] = []
        if self.contents is not None:
            for k1 in self.contents:
                result['Contents'].append(k1.to_map() if k1 else None)

        if self.dd_from is not None:
            result['DdFrom'] = self.dd_from

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contents = []
        if m.get('Contents') is not None:
            for k1 in m.get('Contents'):
                temp_model = main_models.SaveContentRequestContents()
                self.contents.append(temp_model.from_map(k1))

        if m.get('DdFrom') is not None:
            self.dd_from = m.get('DdFrom')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TenantContext') is not None:
            temp_model = main_models.SaveContentRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class SaveContentRequestTenantContext(DaraModel):
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

class SaveContentRequestContents(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        key: str = None,
        sort: int = None,
        type: int = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.content_type = content_type
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.sort = sort
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.key is not None:
            result['Key'] = self.key

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

