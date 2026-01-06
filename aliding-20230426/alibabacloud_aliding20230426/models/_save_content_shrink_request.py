# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveContentShrinkRequest(DaraModel):
    def __init__(
        self,
        contents_shrink: str = None,
        dd_from: str = None,
        template_id: str = None,
        tenant_context_shrink: str = None,
    ):
        # This parameter is required.
        self.contents_shrink = contents_shrink
        # This parameter is required.
        self.dd_from = dd_from
        # This parameter is required.
        self.template_id = template_id
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contents_shrink is not None:
            result['Contents'] = self.contents_shrink

        if self.dd_from is not None:
            result['DdFrom'] = self.dd_from

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contents') is not None:
            self.contents_shrink = m.get('Contents')

        if m.get('DdFrom') is not None:
            self.dd_from = m.get('DdFrom')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

