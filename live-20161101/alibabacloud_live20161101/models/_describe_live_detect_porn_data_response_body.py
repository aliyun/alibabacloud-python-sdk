# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDetectPornDataResponseBody(DaraModel):
    def __init__(
        self,
        detect_porn_data: main_models.DescribeLiveDetectPornDataResponseBodyDetectPornData = None,
        request_id: str = None,
    ):
        # The bandwidth data returned at each interval.
        self.detect_porn_data = detect_porn_data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.detect_porn_data:
            self.detect_porn_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detect_porn_data is not None:
            result['DetectPornData'] = self.detect_porn_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetectPornData') is not None:
            temp_model = main_models.DescribeLiveDetectPornDataResponseBodyDetectPornData()
            self.detect_porn_data = temp_model.from_map(m.get('DetectPornData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveDetectPornDataResponseBodyDetectPornData(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeLiveDetectPornDataResponseBodyDetectPornDataDataModule] = None,
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
                temp_model = main_models.DescribeLiveDetectPornDataResponseBodyDetectPornDataDataModule()
                self.data_module.append(temp_model.from_map(k1))

        return self

class DescribeLiveDetectPornDataResponseBodyDetectPornDataDataModule(DaraModel):
    def __init__(
        self,
        app: str = None,
        count: int = None,
        domain: str = None,
        fee: str = None,
        region: str = None,
        scene: str = None,
        stream: str = None,
        time_stamp: str = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app = app
        # The number of reviewed images.
        self.count = count
        # The main streaming domain.
        self.domain = domain
        # Indicates whether a quota of free image scanning is available. Valid values:
        # 
        # *   **free**
        # *   **charge**
        self.fee = fee
        # The region in which the domain name resides.
        self.region = region
        # The moderation scenario. Valid values:
        # 
        # *   **porn** (default): pornography
        # *   **terrorism**: terrorism or politically sensitive content
        # *   **ad**: ad violation
        # *   **live**: undesirable scene
        # *   **logo**
        self.scene = scene
        # The name of the live stream.
        self.stream = stream
        # The timestamp of the data returned. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app

        if self.count is not None:
            result['Count'] = self.count

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.fee is not None:
            result['Fee'] = self.fee

        if self.region is not None:
            result['Region'] = self.region

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.stream is not None:
            result['Stream'] = self.stream

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Fee') is not None:
            self.fee = m.get('Fee')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

