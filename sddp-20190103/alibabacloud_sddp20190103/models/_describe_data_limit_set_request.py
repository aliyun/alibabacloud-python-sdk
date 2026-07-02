# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataLimitSetRequest(DaraModel):
    def __init__(
        self,
        feature_type: int = None,
        lang: str = None,
        parent_id: str = None,
        region_type: str = None,
        resource_type: int = None,
    ):
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The language of the request and response. Valid values:
        # 
        # - **zh_cn**: Chinese (Simplified). This is the default value.
        # 
        # - **en_us**: English (US).
        self.lang = lang
        # The ID of the parent asset.
        # 
        # The [DescribeDataLimitDetail](~~DescribeDataLimitDetail~~) or [DescribeDataLimits](~~DescribeDataLimits~~) operation returns this ID in the **ParentId** parameter.
        self.parent_id = parent_id
        # The region type.
        # 
        # - **native_audit**: A region that supports traffic collection.
        self.region_type = region_type
        # The type of data asset. Valid values:
        # 
        # - **1**: MaxCompute.
        # 
        # - **2**: OSS.
        # 
        # - **3**: ADS.
        # 
        # - **4**: OTS.
        # 
        # - **5**: RDS.
        # 
        # - **6**: SELF_DB.
        # 
        # > If you set this parameter to a value other than 2, the returned OssBucketList object is empty.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.region_type is not None:
            result['RegionType'] = self.region_type

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('RegionType') is not None:
            self.region_type = m.get('RegionType')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

