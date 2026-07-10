# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class CreateLangfuseProjectResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateLangfuseProjectResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.CreateLangfuseProjectResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateLangfuseProjectResponseBodyData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        name: str = None,
        organization_id: str = None,
        project_id: str = None,
    ):
        # The time when the Langfuse project was created.
        self.created_at = created_at
        # The Langfuse project name.
        self.name = name
        # The Langfuse organization ID.
        self.organization_id = organization_id
        # The Langfuse project ID.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.name is not None:
            result['Name'] = self.name

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

