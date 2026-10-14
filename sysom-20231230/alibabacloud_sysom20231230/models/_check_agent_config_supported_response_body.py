# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class CheckAgentConfigSupportedResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.CheckAgentConfigSupportedResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        total: int = None,
    ):
        # The status code.
        # - If `code` is `Success`, the authorization is successful.
        # - Other status codes indicate that the authorization failed. If the authorization failed, check the `message` field for the detailed fault information.
        self.code = code
        # The returned result.
        self.data = data
        # The error message.
        # - If code is Success, this field is empty.
        # - Otherwise, this field contains the error information of the request.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The total number of returned results.
        self.total = total

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
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.CheckAgentConfigSupportedResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class CheckAgentConfigSupportedResponseBodyData(DaraModel):
    def __init__(
        self,
        cluster: str = None,
        instance: str = None,
        reason: str = None,
    ):
        # The cluster ID.
        self.cluster = cluster
        # The ECS instance ID.
        self.instance = instance
        # The reason why the instance is not supported for management. This field is not empty when success is false.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster is not None:
            result['cluster'] = self.cluster

        if self.instance is not None:
            result['instance'] = self.instance

        if self.reason is not None:
            result['reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        return self

