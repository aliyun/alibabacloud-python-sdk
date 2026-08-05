# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class GetOfflineTaskLogResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetOfflineTaskLogResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.GetOfflineTaskLogResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class GetOfflineTaskLogResponseBodyResult(DaraModel):
    def __init__(
        self,
        network: main_models.GetOfflineTaskLogResponseBodyResultNetwork = None,
    ):
        # The network information.
        self.network = network

    def validate(self):
        if self.network:
            self.network.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network is not None:
            result['network'] = self.network.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('network') is not None:
            temp_model = main_models.GetOfflineTaskLogResponseBodyResultNetwork()
            self.network = temp_model.from_map(m.get('network'))

        return self

class GetOfflineTaskLogResponseBodyResultNetwork(DaraModel):
    def __init__(
        self,
        private_es: main_models.GetOfflineTaskLogResponseBodyResultNetworkPrivateEs = None,
        public_es: main_models.GetOfflineTaskLogResponseBodyResultNetworkPublicEs = None,
    ):
        # The private ES information.
        self.private_es = private_es
        # The public ES information.
        self.public_es = public_es

    def validate(self):
        if self.private_es:
            self.private_es.validate()
        if self.public_es:
            self.public_es.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.private_es is not None:
            result['privateEs'] = self.private_es.to_map()

        if self.public_es is not None:
            result['publicEs'] = self.public_es.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('privateEs') is not None:
            temp_model = main_models.GetOfflineTaskLogResponseBodyResultNetworkPrivateEs()
            self.private_es = temp_model.from_map(m.get('privateEs'))

        if m.get('publicEs') is not None:
            temp_model = main_models.GetOfflineTaskLogResponseBodyResultNetworkPublicEs()
            self.public_es = temp_model.from_map(m.get('publicEs'))

        return self

class GetOfflineTaskLogResponseBodyResultNetworkPublicEs(DaraModel):
    def __init__(
        self,
        domain: str = None,
        enabled: bool = None,
        white_ip_group: List[main_models.GetOfflineTaskLogResponseBodyResultNetworkPublicEsWhiteIpGroup] = None,
    ):
        # The public domain name of ES.
        self.domain = domain
        # Indicates whether public ES is enabled.
        self.enabled = enabled
        # The IP whitelist groups.
        self.white_ip_group = white_ip_group

    def validate(self):
        if self.white_ip_group:
            for v1 in self.white_ip_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['domain'] = self.domain

        if self.enabled is not None:
            result['enabled'] = self.enabled

        result['whiteIpGroup'] = []
        if self.white_ip_group is not None:
            for k1 in self.white_ip_group:
                result['whiteIpGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        self.white_ip_group = []
        if m.get('whiteIpGroup') is not None:
            for k1 in m.get('whiteIpGroup'):
                temp_model = main_models.GetOfflineTaskLogResponseBodyResultNetworkPublicEsWhiteIpGroup()
                self.white_ip_group.append(temp_model.from_map(k1))

        return self

class GetOfflineTaskLogResponseBodyResultNetworkPublicEsWhiteIpGroup(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
    ):
        # The group name.
        self.group_name = group_name
        # The list of IP addresses in the whitelist group.
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.ips is not None:
            result['ips'] = self.ips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('ips') is not None:
            self.ips = m.get('ips')

        return self

class GetOfflineTaskLogResponseBodyResultNetworkPrivateEs(DaraModel):
    def __init__(
        self,
        domain: str = None,
        enabled: bool = None,
        white_ip_group: List[main_models.GetOfflineTaskLogResponseBodyResultNetworkPrivateEsWhiteIpGroup] = None,
    ):
        # The domain name of the private ES.
        self.domain = domain
        # Indicates whether private ES is enabled.
        self.enabled = enabled
        # The IP whitelist groups.
        self.white_ip_group = white_ip_group

    def validate(self):
        if self.white_ip_group:
            for v1 in self.white_ip_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['domain'] = self.domain

        if self.enabled is not None:
            result['enabled'] = self.enabled

        result['whiteIpGroup'] = []
        if self.white_ip_group is not None:
            for k1 in self.white_ip_group:
                result['whiteIpGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        self.white_ip_group = []
        if m.get('whiteIpGroup') is not None:
            for k1 in m.get('whiteIpGroup'):
                temp_model = main_models.GetOfflineTaskLogResponseBodyResultNetworkPrivateEsWhiteIpGroup()
                self.white_ip_group.append(temp_model.from_map(k1))

        return self

class GetOfflineTaskLogResponseBodyResultNetworkPrivateEsWhiteIpGroup(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
    ):
        # The group name.
        self.group_name = group_name
        # The list of IP addresses in the whitelist group.
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.ips is not None:
            result['ips'] = self.ips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('ips') is not None:
            self.ips = m.get('ips')

        return self

