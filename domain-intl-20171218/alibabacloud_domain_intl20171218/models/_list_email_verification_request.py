# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEmailVerificationRequest(DaraModel):
    def __init__(
        self,
        begin_create_time: int = None,
        email: str = None,
        end_create_time: int = None,
        lang: str = None,
        page_num: int = None,
        page_size: int = None,
        user_client_ip: str = None,
        verification_status: int = None,
    ):
        self.begin_create_time = begin_create_time
        self.email = email
        self.end_create_time = end_create_time
        self.lang = lang
        self.page_num = page_num
        self.page_size = page_size
        self.user_client_ip = user_client_ip
        self.verification_status = verification_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_create_time is not None:
            result['BeginCreateTime'] = self.begin_create_time

        if self.email is not None:
            result['Email'] = self.email

        if self.end_create_time is not None:
            result['EndCreateTime'] = self.end_create_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginCreateTime') is not None:
            self.begin_create_time = m.get('BeginCreateTime')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EndCreateTime') is not None:
            self.end_create_time = m.get('EndCreateTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')

        return self

