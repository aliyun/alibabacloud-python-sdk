# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListSentinelBlockFallbackDefinitionsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListSentinelBlockFallbackDefinitionsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the data.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListSentinelBlockFallbackDefinitionsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListSentinelBlockFallbackDefinitionsResponseBodyData(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        fallback_behavior: Dict[str, Any] = None,
        id: str = None,
        name: str = None,
        namespace: str = None,
        resource_classification: str = None,
        target_map: Dict[str, Any] = None,
    ):
        # The name of the application.
        self.app_name = app_name
        # Behavior  detail.
        self.fallback_behavior = fallback_behavior
        # Behavior Id
        self.id = id
        # The name of the behavior.
        self.name = name
        # The name of the Microservices namespace.
        self.namespace = namespace
        # Behavior classification.
        self.resource_classification = resource_classification
        # Resource information bound to the behavior.
        self.target_map = target_map

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.fallback_behavior is not None:
            result['FallbackBehavior'] = self.fallback_behavior

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.resource_classification is not None:
            result['ResourceClassification'] = self.resource_classification

        if self.target_map is not None:
            result['TargetMap'] = self.target_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('FallbackBehavior') is not None:
            self.fallback_behavior = m.get('FallbackBehavior')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('ResourceClassification') is not None:
            self.resource_classification = m.get('ResourceClassification')

        if m.get('TargetMap') is not None:
            self.target_map = m.get('TargetMap')

        return self

