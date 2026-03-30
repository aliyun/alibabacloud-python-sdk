# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class ListAppSecretIdsResponseBody(DaraModel):
    def __init__(
        self,
        app_secrets: main_models.ListAppSecretIdsResponseBodyAppSecrets = None,
        request_id: str = None,
    ):
        self.app_secrets = app_secrets
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.app_secrets:
            self.app_secrets.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_secrets is not None:
            result['AppSecrets'] = self.app_secrets.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppSecrets') is not None:
            temp_model = main_models.ListAppSecretIdsResponseBodyAppSecrets()
            self.app_secrets = temp_model.from_map(m.get('AppSecrets'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAppSecretIdsResponseBodyAppSecrets(DaraModel):
    def __init__(
        self,
        app_secret: List[main_models.ListAppSecretIdsResponseBodyAppSecretsAppSecret] = None,
    ):
        self.app_secret = app_secret

    def validate(self):
        if self.app_secret:
            for v1 in self.app_secret:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppSecret'] = []
        if self.app_secret is not None:
            for k1 in self.app_secret:
                result['AppSecret'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_secret = []
        if m.get('AppSecret') is not None:
            for k1 in m.get('AppSecret'):
                temp_model = main_models.ListAppSecretIdsResponseBodyAppSecretsAppSecret()
                self.app_secret.append(temp_model.from_map(k1))

        return self

class ListAppSecretIdsResponseBodyAppSecretsAppSecret(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret_id: str = None,
        create_date: str = None,
    ):
        self.app_id = app_id
        self.app_secret_id = app_secret_id
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

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        return self

