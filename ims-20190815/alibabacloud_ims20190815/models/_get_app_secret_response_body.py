# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class GetAppSecretResponseBody(DaraModel):
    def __init__(
        self,
        app_secret: main_models.GetAppSecretResponseBodyAppSecret = None,
        request_id: str = None,
    ):
        # The details of the application secret.
        self.app_secret = app_secret
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.app_secret:
            self.app_secret.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppSecret') is not None:
            temp_model = main_models.GetAppSecretResponseBodyAppSecret()
            self.app_secret = temp_model.from_map(m.get('AppSecret'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAppSecretResponseBodyAppSecret(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret_id: str = None,
        app_secret_value: str = None,
        create_date: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The ID of the application secret.
        self.app_secret_id = app_secret_id
        # The content of the application secret.
        self.app_secret_value = app_secret_value
        # The creation time.
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id

        if self.app_secret_value is not None:
            result['AppSecretValue'] = self.app_secret_value

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')

        if m.get('AppSecretValue') is not None:
            self.app_secret_value = m.get('AppSecretValue')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        return self

