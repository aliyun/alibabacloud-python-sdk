# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTableShrinkRequest(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        client_token: str = None,
        columns_shrink: str = None,
        comment: str = None,
        name: str = None,
        namespace: str = None,
        retention_policy_shrink: str = None,
    ):
        # The data catalog to which the table belongs.
        self.catalog = catalog
        # The idempotency token.
        self.client_token = client_token
        # The column definitions.
        self.columns_shrink = columns_shrink
        # The description.
        self.comment = comment
        # The name of the table.
        # 
        # This parameter is required.
        self.name = name
        # The namespace to which the table belongs.
        self.namespace = namespace
        # The data retention policy.
        self.retention_policy_shrink = retention_policy_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.columns_shrink is not None:
            result['Columns'] = self.columns_shrink

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.retention_policy_shrink is not None:
            result['RetentionPolicy'] = self.retention_policy_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Columns') is not None:
            self.columns_shrink = m.get('Columns')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RetentionPolicy') is not None:
            self.retention_policy_shrink = m.get('RetentionPolicy')

        return self

