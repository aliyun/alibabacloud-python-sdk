# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class CreateADConnectorDirectoryResponseBody(DaraModel):
    def __init__(
        self,
        ad_connectors: List[main_models.CreateADConnectorDirectoryResponseBodyAdConnectors] = None,
        directory_id: str = None,
        request_id: str = None,
        trust_password: str = None,
    ):
        # The details of AD connectors.
        self.ad_connectors = ad_connectors
        # The ID of the AD directory.
        self.directory_id = directory_id
        # The ID of the request.
        self.request_id = request_id
        # The AD trust password.
        self.trust_password = trust_password

    def validate(self):
        if self.ad_connectors:
            for v1 in self.ad_connectors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdConnectors'] = []
        if self.ad_connectors is not None:
            for k1 in self.ad_connectors:
                result['AdConnectors'].append(k1.to_map() if k1 else None)

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.trust_password is not None:
            result['TrustPassword'] = self.trust_password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ad_connectors = []
        if m.get('AdConnectors') is not None:
            for k1 in m.get('AdConnectors'):
                temp_model = main_models.CreateADConnectorDirectoryResponseBodyAdConnectors()
                self.ad_connectors.append(temp_model.from_map(k1))

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TrustPassword') is not None:
            self.trust_password = m.get('TrustPassword')

        return self

class CreateADConnectorDirectoryResponseBodyAdConnectors(DaraModel):
    def __init__(
        self,
        address: str = None,
    ):
        # The connection address.
        self.address = address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        return self

