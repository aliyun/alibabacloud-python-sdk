# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class UpdateZooKeeperSaslUserRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        instance_id: str = None,
        reload: bool = None,
        sasl_user: List[main_models.UpdateZooKeeperSaslUserRequestSaslUser] = None,
    ):
        # The language of the response. Valid values: zh (default): Chinese. en: English.
        self.accept_language = accept_language
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether the changes take effect immediately.
        self.reload = reload
        # The list of SASL users to update.
        # 
        # This parameter is required.
        self.sasl_user = sasl_user

    def validate(self):
        if self.sasl_user:
            for v1 in self.sasl_user:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.reload is not None:
            result['Reload'] = self.reload

        result['SaslUser'] = []
        if self.sasl_user is not None:
            for k1 in self.sasl_user:
                result['SaslUser'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Reload') is not None:
            self.reload = m.get('Reload')

        self.sasl_user = []
        if m.get('SaslUser') is not None:
            for k1 in m.get('SaslUser'):
                temp_model = main_models.UpdateZooKeeperSaslUserRequestSaslUser()
                self.sasl_user.append(temp_model.from_map(k1))

        return self

class UpdateZooKeeperSaslUserRequestSaslUser(DaraModel):
    def __init__(
        self,
        description: str = None,
        origin_password: str = None,
        password: str = None,
        user_name: str = None,
    ):
        # The description of the user.
        self.description = description
        # The original password. This parameter is required if you want to change the password.
        self.origin_password = origin_password
        # The password.
        self.password = password
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.origin_password is not None:
            result['OriginPassword'] = self.origin_password

        if self.password is not None:
            result['Password'] = self.password

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OriginPassword') is not None:
            self.origin_password = m.get('OriginPassword')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

