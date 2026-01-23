# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class GetNetworkBlacklistResponseBody(DaraModel):
    def __init__(
        self,
        network_blacklist_model: main_models.GetNetworkBlacklistResponseBodyNetworkBlacklistModel = None,
        request_id: str = None,
    ):
        self.network_blacklist_model = network_blacklist_model
        self.request_id = request_id

    def validate(self):
        if self.network_blacklist_model:
            self.network_blacklist_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_blacklist_model is not None:
            result['NetworkBlacklistModel'] = self.network_blacklist_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkBlacklistModel') is not None:
            temp_model = main_models.GetNetworkBlacklistResponseBodyNetworkBlacklistModel()
            self.network_blacklist_model = temp_model.from_map(m.get('NetworkBlacklistModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetNetworkBlacklistResponseBodyNetworkBlacklistModel(DaraModel):
    def __init__(
        self,
        domain_blacklist: List[str] = None,
        ip_blacklist: List[str] = None,
    ):
        self.domain_blacklist = domain_blacklist
        self.ip_blacklist = ip_blacklist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_blacklist is not None:
            result['DomainBlacklist'] = self.domain_blacklist

        if self.ip_blacklist is not None:
            result['IpBlacklist'] = self.ip_blacklist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainBlacklist') is not None:
            self.domain_blacklist = m.get('DomainBlacklist')

        if m.get('IpBlacklist') is not None:
            self.ip_blacklist = m.get('IpBlacklist')

        return self

