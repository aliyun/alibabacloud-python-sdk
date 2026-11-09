# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_onsmqtt20200420 import models as main_models
from darabonba.model import DaraModel

class QueryCustomAuthIdentityResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.QueryCustomAuthIdentityResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. 200: The request is successful. Other codes indicate errors. For more information about error codes, see Error codes.
        self.code = code
        # The query result.
        self.data = data
        # The additional information.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request is successful. true: The request is successful. false: The request failed.
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
            temp_model = main_models.QueryCustomAuthIdentityResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryCustomAuthIdentityResponseBodyData(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        results: List[main_models.QueryCustomAuthIdentityResponseBodyDataResults] = None,
    ):
        # If more results are available, a NextToken is returned.
        self.next_token = next_token
        # The returned data.
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
                temp_model = main_models.QueryCustomAuthIdentityResponseBodyDataResults()
                self.results.append(temp_model.from_map(k1))

        return self

class QueryCustomAuthIdentityResponseBodyDataResults(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        identity_type: str = None,
        secret: str = None,
        sign_mode: str = None,
        username: str = None,
    ):
        # The client ID of the device when the identity type is CLIENT.
        self.client_id = client_id
        # The identity type.
        # 
        # - USER: Username only.
        # 
        # - CLIENT: Specific to a client.
        self.identity_type = identity_type
        # The secret key.
        self.secret = secret
        # The signature verification mode. ORIGIN: Original value comparison, which compares the password with the secret. SIGNED: The HmacSHA1 signature is calculated for the clientId using the secret for verification, and then the password is compared.
        self.sign_mode = sign_mode
        # The username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type

        if self.secret is not None:
            result['Secret'] = self.secret

        if self.sign_mode is not None:
            result['SignMode'] = self.sign_mode

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')

        if m.get('Secret') is not None:
            self.secret = m.get('Secret')

        if m.get('SignMode') is not None:
            self.sign_mode = m.get('SignMode')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

