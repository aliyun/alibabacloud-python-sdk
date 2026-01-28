# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveSingleTaskForUpdatingContactInfoRequest(DaraModel):
    def __init__(
        self,
        add_transfer_lock: bool = None,
        contact_type: str = None,
        domain_name: str = None,
        instance_id: str = None,
        lang: str = None,
        registrant_profile_id: int = None,
        user_client_ip: str = None,
    ):
        self.add_transfer_lock = add_transfer_lock
        # This parameter is required.
        self.contact_type = contact_type
        # This parameter is required.
        self.domain_name = domain_name
        self.instance_id = instance_id
        self.lang = lang
        # This parameter is required.
        self.registrant_profile_id = registrant_profile_id
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_transfer_lock is not None:
            result['AddTransferLock'] = self.add_transfer_lock

        if self.contact_type is not None:
            result['ContactType'] = self.contact_type

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddTransferLock') is not None:
            self.add_transfer_lock = m.get('AddTransferLock')

        if m.get('ContactType') is not None:
            self.contact_type = m.get('ContactType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

