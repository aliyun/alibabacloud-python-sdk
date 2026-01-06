# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class SetSparkAppLogRootPathResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.SetSparkAppLogRootPathResponseBodyData = None,
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
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.SetSparkAppLogRootPathResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SetSparkAppLogRootPathResponseBodyData(DaraModel):
    def __init__(
        self,
        default_log_path: str = None,
        is_log_path_exists: bool = None,
        modified_timestamp: str = None,
        modified_uid: str = None,
        recorded_log_path: str = None,
    ):
        # The default log path.
        self.default_log_path = default_log_path
        # Indicates whether a log path exists.
        self.is_log_path_exists = is_log_path_exists
        # The last modification time.
        self.modified_timestamp = modified_timestamp
        # The modifier ID.
        self.modified_uid = modified_uid
        # The recorded log path.
        self.recorded_log_path = recorded_log_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_log_path is not None:
            result['DefaultLogPath'] = self.default_log_path

        if self.is_log_path_exists is not None:
            result['IsLogPathExists'] = self.is_log_path_exists

        if self.modified_timestamp is not None:
            result['ModifiedTimestamp'] = self.modified_timestamp

        if self.modified_uid is not None:
            result['ModifiedUid'] = self.modified_uid

        if self.recorded_log_path is not None:
            result['RecordedLogPath'] = self.recorded_log_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultLogPath') is not None:
            self.default_log_path = m.get('DefaultLogPath')

        if m.get('IsLogPathExists') is not None:
            self.is_log_path_exists = m.get('IsLogPathExists')

        if m.get('ModifiedTimestamp') is not None:
            self.modified_timestamp = m.get('ModifiedTimestamp')

        if m.get('ModifiedUid') is not None:
            self.modified_uid = m.get('ModifiedUid')

        if m.get('RecordedLogPath') is not None:
            self.recorded_log_path = m.get('RecordedLogPath')

        return self

