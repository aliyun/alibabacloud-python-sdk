# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class ListServiceContainersResponseBody(DaraModel):
    def __init__(
        self,
        containers: List[main_models.ContainerInfo] = None,
        request_id: str = None,
        service_name: str = None,
    ):
        # The containers of the service.
        self.containers = containers
        # The request ID.
        self.request_id = request_id
        # The service name.
        self.service_name = service_name

    def validate(self):
        if self.containers:
            for v1 in self.containers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Containers'] = []
        if self.containers is not None:
            for k1 in self.containers:
                result['Containers'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.containers = []
        if m.get('Containers') is not None:
            for k1 in m.get('Containers'):
                temp_model = main_models.ContainerInfo()
                self.containers.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

