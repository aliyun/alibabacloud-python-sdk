# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class CreateApplicationResponseBody(DaraModel):
    def __init__(
        self,
        application: main_models.CreateApplicationResponseBodyApplication = None,
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
            temp_model = main_models.CreateApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m.get('Application'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateApplicationResponseBodyApplication(DaraModel):
    def __init__(
        self,
        create_date: str = None,
        description: str = None,
        name: str = None,
        tags: Dict[str, str] = None,
        update_date: str = None,
    ):
        # The time when the application was created.
        self.create_date = create_date
        # The description of the application.
        self.description = description
        # The application name.
        self.name = name
        # The tags.
        self.tags = tags
        # The time when the application was updated.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

