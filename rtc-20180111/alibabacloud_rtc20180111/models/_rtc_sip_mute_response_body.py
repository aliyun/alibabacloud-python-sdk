# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class RtcSipMuteResponseBody(DaraModel):
    def __init__(
        self,
        err_tracks: List[main_models.RtcSipMuteResponseBodyErrTracks] = None,
        request_id: str = None,
    ):
        self.err_tracks = err_tracks
        self.request_id = request_id

    def validate(self):
        if self.err_tracks:
            for v1 in self.err_tracks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ErrTracks'] = []
        if self.err_tracks is not None:
            for k1 in self.err_tracks:
                result['ErrTracks'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.err_tracks = []
        if m.get('ErrTracks') is not None:
            for k1 in m.get('ErrTracks'):
                temp_model = main_models.RtcSipMuteResponseBodyErrTracks()
                self.err_tracks.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RtcSipMuteResponseBodyErrTracks(DaraModel):
    def __init__(
        self,
        err_msg: str = None,
        id: str = None,
        operation_id: str = None,
    ):
        # ErrMsg。
        self.err_msg = err_msg
        self.id = id
        # OperationId。
        self.operation_id = operation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        if self.id is not None:
            result['Id'] = self.id

        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        return self

