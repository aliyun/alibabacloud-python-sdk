# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class HTTPTriggerConfig(DaraModel):
    def __init__(
        self,
        auth_config: str = None,
        auth_type: str = None,
        cors_config: main_models.CORSConfig = None,
        disable_urlinternet: bool = None,
        methods: List[str] = None,
    ):
        # Authentication configuration
        self.auth_config = auth_config
        # The authentication type. Valid values are:
        # 
        # - **function**: Authentication is required.
        # 
        # - **anonymous**: Authentication is not required.
        # 
        # > The default type is **function**.
        self.auth_type = auth_type
        self.cors_config = cors_config
        # Specifies whether to disable access from the default public domain name. If set to true, accessing the function\\"s default public URL returns a 403 error. If set to false, this parameter has no effect.
        self.disable_urlinternet = disable_urlinternet
        # The list of request methods. Multiple methods are supported.
        self.methods = methods

    def validate(self):
        if self.cors_config:
            self.cors_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config

        if self.auth_type is not None:
            result['authType'] = self.auth_type

        if self.cors_config is not None:
            result['corsConfig'] = self.cors_config.to_map()

        if self.disable_urlinternet is not None:
            result['disableURLInternet'] = self.disable_urlinternet

        if self.methods is not None:
            result['methods'] = self.methods

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authConfig') is not None:
            self.auth_config = m.get('authConfig')

        if m.get('authType') is not None:
            self.auth_type = m.get('authType')

        if m.get('corsConfig') is not None:
            temp_model = main_models.CORSConfig()
            self.cors_config = temp_model.from_map(m.get('corsConfig'))

        if m.get('disableURLInternet') is not None:
            self.disable_urlinternet = m.get('disableURLInternet')

        if m.get('methods') is not None:
            self.methods = m.get('methods')

        return self

