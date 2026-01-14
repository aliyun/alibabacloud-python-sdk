# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class CreateSentinelBlockFallbackDefinitionResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.CreateSentinelBlockFallbackDefinitionResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CreateSentinelBlockFallbackDefinitionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateSentinelBlockFallbackDefinitionResponseBodyData(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        fallback_behavior: str = None,
        id: int = None,
        name: str = None,
        namespace: str = None,
        resource_classification: int = None,
        user_id: str = None,
    ):
        self.app_name = app_name
        self.fallback_behavior = fallback_behavior
        self.id = id
        self.name = name
        self.namespace = namespace
        self.resource_classification = resource_classification
        self.user_id = user_id

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

        if self.user_id is not None:
            result['UserId'] = self.user_id

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

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

