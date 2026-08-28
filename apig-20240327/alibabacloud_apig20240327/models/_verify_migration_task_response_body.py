# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class VerifyMigrationTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.VerifyMigrationTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.VerifyMigrationTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class VerifyMigrationTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        is_supported: bool = None,
        message: str = None,
        success: bool = None,
        un_supported_route_rules: List[main_models.VerifyMigrationTaskResponseBodyDataUnSupportedRouteRules] = None,
    ):
        self.is_supported = is_supported
        self.message = message
        self.success = success
        self.un_supported_route_rules = un_supported_route_rules

    def validate(self):
        if self.un_supported_route_rules:
            for v1 in self.un_supported_route_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_supported is not None:
            result['isSupported'] = self.is_supported

        if self.message is not None:
            result['message'] = self.message

        if self.success is not None:
            result['success'] = self.success

        result['unSupportedRouteRules'] = []
        if self.un_supported_route_rules is not None:
            for k1 in self.un_supported_route_rules:
                result['unSupportedRouteRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isSupported') is not None:
            self.is_supported = m.get('isSupported')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('success') is not None:
            self.success = m.get('success')

        self.un_supported_route_rules = []
        if m.get('unSupportedRouteRules') is not None:
            for k1 in m.get('unSupportedRouteRules'):
                temp_model = main_models.VerifyMigrationTaskResponseBodyDataUnSupportedRouteRules()
                self.un_supported_route_rules.append(temp_model.from_map(k1))

        return self

class VerifyMigrationTaskResponseBodyDataUnSupportedRouteRules(DaraModel):
    def __init__(
        self,
        name: str = None,
        rule: str = None,
        un_supported_annotations: List[str] = None,
    ):
        self.name = name
        self.rule = rule
        self.un_supported_annotations = un_supported_annotations

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.rule is not None:
            result['rule'] = self.rule

        if self.un_supported_annotations is not None:
            result['unSupportedAnnotations'] = self.un_supported_annotations

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('rule') is not None:
            self.rule = m.get('rule')

        if m.get('unSupportedAnnotations') is not None:
            self.un_supported_annotations = m.get('unSupportedAnnotations')

        return self

