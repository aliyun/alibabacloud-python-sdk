# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class DeleteAirflowResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        root: main_models.DeleteAirflowResponseBodyRoot = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.root = root
        self.success = success

    def validate(self):
        if self.root:
            self.root.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root is not None:
            result['Root'] = self.root.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Root') is not None:
            temp_model = main_models.DeleteAirflowResponseBodyRoot()
            self.root = temp_model.from_map(m.get('Root'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DeleteAirflowResponseBodyRoot(DaraModel):
    def __init__(
        self,
        responses: List[main_models.DeleteAirflowResponseBodyRootResponses] = None,
    ):
        self.responses = responses

    def validate(self):
        if self.responses:
            for v1 in self.responses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Responses'] = []
        if self.responses is not None:
            for k1 in self.responses:
                result['Responses'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.responses = []
        if m.get('Responses') is not None:
            for k1 in m.get('Responses'):
                temp_model = main_models.DeleteAirflowResponseBodyRootResponses()
                self.responses.append(temp_model.from_map(k1))

        return self

class DeleteAirflowResponseBodyRootResponses(DaraModel):
    def __init__(
        self,
        success: bool = None,
        uuid: str = None,
    ):
        self.success = success
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.success is not None:
            result['Success'] = self.success

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

