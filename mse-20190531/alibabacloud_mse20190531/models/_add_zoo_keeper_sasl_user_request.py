# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class AddZooKeeperSaslUserRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        instance_id: str = None,
        reload: bool = None,
        sasl_user: List[main_models.AddZooKeeperSaslUserRequestSaslUser] = None,
    ):
        # The language of the response. Valid values: zh (default): Chinese, en: English.
        self.accept_language = accept_language
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether to restart the cluster to immediately load the SASL users.
        self.reload = reload
        # The list of SASL users to add.
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
                temp_model = main_models.AddZooKeeperSaslUserRequestSaslUser()
                self.sasl_user.append(temp_model.from_map(k1))

        return self

class AddZooKeeperSaslUserRequestSaslUser(DaraModel):
    def __init__(
        self,
        description: str = None,
        password: str = None,
        user_name: str = None,
    ):
        # The description of the user.
        self.description = description
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

        if self.password is not None:
            result['Password'] = self.password

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

