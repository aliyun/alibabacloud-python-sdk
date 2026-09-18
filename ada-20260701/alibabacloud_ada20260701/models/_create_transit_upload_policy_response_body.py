# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ada20260701 import models as main_models
from darabonba.model import DaraModel

class CreateTransitUploadPolicyResponseBody(DaraModel):
    def __init__(
        self,
        file_path: str = None,
        policy_info: main_models.CreateTransitUploadPolicyResponseBodyPolicyInfo = None,
        request_id: str = None,
        success: bool = None,
        transit_id: str = None,
    ):
        # The object storage key, which is also the `key` field in the PostObject form.
        self.file_path = file_path
        # The upload policy object. For the complete list of subfields, see the following table.
        self.policy_info = policy_info
        # The request ID, used for Tracing Analysis and troubleshooting.
        self.request_id = request_id
        # Indicates whether the upload policy is generated. A successful response always returns `true`. An error response is returned upon failure.
        self.success = success
        # The ID of the newly created Transit record, used for subsequent queries and storage operations.
        self.transit_id = transit_id

    def validate(self):
        if self.policy_info:
            self.policy_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.policy_info is not None:
            result['PolicyInfo'] = self.policy_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.transit_id is not None:
            result['TransitId'] = self.transit_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('PolicyInfo') is not None:
            temp_model = main_models.CreateTransitUploadPolicyResponseBodyPolicyInfo()
            self.policy_info = temp_model.from_map(m.get('PolicyInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TransitId') is not None:
            self.transit_id = m.get('TransitId')

        return self



class CreateTransitUploadPolicyResponseBodyPolicyInfo(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        dir: str = None,
        host: str = None,
        policy: str = None,
        security_token: str = None,
        signature: str = None,
    ):
        # The `OSSAccessKeyId` field in the PostObject form. Protect this value together with the entire `PolicyInfo`.
        self.access_id = access_id
        # The object storage key. The value is the same as the top-level `FilePath`.
        self.dir = dir
        # The target URL to which the client sends the PostObject request.
        self.host = host
        # The Base64-encoded PostObject upload policy. Protect this value together with the entire `PolicyInfo`.
        self.policy = policy
        # The `x-oss-security-token` field in the PostObject form when STS credentials are used. This field may be empty when STS is not used. This field contains sensitive authorization information.
        self.security_token = security_token
        # The signature field in the PostObject form. This field contains sensitive authorization information.
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['AccessId'] = self.access_id

        if self.dir is not None:
            result['Dir'] = self.dir

        if self.host is not None:
            result['Host'] = self.host

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.signature is not None:
            result['Signature'] = self.signature

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')

        if m.get('Dir') is not None:
            self.dir = m.get('Dir')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        return self

