# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest(DaraModel):
    def __init__(
        self,
        domain_name: List[str] = None,
        lang: str = None,
        registrant_profile_id: int = None,
        transfer_out_prohibited: bool = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        # This parameter is required.
        self.registrant_profile_id = registrant_profile_id
        # This parameter is required.
        self.transfer_out_prohibited = transfer_out_prohibited
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id

        if self.transfer_out_prohibited is not None:
            result['TransferOutProhibited'] = self.transfer_out_prohibited

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')

        if m.get('TransferOutProhibited') is not None:
            self.transfer_out_prohibited = m.get('TransferOutProhibited')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

