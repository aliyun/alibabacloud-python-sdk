# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAddressBookRequest(DaraModel):
    def __init__(
        self,
        group_uuid: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        # The unique ID of the address book.
        # 
        # > You can call the [DescribeAddressBook](~~DescribeAddressBook~~) operation to query the ID.
        # 
        # This parameter is required.
        self.group_uuid = group_uuid
        # The language type. Valid values:
        # 
        # - **en**: English
        # - **zh**: Chinese (default).
        self.lang = lang
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

