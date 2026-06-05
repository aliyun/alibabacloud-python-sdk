# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class DeleteWorkspaceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        fail_reasons: List[main_models.DeleteWorkspaceResponseBodyFailReasons] = None,
        http_status_code: int = None,
        is_deleted: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.fail_reasons = fail_reasons
        self.http_status_code = http_status_code
        self.is_deleted = is_deleted
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.fail_reasons:
            for v1 in self.fail_reasons:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['failReasons'] = []
        if self.fail_reasons is not None:
            for k1 in self.fail_reasons:
                result['failReasons'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.is_deleted is not None:
            result['isDeleted'] = self.is_deleted

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.fail_reasons = []
        if m.get('failReasons') is not None:
            for k1 in m.get('failReasons'):
                temp_model = main_models.DeleteWorkspaceResponseBodyFailReasons()
                self.fail_reasons.append(temp_model.from_map(k1))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('isDeleted') is not None:
            self.is_deleted = m.get('isDeleted')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class DeleteWorkspaceResponseBodyFailReasons(DaraModel):
    def __init__(
        self,
        reason: str = None,
        resource_type: str = None,
    ):
        self.reason = reason
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason is not None:
            result['reason'] = self.reason

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

