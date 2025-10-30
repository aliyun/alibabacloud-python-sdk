# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeExternalDataServiceResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        request_id: str = None,
        service_description: str = None,
        service_id: str = None,
        service_name: str = None,
        service_spec: str = None,
        status: str = None,
    ):
        # The time when the service was created.
        self.create_time = create_time
        # The time when the service was last modified.
        self.modify_time = modify_time
        # The request ID.
        self.request_id = request_id
        # The description of the service.
        self.service_description = service_description
        # The service ID.
        self.service_id = service_id
        # The name of the service.
        self.service_name = service_name
        # The specifications of the service. Unit: compute units (CUs).
        self.service_spec = service_spec
        # The status of the operation.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_spec is not None:
            result['ServiceSpec'] = self.service_spec

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceSpec') is not None:
            self.service_spec = m.get('ServiceSpec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

