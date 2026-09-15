# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class CreateAttackPathWhitelistResponseBody(DaraModel):
    def __init__(
        self,
        attack_path_whitelist: main_models.CreateAttackPathWhitelistResponseBodyAttackPathWhitelist = None,
        request_id: str = None,
    ):
        # The attack path whitelist.
        self.attack_path_whitelist = attack_path_whitelist
        # The request ID. Alibaba Cloud generates a unique ID for each request. You can use the ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.attack_path_whitelist:
            self.attack_path_whitelist.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_path_whitelist is not None:
            result['AttackPathWhitelist'] = self.attack_path_whitelist.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackPathWhitelist') is not None:
            temp_model = main_models.CreateAttackPathWhitelistResponseBodyAttackPathWhitelist()
            self.attack_path_whitelist = temp_model.from_map(m.get('AttackPathWhitelist'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateAttackPathWhitelistResponseBodyAttackPathWhitelist(DaraModel):
    def __init__(
        self,
        attack_path_whitelist_id: str = None,
    ):
        # The ID of the attack path whitelist.
        self.attack_path_whitelist_id = attack_path_whitelist_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_path_whitelist_id is not None:
            result['AttackPathWhitelistId'] = self.attack_path_whitelist_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackPathWhitelistId') is not None:
            self.attack_path_whitelist_id = m.get('AttackPathWhitelistId')

        return self

