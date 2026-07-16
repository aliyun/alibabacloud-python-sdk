# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class View(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        created_by: str = None,
        id: str = None,
        name: str = None,
        owner: str = None,
        schema: main_models.ViewSchema = None,
        updated_at: int = None,
        updated_by: str = None,
    ):
        # The creation time.
        self.created_at = created_at
        # The creator.
        self.created_by = created_by
        # The UUID of the view.
        self.id = id
        # The name of the view.
        self.name = name
        # The owner of the view.
        self.owner = owner
        # The view schema.
        self.schema = schema
        # The time of the last update.
        self.updated_at = updated_at
        # The user who last updated the view.
        self.updated_by = updated_by

    def validate(self):
        if self.schema:
            self.schema.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.owner is not None:
            result['owner'] = self.owner

        if self.schema is not None:
            result['schema'] = self.schema.to_map()

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('schema') is not None:
            temp_model = main_models.ViewSchema()
            self.schema = temp_model.from_map(m.get('schema'))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')

        return self

