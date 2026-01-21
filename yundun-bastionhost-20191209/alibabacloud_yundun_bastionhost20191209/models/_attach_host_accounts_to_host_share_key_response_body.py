# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class AttachHostAccountsToHostShareKeyResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[main_models.AttachHostAccountsToHostShareKeyResponseBodyResults] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The result of the call.
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.AttachHostAccountsToHostShareKeyResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self

class AttachHostAccountsToHostShareKeyResponseBodyResults(DaraModel):
    def __init__(
        self,
        code: str = None,
        host_account_id: str = None,
        host_share_key_id: str = None,
        message: str = None,
    ):
        # The error code returned. If **OK** is returned, the association was successful. If another error code is returned, the association failed.
        self.code = code
        # The ID of the host account.
        self.host_account_id = host_account_id
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id
        # The error message returned.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id

        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')

        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

