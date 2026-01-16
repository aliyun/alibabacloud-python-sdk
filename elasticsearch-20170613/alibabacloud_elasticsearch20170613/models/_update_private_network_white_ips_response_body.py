# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class UpdatePrivateNetworkWhiteIpsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.UpdatePrivateNetworkWhiteIpsResponseBodyResult = None,
    ):
        self.request_id = request_id
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
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.UpdatePrivateNetworkWhiteIpsResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class UpdatePrivateNetworkWhiteIpsResponseBodyResult(DaraModel):
    def __init__(
        self,
        private_network_ip_white_list: List[str] = None,
    ):
        self.private_network_ip_white_list = private_network_ip_white_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.private_network_ip_white_list is not None:
            result['privateNetworkIpWhiteList'] = self.private_network_ip_white_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('privateNetworkIpWhiteList') is not None:
            self.private_network_ip_white_list = m.get('privateNetworkIpWhiteList')

        return self

