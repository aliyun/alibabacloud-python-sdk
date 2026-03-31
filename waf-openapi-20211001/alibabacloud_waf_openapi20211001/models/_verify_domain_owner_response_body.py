# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class VerifyDomainOwnerResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        verify_result: main_models.VerifyDomainOwnerResponseBodyVerifyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The verification result.
        self.verify_result = verify_result

    def validate(self):
        if self.verify_result:
            self.verify_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VerifyResult') is not None:
            temp_model = main_models.VerifyDomainOwnerResponseBodyVerifyResult()
            self.verify_result = temp_model.from_map(m.get('VerifyResult'))

        return self

class VerifyDomainOwnerResponseBodyVerifyResult(DaraModel):
    def __init__(
        self,
        fail_code: str = None,
        result: bool = None,
    ):
        # The reasons why the verification fails. Valid values:
        # 
        # *   DnsTxtVerifyFailed: The DNS TXT record and the domain name do not match.
        # *   DnsServerError: The DNS server is abnormal.
        # *   VerifyFileNotExist: The verification file does not exist.
        # *   VerifyDomainNotAccess: The access to the domain name failed.
        # *   FileContentVerifyFailed: The content of the verification file and the domain name do not match.
        self.fail_code = fail_code
        # The verification result. Valid values:
        # 
        # *   **true**: The verification succeeds.
        # *   **false**: The verification fails.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_code is not None:
            result['FailCode'] = self.fail_code

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailCode') is not None:
            self.fail_code = m.get('FailCode')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

