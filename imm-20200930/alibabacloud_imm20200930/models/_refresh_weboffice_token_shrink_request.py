# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshWebofficeTokenShrinkRequest(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        credential_config_shrink: str = None,
        project_name: str = None,
        refresh_token: str = None,
    ):
        # Weboffice access token. Obtain it through the [GenerateWebofficeToken](https://help.aliyun.com/document_detail/478226.html) or [RefreshWebofficeToken](https://help.aliyun.com/document_detail/478227.html) interfaces.
        # 
        # This parameter is required.
        self.access_token = access_token
        # **If there are no special requirements, leave it blank.**
        # 
        # Chained authorization configuration, optional. For more information, see [Access Other Entity Resources Using Chained Authorization](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # Project name. For more information on how to obtain it, see [Create Project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # Weboffice refresh token. Obtain it through the [GenerateWebofficeToken](https://help.aliyun.com/document_detail/478226.html) or [RefreshWebofficeToken](https://help.aliyun.com/document_detail/478227.html) interfaces.
        # 
        # This parameter is required.
        self.refresh_token = refresh_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token is not None:
            result['AccessToken'] = self.access_token

        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')

        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')

        return self

