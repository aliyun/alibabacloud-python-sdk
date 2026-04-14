# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class UpdateUserRequest(DaraModel):
    def __init__(
        self,
        user: main_models.UpdateUserRequestUser = None,
    ):
        # User Information
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user is not None:
            result['User'] = self.user.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('User') is not None:
            temp_model = main_models.UpdateUserRequestUser()
            self.user = temp_model.from_map(m.get('User'))

        return self

class UpdateUserRequestUser(DaraModel):
    def __init__(
        self,
        enable_eventbridge: bool = None,
    ):
        # Whether EventBridge is enabled
        self.enable_eventbridge = enable_eventbridge

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_eventbridge is not None:
            result['EnableEventbridge'] = self.enable_eventbridge

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableEventbridge') is not None:
            self.enable_eventbridge = m.get('EnableEventbridge')

        return self

