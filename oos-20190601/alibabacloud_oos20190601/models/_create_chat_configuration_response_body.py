# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class CreateChatConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        chat_configuration: main_models.CreateChatConfigurationResponseBodyChatConfiguration = None,
        request_id: str = None,
    ):
        self.chat_configuration = chat_configuration
        self.request_id = request_id

    def validate(self):
        if self.chat_configuration:
            self.chat_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_configuration is not None:
            result['ChatConfiguration'] = self.chat_configuration.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatConfiguration') is not None:
            temp_model = main_models.CreateChatConfigurationResponseBodyChatConfiguration()
            self.chat_configuration = temp_model.from_map(m.get('ChatConfiguration'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateChatConfigurationResponseBodyChatConfiguration(DaraModel):
    def __init__(
        self,
        created_date: str = None,
        name: str = None,
        updated_date: str = None,
    ):
        self.created_date = created_date
        self.name = name
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

        if self.name is not None:
            result['Name'] = self.name

        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')

        return self

