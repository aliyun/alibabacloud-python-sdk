# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeToutiaoLivePlayResponseBody(DaraModel):
    def __init__(
        self,
        content: List[main_models.DescribeToutiaoLivePlayResponseBodyContent] = None,
        description: str = None,
        request_id: str = None,
    ):
        # The information about the live stream.
        self.content = content
        # The description of the response status.
        self.description = description
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.DescribeToutiaoLivePlayResponseBodyContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeToutiaoLivePlayResponseBodyContent(DaraModel):
    def __init__(
        self,
        app: str = None,
        bandwidth: float = None,
        cdn_name: str = None,
        domain: str = None,
        play_num: int = None,
        stream_name: str = None,
        timestamp: int = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app = app
        # The bandwidth. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The Content Delivery Network (CDN) name.
        self.cdn_name = cdn_name
        # The streaming domain.
        self.domain = domain
        # The number of viewers.
        self.play_num = play_num
        # The name of the live stream.
        self.stream_name = stream_name
        # The timestamp.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.cdn_name is not None:
            result['CdnName'] = self.cdn_name

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.play_num is not None:
            result['PlayNum'] = self.play_num

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('CdnName') is not None:
            self.cdn_name = m.get('CdnName')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('PlayNum') is not None:
            self.play_num = m.get('PlayNum')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

