# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryLiveWatchDetailResponseBody(DaraModel):
    def __init__(
        self,
        avg_watch_time: int = None,
        live_uv: int = None,
        msg_count: int = None,
        playback_uv: int = None,
        praise_count: int = None,
        pv: int = None,
        request_id: str = None,
        total_watch_time: int = None,
        uv: int = None,
    ):
        self.avg_watch_time = avg_watch_time
        self.live_uv = live_uv
        self.msg_count = msg_count
        self.playback_uv = playback_uv
        self.praise_count = praise_count
        self.pv = pv
        # requestId
        self.request_id = request_id
        self.total_watch_time = total_watch_time
        self.uv = uv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_watch_time is not None:
            result['avgWatchTime'] = self.avg_watch_time

        if self.live_uv is not None:
            result['liveUv'] = self.live_uv

        if self.msg_count is not None:
            result['msgCount'] = self.msg_count

        if self.playback_uv is not None:
            result['playbackUv'] = self.playback_uv

        if self.praise_count is not None:
            result['praiseCount'] = self.praise_count

        if self.pv is not None:
            result['pv'] = self.pv

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_watch_time is not None:
            result['totalWatchTime'] = self.total_watch_time

        if self.uv is not None:
            result['uv'] = self.uv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avgWatchTime') is not None:
            self.avg_watch_time = m.get('avgWatchTime')

        if m.get('liveUv') is not None:
            self.live_uv = m.get('liveUv')

        if m.get('msgCount') is not None:
            self.msg_count = m.get('msgCount')

        if m.get('playbackUv') is not None:
            self.playback_uv = m.get('playbackUv')

        if m.get('praiseCount') is not None:
            self.praise_count = m.get('praiseCount')

        if m.get('pv') is not None:
            self.pv = m.get('pv')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalWatchTime') is not None:
            self.total_watch_time = m.get('totalWatchTime')

        if m.get('uv') is not None:
            self.uv = m.get('uv')

        return self

