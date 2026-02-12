# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ons20190214 import models as main_models
from darabonba.model import DaraModel

class OnsMessageTraceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.OnsMessageTraceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.OnsMessageTraceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class OnsMessageTraceResponseBodyData(DaraModel):
    def __init__(
        self,
        message_track: List[main_models.OnsMessageTraceResponseBodyDataMessageTrack] = None,
    ):
        self.message_track = message_track

    def validate(self):
        if self.message_track:
            for v1 in self.message_track:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MessageTrack'] = []
        if self.message_track is not None:
            for k1 in self.message_track:
                result['MessageTrack'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.message_track = []
        if m.get('MessageTrack') is not None:
            for k1 in m.get('MessageTrack'):
                temp_model = main_models.OnsMessageTraceResponseBodyDataMessageTrack()
                self.message_track.append(temp_model.from_map(k1))

        return self

class OnsMessageTraceResponseBodyDataMessageTrack(DaraModel):
    def __init__(
        self,
        consumer_group: str = None,
        instance_id: str = None,
        track_type: str = None,
    ):
        self.consumer_group = consumer_group
        self.instance_id = instance_id
        self.track_type = track_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.track_type is not None:
            result['TrackType'] = self.track_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TrackType') is not None:
            self.track_type = m.get('TrackType')

        return self

