# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class ListServicesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListServicesResponseBodyResult] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The task execution result.
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.ListServicesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListServicesResponseBodyResult(DaraModel):
    def __init__(
        self,
        charge_way: List[str] = None,
        description: str = None,
        meta: Dict[str, Any] = None,
        model_type: str = None,
        name: str = None,
        service_id: str = None,
        service_type: str = None,
    ):
        # The billing method.
        self.charge_way = charge_way
        # The description.
        self.description = description
        # The metadata.
        self.meta = meta
        # The model type.
        self.model_type = model_type
        # The service name.
        self.name = name
        # The service ID.
        self.service_id = service_id
        # The service type.
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_way is not None:
            result['chargeWay'] = self.charge_way

        if self.description is not None:
            result['description'] = self.description

        if self.meta is not None:
            result['meta'] = self.meta

        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.name is not None:
            result['name'] = self.name

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.service_type is not None:
            result['serviceType'] = self.service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeWay') is not None:
            self.charge_way = m.get('chargeWay')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('meta') is not None:
            self.meta = m.get('meta')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')

        return self

