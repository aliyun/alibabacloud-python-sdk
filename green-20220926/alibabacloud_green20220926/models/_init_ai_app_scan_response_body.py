# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class InitAiAppScanResponseBody(DaraModel):
    def __init__(
        self,
        auth_info: main_models.InitAiAppScanResponseBodyAuthInfo = None,
        auth_info_config: Dict[str, main_models.AuthInfoConfigValue] = None,
        auth_status: str = None,
        open_status: str = None,
        ready_status: str = None,
        request_id: str = None,
    ):
        # The access entry information.
        self.auth_info = auth_info
        # The access information.
        self.auth_info_config = auth_info_config
        # The authorization status.
        self.auth_status = auth_status
        # The service activation status.
        self.open_status = open_status
        # The ready status.
        self.ready_status = ready_status
        # The ID assigned by the backend to uniquely identify a request. You can use this ID for troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.auth_info:
            self.auth_info.validate()
        if self.auth_info_config:
            for v1 in self.auth_info_config.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_info is not None:
            result['AuthInfo'] = self.auth_info.to_map()

        result['AuthInfoConfig'] = {}
        if self.auth_info_config is not None:
            for k1, v1 in self.auth_info_config.items():
                result['AuthInfoConfig'][k1] = v1.to_map() if v1 else None

        if self.auth_status is not None:
            result['AuthStatus'] = self.auth_status

        if self.open_status is not None:
            result['OpenStatus'] = self.open_status

        if self.ready_status is not None:
            result['ReadyStatus'] = self.ready_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthInfo') is not None:
            temp_model = main_models.InitAiAppScanResponseBodyAuthInfo()
            self.auth_info = temp_model.from_map(m.get('AuthInfo'))

        self.auth_info_config = {}
        if m.get('AuthInfoConfig') is not None:
            for k1, v1 in m.get('AuthInfoConfig').items():
                temp_model = main_models.AuthInfoConfigValue()
                self.auth_info_config[k1] = temp_model.from_map(v1)

        if m.get('AuthStatus') is not None:
            self.auth_status = m.get('AuthStatus')

        if m.get('OpenStatus') is not None:
            self.open_status = m.get('OpenStatus')

        if m.get('ReadyStatus') is not None:
            self.ready_status = m.get('ReadyStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class InitAiAppScanResponseBodyAuthInfo(DaraModel):
    def __init__(
        self,
        auth_token: str = None,
        private_domain: str = None,
        project: str = None,
        public_domain: str = None,
    ):
        # The credential.
        self.auth_token = auth_token
        # The private domain name.
        self.private_domain = private_domain
        # The project space.
        self.project = project
        # The public domain name.
        self.public_domain = public_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_token is not None:
            result['AuthToken'] = self.auth_token

        if self.private_domain is not None:
            result['PrivateDomain'] = self.private_domain

        if self.project is not None:
            result['Project'] = self.project

        if self.public_domain is not None:
            result['PublicDomain'] = self.public_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthToken') is not None:
            self.auth_token = m.get('AuthToken')

        if m.get('PrivateDomain') is not None:
            self.private_domain = m.get('PrivateDomain')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('PublicDomain') is not None:
            self.public_domain = m.get('PublicDomain')

        return self

