# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DatabaseSummaryModel(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        created_by_source: str = None,
        created_by_user: str = None,
        db_type: str = None,
        description: str = None,
        location: str = None,
        owner: str = None,
        schema_name: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.created_by_source = created_by_source
        self.created_by_user = created_by_user
        self.db_type = db_type
        self.description = description
        self.location = location
        self.owner = owner
        self.schema_name = schema_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.created_by_source is not None:
            result['CreatedBySource'] = self.created_by_source

        if self.created_by_user is not None:
            result['CreatedByUser'] = self.created_by_user

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.description is not None:
            result['Description'] = self.description

        if self.location is not None:
            result['Location'] = self.location

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatedBySource') is not None:
            self.created_by_source = m.get('CreatedBySource')

        if m.get('CreatedByUser') is not None:
            self.created_by_user = m.get('CreatedByUser')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

