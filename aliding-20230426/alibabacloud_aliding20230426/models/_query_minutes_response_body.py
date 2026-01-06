# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class QueryMinutesResponseBody(DaraModel):
    def __init__(
        self,
        audio_list: List[main_models.QueryMinutesResponseBodyAudioList] = None,
        request_id: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.audio_list = audio_list
        self.request_id = request_id
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.audio_list:
            for v1 in self.audio_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['audioList'] = []
        if self.audio_list is not None:
            for k1 in self.audio_list:
                result['audioList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_list = []
        if m.get('audioList') is not None:
            for k1 in m.get('audioList'):
                temp_model = main_models.QueryMinutesResponseBodyAudioList()
                self.audio_list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class QueryMinutesResponseBodyAudioList(DaraModel):
    def __init__(
        self,
        duration: int = None,
        end_time: int = None,
        file_size: int = None,
        play_url: str = None,
        record_id: str = None,
        start_time: int = None,
        user_id: str = None,
    ):
        self.duration = duration
        self.end_time = end_time
        self.file_size = file_size
        self.play_url = play_url
        self.record_id = record_id
        self.start_time = start_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.play_url is not None:
            result['PlayUrl'] = self.play_url

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('PlayUrl') is not None:
            self.play_url = m.get('PlayUrl')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

