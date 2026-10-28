# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class GetSparkAppLogResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetSparkAppLogResponseBodyData = None,
        request_id: str = None,
    ):
        # The log details.
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
            temp_model = main_models.GetSparkAppLogResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSparkAppLogResponseBodyData(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        log_content: str = None,
        log_size: int = None,
        message: str = None,
    ):
        # <props="china">The ID of the Enterprise Edition, Basic Edition, or Data Lakehouse Edition cluster.
        # <props="intl">The ID of the Data Lakehouse Edition cluster.
        self.dbcluster_id = dbcluster_id
        # The log content.
        self.log_content = log_content
        # The number of log lines. A value of 0 indicates that no valid logs exist.
        self.log_size = log_size
        # The alert information, such as task execution failure or insufficient resources. If no alerts are triggered, an empty value is returned.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.log_content is not None:
            result['LogContent'] = self.log_content

        if self.log_size is not None:
            result['LogSize'] = self.log_size

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('LogContent') is not None:
            self.log_content = m.get('LogContent')

        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

