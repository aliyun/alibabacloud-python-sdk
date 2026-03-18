# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class GetMmsFetchMetadataJobResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMmsFetchMetadataJobResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
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
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetMmsFetchMetadataJobResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetMmsFetchMetadataJobResponseBodyData(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        error_msg: str = None,
        id: int = None,
        progress: float = None,
        result: str = None,
        source_id: int = None,
        start_time: str = None,
        status: str = None,
    ):
        # The time when metadata synchronization ended.
        self.end_time = end_time
        # The error message.
        self.error_msg = error_msg
        # The ID of the asynchronous task.
        self.id = id
        # The progress of metadata synchronization. Valid values: 1 to 10000.
        self.progress = progress
        # The result of metadata synchronization.
        self.result = result
        # The data source ID.
        self.source_id = source_id
        # The time when metadata synchronization started.
        self.start_time = start_time
        # The status of the asynchronous task for metadata synchronization.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.id is not None:
            result['id'] = self.id

        if self.progress is not None:
            result['progress'] = self.progress

        if self.result is not None:
            result['result'] = self.result

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

