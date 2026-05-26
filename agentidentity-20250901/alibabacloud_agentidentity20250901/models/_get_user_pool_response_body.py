# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class GetUserPoolResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_pool: main_models.GetUserPoolResponseBodyUserPool = None,
    ):
        self.request_id = request_id
        self.user_pool = user_pool

    def validate(self):
        if self.user_pool:
            self.user_pool.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_pool is not None:
            result['UserPool'] = self.user_pool.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserPool') is not None:
            temp_model = main_models.GetUserPoolResponseBodyUserPool()
            self.user_pool = temp_model.from_map(m.get('UserPool'))

        return self

class GetUserPoolResponseBodyUserPool(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        update_time: str = None,
        user_pool_id: str = None,
        user_pool_name: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.update_time = update_time
        self.user_pool_id = user_pool_id
        self.user_pool_name = user_pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_pool_id is not None:
            result['UserPoolId'] = self.user_pool_id

        if self.user_pool_name is not None:
            result['UserPoolName'] = self.user_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserPoolId') is not None:
            self.user_pool_id = m.get('UserPoolId')

        if m.get('UserPoolName') is not None:
            self.user_pool_name = m.get('UserPoolName')

        return self

