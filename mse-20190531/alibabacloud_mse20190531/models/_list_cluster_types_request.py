# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListClusterTypesRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        connect_type: str = None,
        mse_version: str = None,
        region_id: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The network type. Valid values:
        # 
        # *   slb
        # *   eni
        self.connect_type = connect_type
        # The edition of the MSE instance that you want to purchase.
        # 
        # *   mse_pro: Professional Edition
        # *   mse_dev: Developer Edition
        self.mse_version = mse_version
        # The ID of the region in which the instance resides. The region is supported by Microservices Engine (MSE).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type

        if self.mse_version is not None:
            result['MseVersion'] = self.mse_version

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')

        if m.get('MseVersion') is not None:
            self.mse_version = m.get('MseVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

