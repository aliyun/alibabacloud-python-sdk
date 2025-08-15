# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Share(DaraModel):
    def __init__(
        self,
        comment: str = None,
        created_at: int = None,
        created_by: str = None,
        owner: str = None,
        provider_tenant_id: int = None,
        share_id: str = None,
        share_name: str = None,
        updated_at: int = None,
        updated_by: str = None,
    ):
        self.comment = comment
        self.created_at = created_at
        self.created_by = created_by
        self.owner = owner
        self.provider_tenant_id = provider_tenant_id
        self.share_id = share_id
        self.share_name = share_name
        self.updated_at = updated_at
        self.updated_by = updated_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.owner is not None:
            result['owner'] = self.owner

        if self.provider_tenant_id is not None:
            result['providerTenantId'] = self.provider_tenant_id

        if self.share_id is not None:
            result['shareId'] = self.share_id

        if self.share_name is not None:
            result['shareName'] = self.share_name

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('providerTenantId') is not None:
            self.provider_tenant_id = m.get('providerTenantId')

        if m.get('shareId') is not None:
            self.share_id = m.get('shareId')

        if m.get('shareName') is not None:
            self.share_name = m.get('shareName')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')

        return self

