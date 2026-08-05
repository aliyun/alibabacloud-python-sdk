# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class GetAsyncTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetAsyncTaskResponseBodyResult = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The response result.
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
            temp_model = main_models.GetAsyncTaskResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class GetAsyncTaskResponseBodyResult(DaraModel):
    def __init__(
        self,
        created: int = None,
        data_id: int = None,
        id: str = None,
        name: str = None,
        result: str = None,
        service_id: str = None,
        service_type: str = None,
        status: str = None,
        updated: int = None,
    ):
        # The creation time.
        self.created = created
        # The playground data ID.
        self.data_id = data_id
        # The asynchronous task ID.
        self.id = id
        # The task name.
        self.name = name
        # The parsing result.
        self.result = result
        # The service ID.
        self.service_id = service_id
        # The service type.
        self.service_type = service_type
        # The task status. Valid values:
        # - PENDING: in progress.
        # - SUCCESS: parsing succeeded.
        # - FAILED: parsing failed.
        self.status = status
        # The update time.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created is not None:
            result['created'] = self.created

        if self.data_id is not None:
            result['dataId'] = self.data_id

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.result is not None:
            result['result'] = self.result

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.service_type is not None:
            result['serviceType'] = self.service_type

        if self.status is not None:
            result['status'] = self.status

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('dataId') is not None:
            self.data_id = m.get('dataId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

