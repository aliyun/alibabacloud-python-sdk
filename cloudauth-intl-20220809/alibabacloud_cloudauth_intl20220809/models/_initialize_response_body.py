# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class InitializeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.InitializeResponseBodyResult = None,
    ):
        # Return code
        self.code = code
        # Return message
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Return result
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.InitializeResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class InitializeResponseBodyResult(DaraModel):
    def __init__(
        self,
        client_cfg: str = None,
        protocol: str = None,
        transaction_id: str = None,
        transaction_url: str = None,
    ):
        # Client configuration
        self.client_cfg = client_cfg
        # Standard encryption protocol for authentication.
        # 
        # > This field is required when integrating with H5 web pages using iframe embedding.
        self.protocol = protocol
        # Authentication ID
        self.transaction_id = transaction_id
        # Web authentication URL
        self.transaction_url = transaction_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_cfg is not None:
            result['ClientCfg'] = self.client_cfg

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id

        if self.transaction_url is not None:
            result['TransactionUrl'] = self.transaction_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientCfg') is not None:
            self.client_cfg = m.get('ClientCfg')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')

        if m.get('TransactionUrl') is not None:
            self.transaction_url = m.get('TransactionUrl')

        return self

