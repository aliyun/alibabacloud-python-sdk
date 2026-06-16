# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListApplicationTokensResponseBody(DaraModel):
    def __init__(
        self,
        application_tokens: List[main_models.ListApplicationTokensResponseBodyApplicationTokens] = None,
        request_id: str = None,
    ):
        # The application tokens.
        self.application_tokens = application_tokens
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.application_tokens:
            for v1 in self.application_tokens:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationTokens'] = []
        if self.application_tokens is not None:
            for k1 in self.application_tokens:
                result['ApplicationTokens'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_tokens = []
        if m.get('ApplicationTokens') is not None:
            for k1 in m.get('ApplicationTokens'):
                temp_model = main_models.ListApplicationTokensResponseBodyApplicationTokens()
                self.application_tokens.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListApplicationTokensResponseBodyApplicationTokens(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        application_id: str = None,
        application_token: str = None,
        application_token_id: str = None,
        application_token_type: str = None,
        create_time: int = None,
        description: str = None,
        expiration_time: int = None,
        instance_id: str = None,
        last_used_time: int = None,
        status: str = None,
    ):
        # The Alibaba Cloud account ID.
        self.ali_uid = ali_uid
        # The application ID.
        self.application_id = application_id
        # The application token.
        self.application_token = application_token
        # The ID of the application token.
        self.application_token_id = application_token_id
        # The type of the application token.
        self.application_token_type = application_token_type
        # The creation time.
        self.create_time = create_time
        # The description of the application token.
        self.description = description
        # The expiration time.
        self.expiration_time = expiration_time
        # The ID of the IDaaS EIAM instance.
        self.instance_id = instance_id
        # The last used time.
        self.last_used_time = last_used_time
        # The status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_token is not None:
            result['ApplicationToken'] = self.application_token

        if self.application_token_id is not None:
            result['ApplicationTokenId'] = self.application_token_id

        if self.application_token_type is not None:
            result['ApplicationTokenType'] = self.application_token_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.last_used_time is not None:
            result['LastUsedTime'] = self.last_used_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationToken') is not None:
            self.application_token = m.get('ApplicationToken')

        if m.get('ApplicationTokenId') is not None:
            self.application_token_id = m.get('ApplicationTokenId')

        if m.get('ApplicationTokenType') is not None:
            self.application_token_type = m.get('ApplicationTokenType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LastUsedTime') is not None:
            self.last_used_time = m.get('LastUsedTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

