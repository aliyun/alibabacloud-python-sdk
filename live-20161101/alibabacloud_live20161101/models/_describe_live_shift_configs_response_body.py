# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveShiftConfigsResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.DescribeLiveShiftConfigsResponseBodyContent = None,
        request_id: str = None,
    ):
        # The time shifting configurations.
        self.content = content
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.DescribeLiveShiftConfigsResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveShiftConfigsResponseBodyContent(DaraModel):
    def __init__(
        self,
        config: List[main_models.DescribeLiveShiftConfigsResponseBodyContentConfig] = None,
    ):
        self.config = config

    def validate(self):
        if self.config:
            for v1 in self.config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Config'] = []
        if self.config is not None:
            for k1 in self.config:
                result['Config'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config = []
        if m.get('Config') is not None:
            for k1 in m.get('Config'):
                temp_model = main_models.DescribeLiveShiftConfigsResponseBodyContentConfig()
                self.config.append(temp_model.from_map(k1))

        return self

class DescribeLiveShiftConfigsResponseBodyContentConfig(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        ignore_transcode: bool = None,
        stream_name: str = None,
        vision: int = None,
    ):
        # The application for which you configure time shifting.
        self.app_name = app_name
        # The domain name for which you configure time shifting.
        self.domain_name = domain_name
        # Whether to ignore time shift generation for the transcode stream.
        # 
        # *   true: Ignore time shifting generation.
        # *   false: Generate time shifting.
        # 
        # The default value is true.
        self.ignore_transcode = ignore_transcode
        # The name of the live stream for which you configure time shifting.
        self.stream_name = stream_name
        # The number of days for which the time shifting configurations are retained.
        self.vision = vision

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.ignore_transcode is not None:
            result['IgnoreTranscode'] = self.ignore_transcode

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.vision is not None:
            result['Vision'] = self.vision

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('IgnoreTranscode') is not None:
            self.ignore_transcode = m.get('IgnoreTranscode')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('Vision') is not None:
            self.vision = m.get('Vision')

        return self

