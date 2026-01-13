# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class GetRecallManagementConfigResponseBody(DaraModel):
    def __init__(
        self,
        network_configs: List[main_models.GetRecallManagementConfigResponseBodyNetworkConfigs] = None,
        request_id: str = None,
        user_name: str = None,
    ):
        self.network_configs = network_configs
        # Id of the request
        self.request_id = request_id
        self.user_name = user_name

    def validate(self):
        if self.network_configs:
            for v1 in self.network_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkConfigs'] = []
        if self.network_configs is not None:
            for k1 in self.network_configs:
                result['NetworkConfigs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_configs = []
        if m.get('NetworkConfigs') is not None:
            for k1 in m.get('NetworkConfigs'):
                temp_model = main_models.GetRecallManagementConfigResponseBodyNetworkConfigs()
                self.network_configs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class GetRecallManagementConfigResponseBodyNetworkConfigs(DaraModel):
    def __init__(
        self,
        private_link_address: str = None,
        status: str = None,
        vpc_id: str = None,
        vswitch_ids: Dict[str, str] = None,
    ):
        self.private_link_address = private_link_address
        self.status = status
        self.vpc_id = vpc_id
        self.vswitch_ids = vswitch_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.private_link_address is not None:
            result['PrivateLinkAddress'] = self.private_link_address

        if self.status is not None:
            result['Status'] = self.status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_ids is not None:
            result['VswitchIds'] = self.vswitch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateLinkAddress') is not None:
            self.private_link_address = m.get('PrivateLinkAddress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchIds') is not None:
            self.vswitch_ids = m.get('VswitchIds')

        return self

