# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class CreateLangfuseOrgResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateLangfuseOrgResponseBodyData = None,
        request_id: str = None,
    ):
        # The response data.
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
            temp_model = main_models.CreateLangfuseOrgResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateLangfuseOrgResponseBodyData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        name: str = None,
        organization_id: str = None,
    ):
        # The time when the Langfuse organization was created.
        self.created_at = created_at
        # The name of the Langfuse organization.
        self.name = name
        # The Langfuse organization ID.
        self.organization_id = organization_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        return self

