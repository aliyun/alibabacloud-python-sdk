# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class CreateExperienceDataResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.CreateExperienceDataResponseBodyResult = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.CreateExperienceDataResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class CreateExperienceDataResponseBodyResult(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        created: int = None,
        data_size: int = None,
        data_type: bool = None,
        data_value: str = None,
        id: int = None,
        name: str = None,
        service_type: str = None,
        updated: int = None,
    ):
        # The data content type.
        self.content_type = content_type
        # The creation time.
        self.created = created
        # The data size.
        self.data_size = data_size
        # The data type.
        self.data_type = data_type
        # The data content.
        self.data_value = data_value
        # The data ID.
        self.id = id
        # The data name.
        self.name = name
        # The service type.
        self.service_type = service_type
        # The update time.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.created is not None:
            result['created'] = self.created

        if self.data_size is not None:
            result['dataSize'] = self.data_size

        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.data_value is not None:
            result['dataValue'] = self.data_value

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.service_type is not None:
            result['serviceType'] = self.service_type

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('dataSize') is not None:
            self.data_size = m.get('dataSize')

        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('dataValue') is not None:
            self.data_value = m.get('dataValue')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

