# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProxyBrandUserRequest(DaraModel):
    def __init__(
        self,
        brand_user_nick: str = None,
        channel_id: str = None,
        client_token: str = None,
        company: str = None,
        contact_name: str = None,
        contact_phone: str = None,
        industry: str = None,
        proxy_user_id: int = None,
    ):
        # This parameter is required.
        self.brand_user_nick = brand_user_nick
        # This parameter is required.
        self.channel_id = channel_id
        self.client_token = client_token
        # This parameter is required.
        self.company = company
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        # This parameter is required.
        self.industry = industry
        # This parameter is required.
        self.proxy_user_id = proxy_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brand_user_nick is not None:
            result['BrandUserNick'] = self.brand_user_nick

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.company is not None:
            result['Company'] = self.company

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.contact_phone is not None:
            result['ContactPhone'] = self.contact_phone

        if self.industry is not None:
            result['Industry'] = self.industry

        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrandUserNick') is not None:
            self.brand_user_nick = m.get('BrandUserNick')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Company') is not None:
            self.company = m.get('Company')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('ContactPhone') is not None:
            self.contact_phone = m.get('ContactPhone')

        if m.get('Industry') is not None:
            self.industry = m.get('Industry')

        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')

        return self

