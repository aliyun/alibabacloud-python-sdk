# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class UpdateTableRequest(DaraModel):
    def __init__(
        self,
        add_column: main_models.UpdateTableRequestAddColumn = None,
        catalog: str = None,
        client_token: str = None,
        delete_column: main_models.UpdateTableRequestDeleteColumn = None,
        name: str = None,
        namespace: str = None,
        rename_column: main_models.UpdateTableRequestRenameColumn = None,
        update_column_comment: main_models.UpdateTableRequestUpdateColumnComment = None,
        update_column_type: main_models.UpdateTableRequestUpdateColumnType = None,
        update_comment: str = None,
        update_retention_policy: main_models.UpdateTableRequestUpdateRetentionPolicy = None,
    ):
        # Add column
        self.add_column = add_column
        # Data catalog to which it belongs
        self.catalog = catalog
        # Idempotency token
        self.client_token = client_token
        # Delete column
        self.delete_column = delete_column
        # Table name
        # 
        # This parameter is required.
        self.name = name
        # Namespace to which it belongs
        self.namespace = namespace
        # Rename column
        self.rename_column = rename_column
        # Update column comment
        self.update_column_comment = update_column_comment
        # Update column type
        self.update_column_type = update_column_type
        # Update table comment
        self.update_comment = update_comment
        # Update retention policy
        self.update_retention_policy = update_retention_policy

    def validate(self):
        if self.add_column:
            self.add_column.validate()
        if self.delete_column:
            self.delete_column.validate()
        if self.rename_column:
            self.rename_column.validate()
        if self.update_column_comment:
            self.update_column_comment.validate()
        if self.update_column_type:
            self.update_column_type.validate()
        if self.update_retention_policy:
            self.update_retention_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_column is not None:
            result['AddColumn'] = self.add_column.to_map()

        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.delete_column is not None:
            result['DeleteColumn'] = self.delete_column.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.rename_column is not None:
            result['RenameColumn'] = self.rename_column.to_map()

        if self.update_column_comment is not None:
            result['UpdateColumnComment'] = self.update_column_comment.to_map()

        if self.update_column_type is not None:
            result['UpdateColumnType'] = self.update_column_type.to_map()

        if self.update_comment is not None:
            result['UpdateComment'] = self.update_comment

        if self.update_retention_policy is not None:
            result['UpdateRetentionPolicy'] = self.update_retention_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddColumn') is not None:
            temp_model = main_models.UpdateTableRequestAddColumn()
            self.add_column = temp_model.from_map(m.get('AddColumn'))

        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeleteColumn') is not None:
            temp_model = main_models.UpdateTableRequestDeleteColumn()
            self.delete_column = temp_model.from_map(m.get('DeleteColumn'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RenameColumn') is not None:
            temp_model = main_models.UpdateTableRequestRenameColumn()
            self.rename_column = temp_model.from_map(m.get('RenameColumn'))

        if m.get('UpdateColumnComment') is not None:
            temp_model = main_models.UpdateTableRequestUpdateColumnComment()
            self.update_column_comment = temp_model.from_map(m.get('UpdateColumnComment'))

        if m.get('UpdateColumnType') is not None:
            temp_model = main_models.UpdateTableRequestUpdateColumnType()
            self.update_column_type = temp_model.from_map(m.get('UpdateColumnType'))

        if m.get('UpdateComment') is not None:
            self.update_comment = m.get('UpdateComment')

        if m.get('UpdateRetentionPolicy') is not None:
            temp_model = main_models.UpdateTableRequestUpdateRetentionPolicy()
            self.update_retention_policy = temp_model.from_map(m.get('UpdateRetentionPolicy'))

        return self

class UpdateTableRequestUpdateRetentionPolicy(DaraModel):
    def __init__(
        self,
        cold_ttl: int = None,
        hot_ttl: int = None,
    ):
        # Cold storage duration
        self.cold_ttl = cold_ttl
        # Hot storage duration
        self.hot_ttl = hot_ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cold_ttl is not None:
            result['ColdTTL'] = self.cold_ttl

        if self.hot_ttl is not None:
            result['HotTTL'] = self.hot_ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColdTTL') is not None:
            self.cold_ttl = m.get('ColdTTL')

        if m.get('HotTTL') is not None:
            self.hot_ttl = m.get('HotTTL')

        return self

class UpdateTableRequestUpdateColumnType(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # Connector name
        self.name = name
        # Column type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateTableRequestUpdateColumnComment(DaraModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
    ):
        # Comment information.
        self.comment = comment
        # Extended data name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class UpdateTableRequestRenameColumn(DaraModel):
    def __init__(
        self,
        name: str = None,
        new_name: str = None,
    ):
        # Connector name.
        self.name = name
        # The updated name. Enter this when you need to modify the metric name.
        self.new_name = new_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.new_name is not None:
            result['NewName'] = self.new_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NewName') is not None:
            self.new_name = m.get('NewName')

        return self

class UpdateTableRequestDeleteColumn(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # Connector name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class UpdateTableRequestAddColumn(DaraModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
        type: str = None,
    ):
        # Comment.
        self.comment = comment
        # The full name of the queried event type.
        self.name = name
        # The event target type. For more information, see [Event target parameters](https://help.aliyun.com/document_detail/185887.html).
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

