# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class CreateAnalysisExportTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.CreateAnalysisExportTaskResponseBodyResultObject = None,
    ):
        # Request ID
        self.request_id = request_id
        # Returned object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.CreateAnalysisExportTaskResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class CreateAnalysisExportTaskResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        columns: str = None,
        conditions: str = None,
        event_begin_time: int = None,
        event_codes: str = None,
        event_end_time: int = None,
        file_format: str = None,
        oss_key: str = None,
        scope: str = None,
        status: str = None,
        type: str = None,
        user_id: int = None,
    ):
        # Export list.
        self.columns = columns
        # Export task conditions.
        self.conditions = conditions
        # Event start time.
        self.event_begin_time = event_begin_time
        # Event code.
        self.event_codes = event_codes
        # End time.
        self.event_end_time = event_end_time
        # File format.
        self.file_format = file_format
        # OSS-generated key.
        self.oss_key = oss_key
        # Export task scope.
        self.scope = scope
        # Task status.
        self.status = status
        # Export task type.
        self.type = type
        # User UID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.columns is not None:
            result['columns'] = self.columns

        if self.conditions is not None:
            result['conditions'] = self.conditions

        if self.event_begin_time is not None:
            result['eventBeginTime'] = self.event_begin_time

        if self.event_codes is not None:
            result['eventCodes'] = self.event_codes

        if self.event_end_time is not None:
            result['eventEndTime'] = self.event_end_time

        if self.file_format is not None:
            result['fileFormat'] = self.file_format

        if self.oss_key is not None:
            result['ossKey'] = self.oss_key

        if self.scope is not None:
            result['scope'] = self.scope

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columns') is not None:
            self.columns = m.get('columns')

        if m.get('conditions') is not None:
            self.conditions = m.get('conditions')

        if m.get('eventBeginTime') is not None:
            self.event_begin_time = m.get('eventBeginTime')

        if m.get('eventCodes') is not None:
            self.event_codes = m.get('eventCodes')

        if m.get('eventEndTime') is not None:
            self.event_end_time = m.get('eventEndTime')

        if m.get('fileFormat') is not None:
            self.file_format = m.get('fileFormat')

        if m.get('ossKey') is not None:
            self.oss_key = m.get('ossKey')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

