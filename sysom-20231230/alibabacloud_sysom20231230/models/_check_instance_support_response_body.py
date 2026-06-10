# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class CheckInstanceSupportResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.CheckInstanceSupportResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # Status code  
        # - `code == Success` indicates that authorization succeeded.  
        # - Other status codes indicate that authorization failed. When authorization fails, view the `message` field to obtain detailed error information.
        self.code = code
        # Returned data.
        self.data = data
        # Error message. When code != Success, the error message is stored here.
        self.message = message
        # Id of the request
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.CheckInstanceSupportResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class CheckInstanceSupportResponseBodyData(DaraModel):
    def __init__(
        self,
        instance: str = None,
        reason: str = None,
        support: bool = None,
    ):
        # ECS instance ID
        self.instance = instance
        # When `success` is false, this value is not empty and indicates the reason why the instance cannot be managed by SysOM.
        self.reason = reason
        # Indicates whether the instance can be managed by SysOM.  
        # 
        # - **true**: The instance can be managed by SysOM.  
        # 
        # - **false**: The instance cannot be managed by SysOM.
        self.support = support

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance is not None:
            result['instance'] = self.instance

        if self.reason is not None:
            result['reason'] = self.reason

        if self.support is not None:
            result['support'] = self.support

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('support') is not None:
            self.support = m.get('support')

        return self

