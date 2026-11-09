# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_onsmqtt20200420 import models as main_models
from darabonba.model import DaraModel

class QueryCustomAuthPermissionResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.QueryCustomAuthPermissionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
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
            temp_model = main_models.QueryCustomAuthPermissionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryCustomAuthPermissionResponseBodyData(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        results: List[main_models.QueryCustomAuthPermissionResponseBodyDataResults] = None,
    ):
        # The token that marks the end position of the previous returned page. To obtain the next batch of data, call the operation again by using the value of NextToken returned by the previous request. If you call this operation for the first time or want to query all results, set NextToken to an empty string.
        self.next_token = next_token
        # The response results.
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.QueryCustomAuthPermissionResponseBodyDataResults()
                self.results.append(temp_model.from_map(k1))

        return self

class QueryCustomAuthPermissionResponseBodyDataResults(DaraModel):
    def __init__(
        self,
        effect: str = None,
        identity: str = None,
        identity_type: str = None,
        permit_action: str = None,
        topic: str = None,
    ):
        # Indicates whether to allow or deny access.
        self.effect = effect
        # The username or client ID.
        self.identity = identity
        # The identity type. Valid values:
        # 
        # *   USER
        # *   CLIENT
        self.identity_type = identity_type
        # The authorized permissions.
        self.permit_action = permit_action
        # The topic name. Multi-level topics and wildcard characters are supported.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effect is not None:
            result['Effect'] = self.effect

        if self.identity is not None:
            result['Identity'] = self.identity

        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type

        if self.permit_action is not None:
            result['PermitAction'] = self.permit_action

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Effect') is not None:
            self.effect = m.get('Effect')

        if m.get('Identity') is not None:
            self.identity = m.get('Identity')

        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')

        if m.get('PermitAction') is not None:
            self.permit_action = m.get('PermitAction')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

