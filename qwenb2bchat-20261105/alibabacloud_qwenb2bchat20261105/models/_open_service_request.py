# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_qwenb2bchat20261105 import models as main_models
from darabonba.model import DaraModel

class OpenServiceRequest(DaraModel):
    def __init__(
        self,
        communication: main_models.OpenServiceRequestCommunication = None,
        open_benefits: bool = None,
    ):
        # The business user identity. Provided according to the identity configuration bound to the gateway credential.
        self.communication = communication
        # Specifies whether to actually activate benefits. true enters the activation process, and false only validates the call and returns TEST_OK.
        # 
        # This parameter is required.
        self.open_benefits = open_benefits

    def validate(self):
        if self.communication:
            self.communication.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.communication is not None:
            result['communication'] = self.communication.to_map()

        if self.open_benefits is not None:
            result['openBenefits'] = self.open_benefits

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('communication') is not None:
            temp_model = main_models.OpenServiceRequestCommunication()
            self.communication = temp_model.from_map(m.get('communication'))

        if m.get('openBenefits') is not None:
            self.open_benefits = m.get('openBenefits')

        return self

class OpenServiceRequestCommunication(DaraModel):
    def __init__(
        self,
        user_info: main_models.OpenServiceRequestCommunicationUserInfo = None,
    ):
        # The object that carries the customer business user identifier.
        # 
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_info is not None:
            result['user_info'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user_info') is not None:
            temp_model = main_models.OpenServiceRequestCommunicationUserInfo()
            self.user_info = temp_model.from_map(m.get('user_info'))

        return self

class OpenServiceRequestCommunicationUserInfo(DaraModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # The customer business user ID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

