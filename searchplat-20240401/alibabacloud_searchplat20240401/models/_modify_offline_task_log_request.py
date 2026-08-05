# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class ModifyOfflineTaskLogRequest(DaraModel):
    def __init__(
        self,
        network: main_models.ModifyOfflineTaskLogRequestNetwork = None,
        region_id: str = None,
    ):
        # The network configuration for enabling or disabling network access.
        self.network = network
        # The region ID.
        self.region_id = region_id

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

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('network') is not None:
            temp_model = main_models.ModifyOfflineTaskLogRequestNetwork()
            self.network = temp_model.from_map(m.get('network'))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

class ModifyOfflineTaskLogRequestNetwork(DaraModel):
    def __init__(
        self,
        private_es: main_models.ModifyOfflineTaskLogRequestNetworkPrivateEs = None,
        public_es: main_models.ModifyOfflineTaskLogRequestNetworkPublicEs = None,
    ):
        # The ES private network information.
        self.private_es = private_es
        # **The ES public network information.**
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
            temp_model = main_models.ModifyOfflineTaskLogRequestNetworkPrivateEs()
            self.private_es = temp_model.from_map(m.get('privateEs'))

        if m.get('publicEs') is not None:
            temp_model = main_models.ModifyOfflineTaskLogRequestNetworkPublicEs()
            self.public_es = temp_model.from_map(m.get('publicEs'))

        return self

class ModifyOfflineTaskLogRequestNetworkPublicEs(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        white_ip_group: List[main_models.ModifyOfflineTaskLogRequestNetworkPublicEsWhiteIpGroup] = None,
    ):
        # **Specifies whether to enable or disable public network access.**
        self.enabled = enabled
        # **The IP whitelist group information.**
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
        if self.enabled is not None:
            result['enabled'] = self.enabled

        result['whiteIpGroup'] = []
        if self.white_ip_group is not None:
            for k1 in self.white_ip_group:
                result['whiteIpGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        self.white_ip_group = []
        if m.get('whiteIpGroup') is not None:
            for k1 in m.get('whiteIpGroup'):
                temp_model = main_models.ModifyOfflineTaskLogRequestNetworkPublicEsWhiteIpGroup()
                self.white_ip_group.append(temp_model.from_map(k1))

        return self

class ModifyOfflineTaskLogRequestNetworkPublicEsWhiteIpGroup(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
    ):
        # **The name of the IP whitelist group.**
        self.group_name = group_name
        # **The IP whitelist.**
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

class ModifyOfflineTaskLogRequestNetworkPrivateEs(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        white_ip_group: List[main_models.ModifyOfflineTaskLogRequestNetworkPrivateEsWhiteIpGroup] = None,
    ):
        # Specifies whether to enable or disable private network access.
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
        if self.enabled is not None:
            result['enabled'] = self.enabled

        result['whiteIpGroup'] = []
        if self.white_ip_group is not None:
            for k1 in self.white_ip_group:
                result['whiteIpGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        self.white_ip_group = []
        if m.get('whiteIpGroup') is not None:
            for k1 in m.get('whiteIpGroup'):
                temp_model = main_models.ModifyOfflineTaskLogRequestNetworkPrivateEsWhiteIpGroup()
                self.white_ip_group.append(temp_model.from_map(k1))

        return self

class ModifyOfflineTaskLogRequestNetworkPrivateEsWhiteIpGroup(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
    ):
        # The name of the IP whitelist group.
        self.group_name = group_name
        # The IP whitelist.
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

