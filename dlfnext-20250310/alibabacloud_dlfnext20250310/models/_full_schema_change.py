# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class FullSchemaChange(DaraModel):
    def __init__(
        self,
        action: str = None,
        comment: str = None,
        data_type: main_models.FullDataType = None,
        field_names: List[str] = None,
        keep_nullability: bool = None,
        key: str = None,
        move: main_models.Move = None,
        new_comment: str = None,
        new_data_type: main_models.FullDataType = None,
        new_name: str = None,
        new_nullability: bool = None,
        value: str = None,
    ):
        self.action = action
        # required in UpdateComment/AddColumn
        self.comment = comment
        self.data_type = data_type
        # required in AddColumn/RenameColumn/DropColumn/UpdateColumnComment/UpdateColumnType/UpdateColumnNullability
        self.field_names = field_names
        # required in UpdateColumnType
        self.keep_nullability = keep_nullability
        # required in SetOption/RemoveOption
        self.key = key
        self.move = move
        # required in UpdateColumnComment
        self.new_comment = new_comment
        self.new_data_type = new_data_type
        # required in RenameColumn
        self.new_name = new_name
        # required in UpdateColumnNullability
        self.new_nullability = new_nullability
        # required in SetOption
        self.value = value

    def validate(self):
        if self.data_type:
            self.data_type.validate()
        if self.move:
            self.move.validate()
        if self.new_data_type:
            self.new_data_type.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.comment is not None:
            result['comment'] = self.comment

        if self.data_type is not None:
            result['dataType'] = self.data_type.to_map()

        if self.field_names is not None:
            result['fieldNames'] = self.field_names

        if self.keep_nullability is not None:
            result['keepNullability'] = self.keep_nullability

        if self.key is not None:
            result['key'] = self.key

        if self.move is not None:
            result['move'] = self.move.to_map()

        if self.new_comment is not None:
            result['newComment'] = self.new_comment

        if self.new_data_type is not None:
            result['newDataType'] = self.new_data_type.to_map()

        if self.new_name is not None:
            result['newName'] = self.new_name

        if self.new_nullability is not None:
            result['newNullability'] = self.new_nullability

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('dataType') is not None:
            temp_model = main_models.FullDataType()
            self.data_type = temp_model.from_map(m.get('dataType'))

        if m.get('fieldNames') is not None:
            self.field_names = m.get('fieldNames')

        if m.get('keepNullability') is not None:
            self.keep_nullability = m.get('keepNullability')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('move') is not None:
            temp_model = main_models.Move()
            self.move = temp_model.from_map(m.get('move'))

        if m.get('newComment') is not None:
            self.new_comment = m.get('newComment')

        if m.get('newDataType') is not None:
            temp_model = main_models.FullDataType()
            self.new_data_type = temp_model.from_map(m.get('newDataType'))

        if m.get('newName') is not None:
            self.new_name = m.get('newName')

        if m.get('newNullability') is not None:
            self.new_nullability = m.get('newNullability')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

