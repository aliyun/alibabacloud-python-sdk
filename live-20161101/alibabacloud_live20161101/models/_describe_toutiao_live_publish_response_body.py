# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeToutiaoLivePublishResponseBody(DaraModel):
    def __init__(
        self,
        content: List[main_models.DescribeToutiaoLivePublishResponseBodyContent] = None,
        description: str = None,
        request_id: str = None,
    ):
        # The stream ingest details.
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
                temp_model = main_models.DescribeToutiaoLivePublishResponseBodyContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeToutiaoLivePublishResponseBodyContent(DaraModel):
    def __init__(
        self,
        app: str = None,
        bitrate: float = None,
        bw_diff: float = None,
        cdn_name: str = None,
        domain: str = None,
        flr: float = None,
        fps: float = None,
        stream_name: str = None,
        timestamp: int = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app = app
        # The bitrate. Unit: bit/s.
        self.bitrate = bitrate
        # The bitrate difference.
        self.bw_diff = bw_diff
        # The name of the content delivery network (CDN) service.
        self.cdn_name = cdn_name
        # The ingest domain.
        self.domain = domain
        # The number of dropped frames.
        self.flr = flr
        # The frame rate.
        self.fps = fps
        # The name of the ingested stream.
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

        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.bw_diff is not None:
            result['BwDiff'] = self.bw_diff

        if self.cdn_name is not None:
            result['CdnName'] = self.cdn_name

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.flr is not None:
            result['Flr'] = self.flr

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('BwDiff') is not None:
            self.bw_diff = m.get('BwDiff')

        if m.get('CdnName') is not None:
            self.cdn_name = m.get('CdnName')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Flr') is not None:
            self.flr = m.get('Flr')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

