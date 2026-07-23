# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTableShrinkRequest(DaraModel):
    def __init__(
        self,
        add_column_shrink: str = None,
        catalog: str = None,
        client_token: str = None,
        delete_column_shrink: str = None,
        name: str = None,
        namespace: str = None,
        rename_column_shrink: str = None,
        update_column_comment_shrink: str = None,
        update_column_type_shrink: str = None,
        update_comment: str = None,
        update_retention_policy_shrink: str = None,
    ):
        # Add column
        self.add_column_shrink = add_column_shrink
        # Data catalog to which it belongs
        self.catalog = catalog
        # Idempotency token
        self.client_token = client_token
        # Delete column
        self.delete_column_shrink = delete_column_shrink
        # Table name
        # 
        # This parameter is required.
        self.name = name
        # Namespace to which it belongs
        self.namespace = namespace
        # Rename column
        self.rename_column_shrink = rename_column_shrink
        # Update column comment
        self.update_column_comment_shrink = update_column_comment_shrink
        # Update column type
        self.update_column_type_shrink = update_column_type_shrink
        # Update table comment
        self.update_comment = update_comment
        # Update retention policy
        self.update_retention_policy_shrink = update_retention_policy_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_column_shrink is not None:
            result['AddColumn'] = self.add_column_shrink

        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.delete_column_shrink is not None:
            result['DeleteColumn'] = self.delete_column_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.rename_column_shrink is not None:
            result['RenameColumn'] = self.rename_column_shrink

        if self.update_column_comment_shrink is not None:
            result['UpdateColumnComment'] = self.update_column_comment_shrink

        if self.update_column_type_shrink is not None:
            result['UpdateColumnType'] = self.update_column_type_shrink

        if self.update_comment is not None:
            result['UpdateComment'] = self.update_comment

        if self.update_retention_policy_shrink is not None:
            result['UpdateRetentionPolicy'] = self.update_retention_policy_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddColumn') is not None:
            self.add_column_shrink = m.get('AddColumn')

        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeleteColumn') is not None:
            self.delete_column_shrink = m.get('DeleteColumn')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RenameColumn') is not None:
            self.rename_column_shrink = m.get('RenameColumn')

        if m.get('UpdateColumnComment') is not None:
            self.update_column_comment_shrink = m.get('UpdateColumnComment')

        if m.get('UpdateColumnType') is not None:
            self.update_column_type_shrink = m.get('UpdateColumnType')

        if m.get('UpdateComment') is not None:
            self.update_comment = m.get('UpdateComment')

        if m.get('UpdateRetentionPolicy') is not None:
            self.update_retention_policy_shrink = m.get('UpdateRetentionPolicy')

        return self

