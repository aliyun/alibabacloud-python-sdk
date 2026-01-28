# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDomainGroupListRequest(DaraModel):
    def __init__(
        self,
        domain_group_name: str = None,
        lang: str = None,
        order_by_type: str = None,
        order_key_type: str = None,
        show_deleting_group: bool = None,
        user_client_ip: str = None,
    ):
        self.domain_group_name = domain_group_name
        self.lang = lang
        self.order_by_type = order_by_type
        self.order_key_type = order_key_type
        self.show_deleting_group = show_deleting_group
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_group_name is not None:
            result['DomainGroupName'] = self.domain_group_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.order_by_type is not None:
            result['OrderByType'] = self.order_by_type

        if self.order_key_type is not None:
            result['OrderKeyType'] = self.order_key_type

        if self.show_deleting_group is not None:
            result['ShowDeletingGroup'] = self.show_deleting_group

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainGroupName') is not None:
            self.domain_group_name = m.get('DomainGroupName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('OrderByType') is not None:
            self.order_by_type = m.get('OrderByType')

        if m.get('OrderKeyType') is not None:
            self.order_key_type = m.get('OrderKeyType')

        if m.get('ShowDeletingGroup') is not None:
            self.show_deleting_group = m.get('ShowDeletingGroup')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

