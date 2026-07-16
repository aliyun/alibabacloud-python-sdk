# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class EnableServicesResponseBody(DaraModel):
    def __init__(
        self,
        failed_services: List[main_models.EnableServicesResponseBodyFailedServices] = None,
        request_id: str = None,
    ):
        self.failed_services = failed_services
        self.request_id = request_id

    def validate(self):
        if self.failed_services:
            for v1 in self.failed_services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailedServices'] = []
        if self.failed_services is not None:
            for k1 in self.failed_services:
                result['FailedServices'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_services = []
        if m.get('FailedServices') is not None:
            for k1 in m.get('FailedServices'):
                temp_model = main_models.EnableServicesResponseBodyFailedServices()
                self.failed_services.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class EnableServicesResponseBodyFailedServices(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        service_name: str = None,
    ):
        self.code = code
        self.message = message
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

