# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FraudResultCallBackRequest(DaraModel):
    def __init__(
        self,
        certify_id: str = None,
        ext_params: str = None,
        result_code: str = None,
        verify_deploy_env: str = None,
    ):
        # The unique identifier for identity verification, which corresponds to the verifyId of Ant.
        self.certify_id = certify_id
        # The extended parameters, in JSON string format.
        self.ext_params = ext_params
        # Indicates whether the anti-spoofing check is passed. Valid values:
        # - PASS: Passed.
        # - REJECT: Not passed.
        self.result_code = result_code
        # The environment routing parameter. Valid values:
        # - staging: staging environment
        # - production: production environment.
        self.verify_deploy_env = verify_deploy_env

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id

        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.verify_deploy_env is not None:
            result['VerifyDeployEnv'] = self.verify_deploy_env

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('VerifyDeployEnv') is not None:
            self.verify_deploy_env = m.get('VerifyDeployEnv')

        return self

