# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class UpdateApplicationResponseBody(DaraModel):
    def __init__(
        self,
        application: main_models.UpdateApplicationResponseBodyApplication = None,
        request_id: str = None,
    ):
        # The information about the application.
        self.application = application
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application is not None:
            result['Application'] = self.application.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = main_models.UpdateApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m.get('Application'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateApplicationResponseBodyApplication(DaraModel):
    def __init__(
        self,
        created_date: str = None,
        description: str = None,
        name: str = None,
        resource_group_id: str = None,
        tags: Dict[str, Any] = None,
        updated_date: str = None,
    ):
        # The time when the application was created.
        self.created_date = created_date
        # The description of the application.
        self.description = description
        # The application name.
        self.name = name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tags = tags
        # The time when the application was updated.
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')

        return self

