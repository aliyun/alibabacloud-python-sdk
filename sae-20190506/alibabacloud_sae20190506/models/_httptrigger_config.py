# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class HTTPTriggerConfig(DaraModel):
    def __init__(
        self,
        acl_config: main_models.AclConfig = None,
        auth_config: Any = None,
        auth_type: str = None,
        disable_urlinternet: bool = None,
        safe_mode: bool = None,
    ):
        self.acl_config = acl_config
        self.auth_config = auth_config
        self.auth_type = auth_type
        self.disable_urlinternet = disable_urlinternet
        self.safe_mode = safe_mode

    def validate(self):
        if self.acl_config:
            self.acl_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_config is not None:
            result['aclConfig'] = self.acl_config.to_map()

        if self.auth_config is not None:
            result['authConfig'] = self.auth_config

        if self.auth_type is not None:
            result['authType'] = self.auth_type

        if self.disable_urlinternet is not None:
            result['disableURLInternet'] = self.disable_urlinternet

        if self.safe_mode is not None:
            result['safeMode'] = self.safe_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aclConfig') is not None:
            temp_model = main_models.AclConfig()
            self.acl_config = temp_model.from_map(m.get('aclConfig'))

        if m.get('authConfig') is not None:
            self.auth_config = m.get('authConfig')

        if m.get('authType') is not None:
            self.auth_type = m.get('authType')

        if m.get('disableURLInternet') is not None:
            self.disable_urlinternet = m.get('disableURLInternet')

        if m.get('safeMode') is not None:
            self.safe_mode = m.get('safeMode')

        return self

