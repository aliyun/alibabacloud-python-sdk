# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Receiver(DaraModel):
    def __init__(
        self,
        comment: str = None,
        created_at: int = None,
        created_by: str = None,
        receiver_name: str = None,
        receiver_tenant_id: int = None,
        updated_at: int = None,
        updated_by: str = None,
    ):
        self.comment = comment
        self.created_at = created_at
        self.created_by = created_by
        self.receiver_name = receiver_name
        self.receiver_tenant_id = receiver_tenant_id
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

        if self.receiver_name is not None:
            result['receiverName'] = self.receiver_name

        if self.receiver_tenant_id is not None:
            result['receiverTenantId'] = self.receiver_tenant_id

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

        if m.get('receiverName') is not None:
            self.receiver_name = m.get('receiverName')

        if m.get('receiverTenantId') is not None:
            self.receiver_tenant_id = m.get('receiverTenantId')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')

        return self

