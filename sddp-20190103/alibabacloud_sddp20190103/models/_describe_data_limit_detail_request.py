# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataLimitDetailRequest(DaraModel):
    def __init__(
        self,
        feature_type: int = None,
        id: int = None,
        lang: str = None,
        network_type: int = None,
    ):
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The unique ID of the data asset that you want to query.
        # 
        # > You can call the [DescribeDataLimits](~~DescribeDataLimits~~) operation to query the ID of the data asset.
        # 
        # This parameter is required.
        self.id = id
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Simplified Chinese.
        # *   **en**: English
        self.lang = lang
        # The network type of the data asset that you want to query. Valid values:
        # 
        # *   **1**: virtual private cloud (VPC)
        # *   **2**: classic network
        self.network_type = network_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.id is not None:
            result['Id'] = self.id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        return self

