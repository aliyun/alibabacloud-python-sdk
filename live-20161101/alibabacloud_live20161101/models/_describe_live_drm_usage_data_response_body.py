# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDrmUsageDataResponseBody(DaraModel):
    def __init__(
        self,
        drm_usage_data: main_models.DescribeLiveDrmUsageDataResponseBodyDrmUsageData = None,
        request_id: str = None,
    ):
        # The usage of the DRM encryption service at each time interval.
        self.drm_usage_data = drm_usage_data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.drm_usage_data:
            self.drm_usage_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drm_usage_data is not None:
            result['DrmUsageData'] = self.drm_usage_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DrmUsageData') is not None:
            temp_model = main_models.DescribeLiveDrmUsageDataResponseBodyDrmUsageData()
            self.drm_usage_data = temp_model.from_map(m.get('DrmUsageData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveDrmUsageDataResponseBodyDrmUsageData(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeLiveDrmUsageDataResponseBodyDrmUsageDataDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for v1 in self.data_module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataModule'] = []
        if self.data_module is not None:
            for k1 in self.data_module:
                result['DataModule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k1 in m.get('DataModule'):
                temp_model = main_models.DescribeLiveDrmUsageDataResponseBodyDrmUsageDataDataModule()
                self.data_module.append(temp_model.from_map(k1))

        return self

class DescribeLiveDrmUsageDataResponseBodyDrmUsageDataDataModule(DaraModel):
    def __init__(
        self,
        count: int = None,
        domain: str = None,
        drm_type: str = None,
        region: str = None,
        time_stamp: str = None,
    ):
        # The number of times DRM-encrypted live streams are requested.
        self.count = count
        # The domain name. If the value of SplitBy includes domain, the returned data is grouped by domain name.
        self.domain = domain
        # The DRM type. If the value of SplitBy includes drm_type, the returned data is grouped by DRM type.
        self.drm_type = drm_type
        # The ID of the region. If the value of SplitBy includes region, the returned data is grouped by region.
        self.region = region
        # The timestamp of the returned data.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.drm_type is not None:
            result['DrmType'] = self.drm_type

        if self.region is not None:
            result['Region'] = self.region

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('DrmType') is not None:
            self.drm_type = m.get('DrmType')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

