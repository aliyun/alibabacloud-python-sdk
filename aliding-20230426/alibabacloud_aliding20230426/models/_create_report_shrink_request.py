# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateReportShrinkRequest(DaraModel):
    def __init__(
        self,
        contents_shrink: str = None,
        dd_from: str = None,
        template_id: str = None,
        tenant_context_shrink: str = None,
        to_chat: bool = None,
        to_cids_shrink: str = None,
        to_userids_shrink: str = None,
    ):
        # This parameter is required.
        self.contents_shrink = contents_shrink
        # This parameter is required.
        self.dd_from = dd_from
        # This parameter is required.
        self.template_id = template_id
        self.tenant_context_shrink = tenant_context_shrink
        # This parameter is required.
        self.to_chat = to_chat
        self.to_cids_shrink = to_cids_shrink
        self.to_userids_shrink = to_userids_shrink

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

        if self.to_chat is not None:
            result['ToChat'] = self.to_chat

        if self.to_cids_shrink is not None:
            result['ToCids'] = self.to_cids_shrink

        if self.to_userids_shrink is not None:
            result['ToUserids'] = self.to_userids_shrink

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

        if m.get('ToChat') is not None:
            self.to_chat = m.get('ToChat')

        if m.get('ToCids') is not None:
            self.to_cids_shrink = m.get('ToCids')

        if m.get('ToUserids') is not None:
            self.to_userids_shrink = m.get('ToUserids')

        return self

