# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class GetSavedQueryResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        saved_query: main_models.GetSavedQueryResponseBodySavedQuery = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the template.
        self.saved_query = saved_query

    def validate(self):
        if self.saved_query:
            self.saved_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.saved_query is not None:
            result['SavedQuery'] = self.saved_query.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SavedQuery') is not None:
            temp_model = main_models.GetSavedQueryResponseBodySavedQuery()
            self.saved_query = temp_model.from_map(m.get('SavedQuery'))

        return self

class GetSavedQueryResponseBodySavedQuery(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        expression: str = None,
        name: str = None,
        query_id: str = None,
        update_time: str = None,
    ):
        # The time when the template was created. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the template.
        self.description = description
        # The expression of the template.
        self.expression = expression
        # The name of the template.
        self.name = name
        # The ID of the template.
        self.query_id = query_id
        # The time when the template was last updated. The time is displayed in UTC.
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

        if self.description is not None:
            result['Description'] = self.description

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.name is not None:
            result['Name'] = self.name

        if self.query_id is not None:
            result['QueryId'] = self.query_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

