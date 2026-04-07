# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMetaTableRequest(DaraModel):
    def __init__(
        self,
        added_labels: str = None,
        caption: str = None,
        category_id: int = None,
        env_type: int = None,
        new_owner_id: str = None,
        project_id: int = None,
        removed_labels: str = None,
        schema: str = None,
        table_guid: str = None,
        table_name: str = None,
        visibility: int = None,
    ):
        # The names of the labels that you want to add. Separate the labels with commas (,).
        self.added_labels = added_labels
        # The display name of the table.
        self.caption = caption
        # The ID of the category that you want to associate.
        self.category_id = category_id
        # The environment of the DataWorks workspace. Valid values: 0 and 1. The value 0 indicates the development environment. The value 1 indicates the production environment.
        self.env_type = env_type
        # The new owner ID. If you leave this parameter empty, the owner ID is not updated.
        self.new_owner_id = new_owner_id
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The names of labels that you want to remove. Separate the labels with commas (,).
        self.removed_labels = removed_labels
        # The schema information about the table. You must configure this parameter if you enable the three-layer model of MaxCompute.
        self.schema = schema
        # The GUID of the table. Specify the GUID in the format of odps.{projectName}.{tableName}.
        self.table_guid = table_guid
        # The name of the table.
        self.table_name = table_name
        # The scope in which the table is visible. Valid values: 0, 1, and 2. The value 0 indicates that the table is invisible to all members. The value 1 indicates that the table is visible to all members. The value 2 indicates that the table is visible to workspace members.
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.added_labels is not None:
            result['AddedLabels'] = self.added_labels

        if self.caption is not None:
            result['Caption'] = self.caption

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.new_owner_id is not None:
            result['NewOwnerId'] = self.new_owner_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.removed_labels is not None:
            result['RemovedLabels'] = self.removed_labels

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddedLabels') is not None:
            self.added_labels = m.get('AddedLabels')

        if m.get('Caption') is not None:
            self.caption = m.get('Caption')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('NewOwnerId') is not None:
            self.new_owner_id = m.get('NewOwnerId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RemovedLabels') is not None:
            self.removed_labels = m.get('RemovedLabels')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

