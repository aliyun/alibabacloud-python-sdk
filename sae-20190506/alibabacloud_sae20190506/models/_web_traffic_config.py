# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class WebTrafficConfig(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        disable_internet_url: bool = None,
        revisions_traffic_weight: Dict[str, float] = None,
        web_acl_config: main_models.WebAclConfig = None,
    ):
        # The authentication type. Valid values:
        # 
        # *   **Anonymous**: does not require authentication.
        # *   **Application**: requires authentication.
        # 
        # >  The default value is **Anonymous**.
        self.auth_type = auth_type
        # Specifies whether to disable access to the default Internet domain. If you set this parameter to true, a 403 error is returned if you access the default public URL provided by the function. A value of false does not have affect the running of the function.
        self.disable_internet_url = disable_internet_url
        # Specifies the traffic weight of applications in different versions. The sum of traffic weight for all versions must be 100%.
        self.revisions_traffic_weight = revisions_traffic_weight
        # The configurations of IP ACL whitelist.
        self.web_acl_config = web_acl_config

    def validate(self):
        if self.web_acl_config:
            self.web_acl_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.disable_internet_url is not None:
            result['DisableInternetURL'] = self.disable_internet_url

        if self.revisions_traffic_weight is not None:
            result['RevisionsTrafficWeight'] = self.revisions_traffic_weight

        if self.web_acl_config is not None:
            result['WebAclConfig'] = self.web_acl_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('DisableInternetURL') is not None:
            self.disable_internet_url = m.get('DisableInternetURL')

        if m.get('RevisionsTrafficWeight') is not None:
            self.revisions_traffic_weight = m.get('RevisionsTrafficWeight')

        if m.get('WebAclConfig') is not None:
            temp_model = main_models.WebAclConfig()
            self.web_acl_config = temp_model.from_map(m.get('WebAclConfig'))

        return self

