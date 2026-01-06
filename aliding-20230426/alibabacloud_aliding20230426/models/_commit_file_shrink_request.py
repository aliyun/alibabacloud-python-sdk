# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CommitFileShrinkRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        option_shrink: str = None,
        parent_dentry_uuid: str = None,
        tenant_context_shrink: str = None,
        upload_key: str = None,
    ):
        self.name = name
        self.option_shrink = option_shrink
        self.parent_dentry_uuid = parent_dentry_uuid
        self.tenant_context_shrink = tenant_context_shrink
        self.upload_key = upload_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.option_shrink is not None:
            result['Option'] = self.option_shrink

        if self.parent_dentry_uuid is not None:
            result['ParentDentryUuid'] = self.parent_dentry_uuid

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.upload_key is not None:
            result['UploadKey'] = self.upload_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Option') is not None:
            self.option_shrink = m.get('Option')

        if m.get('ParentDentryUuid') is not None:
            self.parent_dentry_uuid = m.get('ParentDentryUuid')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('UploadKey') is not None:
            self.upload_key = m.get('UploadKey')

        return self

