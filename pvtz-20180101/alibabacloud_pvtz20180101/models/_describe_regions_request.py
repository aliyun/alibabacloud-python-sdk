# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRegionsRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        authorized_user_id: int = None,
        lang: str = None,
        scene: str = None,
        user_client_ip: str = None,
        vpc_type: str = None,
    ):
        # The supported language. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US: English
        # 
        # Default value: en-US.
        # 
        # >  AcceptLanguage has a higher priority than Lang.
        self.accept_language = accept_language
        # The ID of the Alibaba Cloud account to which the permissions on the resources are granted.
        self.authorized_user_id = authorized_user_id
        # The language of the response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        # 
        # Default value: **en**.
        # 
        # >  Lang has a lower priority than AcceptLanguage.
        self.lang = lang
        # The scenario. Valid values:
        # 
        # *   AUTH: the built-in authoritative module
        # *   FWD: the forward module
        # *   RA: the traffic analysis module
        self.scene = scene
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The VPC type. Valid values:
        # 
        # *   STANDARD: standard VPC
        # *   EDS: Elastic Desktop Service (EDS) workspace VPC
        self.vpc_type = vpc_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')

        return self

