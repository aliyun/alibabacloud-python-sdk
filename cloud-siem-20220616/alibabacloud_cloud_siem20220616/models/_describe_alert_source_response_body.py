# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeAlertSourceResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.DescribeAlertSourceResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeAlertSourceResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeAlertSourceResponseBodyData(DaraModel):
    def __init__(
        self,
        modules: List[str] = None,
        source: str = None,
        source_name: str = None,
    ):
        self.modules = modules
        # The internal code of the alert data source.
        self.source = source
        # The name of the alert data source.
        self.source_name = source_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.modules is not None:
            result['Modules'] = self.modules

        if self.source is not None:
            result['Source'] = self.source

        if self.source_name is not None:
            result['SourceName'] = self.source_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Modules') is not None:
            self.modules = m.get('Modules')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')

        return self

