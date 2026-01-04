# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateApplicationInfoRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_name: str = None,
        application_visibility: List[str] = None,
        client_token: str = None,
        instance_id: str = None,
        logo_url: str = None,
    ):
        # IDaaS的应用主键id
        # 
        # This parameter is required.
        self.application_id = application_id
        # 应用的表示名称
        # 
        # This parameter is required.
        self.application_name = application_name
        self.application_visibility = application_visibility
        self.client_token = client_token
        # IDaaS EIAM的实例id
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 应用Logo地址
        self.logo_url = logo_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.application_visibility is not None:
            result['ApplicationVisibility'] = self.application_visibility

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ApplicationVisibility') is not None:
            self.application_visibility = m.get('ApplicationVisibility')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')

        return self

