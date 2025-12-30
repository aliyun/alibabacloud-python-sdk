# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TransferDomainRequest(DaraModel):
    def __init__(
        self,
        domain_names: str = None,
        lang: str = None,
        remark: str = None,
        target_user_id: int = None,
    ):
        # The domain names. Separate multiple domain names with commas (,). Only domain names registered with Alibaba Cloud are supported.
        # 
        # This parameter is required.
        self.domain_names = domain_names
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The description of the domain name.
        self.remark = remark
        # The destination user ID. The domain names and their Domain Name System (DNS) records are transferred to the destination user ID.
        # 
        # This parameter is required.
        self.target_user_id = target_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')

        return self

