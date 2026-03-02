# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_amqp20190901 import models as main_models
from darabonba.model import DaraModel

class MetadataResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.MetadataResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = main_models.MetadataResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class MetadataResponseBodyData(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        has_pretend_permission: bool = None,
        internal_endpoint: str = None,
        pretend_user_id: str = None,
        user_status: int = None,
    ):
        self.endpoint = endpoint
        self.has_pretend_permission = has_pretend_permission
        self.internal_endpoint = internal_endpoint
        self.pretend_user_id = pretend_user_id
        self.user_status = user_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.has_pretend_permission is not None:
            result['HasPretendPermission'] = self.has_pretend_permission

        if self.internal_endpoint is not None:
            result['InternalEndpoint'] = self.internal_endpoint

        if self.pretend_user_id is not None:
            result['PretendUserId'] = self.pretend_user_id

        if self.user_status is not None:
            result['UserStatus'] = self.user_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('HasPretendPermission') is not None:
            self.has_pretend_permission = m.get('HasPretendPermission')

        if m.get('InternalEndpoint') is not None:
            self.internal_endpoint = m.get('InternalEndpoint')

        if m.get('PretendUserId') is not None:
            self.pretend_user_id = m.get('PretendUserId')

        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')

        return self

