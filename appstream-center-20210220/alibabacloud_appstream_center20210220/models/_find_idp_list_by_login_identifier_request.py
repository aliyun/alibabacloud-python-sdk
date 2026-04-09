# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from darabonba.model import DaraModel

class FindIdpListByLoginIdentifierRequest(DaraModel):
    def __init__(
        self,
        available_features: Dict[str, str] = None,
        client_channel: str = None,
        client_id: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_version: str = None,
        login_identifier: str = None,
        support_types: List[str] = None,
        uuid: str = None,
    ):
        self.available_features = available_features
        self.client_channel = client_channel
        self.client_id = client_id
        self.client_ip = client_ip
        self.client_os = client_os
        self.client_version = client_version
        # This parameter is required.
        self.login_identifier = login_identifier
        self.support_types = support_types
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_features is not None:
            result['AvailableFeatures'] = self.available_features

        if self.client_channel is not None:
            result['ClientChannel'] = self.client_channel

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.client_os is not None:
            result['ClientOS'] = self.client_os

        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.login_identifier is not None:
            result['LoginIdentifier'] = self.login_identifier

        if self.support_types is not None:
            result['SupportTypes'] = self.support_types

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableFeatures') is not None:
            self.available_features = m.get('AvailableFeatures')

        if m.get('ClientChannel') is not None:
            self.client_channel = m.get('ClientChannel')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')

        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('LoginIdentifier') is not None:
            self.login_identifier = m.get('LoginIdentifier')

        if m.get('SupportTypes') is not None:
            self.support_types = m.get('SupportTypes')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

