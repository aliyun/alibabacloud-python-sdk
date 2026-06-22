# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class RefreshWebofficeTokenRequest(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        credential_config: main_models.CredentialConfig = None,
        project_name: str = None,
        refresh_token: str = None,
    ):
        # The Weboffice access token. You can obtain the token by calling the [GenerateWebofficeToken](https://help.aliyun.com/document_detail/478226.html) or [RefreshWebofficeToken](https://help.aliyun.com/document_detail/478227.html) operation.
        # 
        # This parameter is required.
        self.access_token = access_token
        # **Leave this parameter empty unless you have special requirements.**
        # 
        # The China authorization configuration. This parameter is optional. For more information, see [Use chained authorization to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config = credential_config
        # The project name. For information about how to obtain the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The Weboffice refresh token. You can obtain the token by calling the [GenerateWebofficeToken](https://help.aliyun.com/document_detail/478226.html) or [RefreshWebofficeToken](https://help.aliyun.com/document_detail/478227.html) operation.
        # 
        # This parameter is required.
        self.refresh_token = refresh_token

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token is not None:
            result['AccessToken'] = self.access_token

        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()

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
            temp_model = main_models.CredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')

        return self

