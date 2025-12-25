# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeApiExportsResponseBody(DaraModel):
    def __init__(
        self,
        api_exports: List[main_models.DescribeApiExportsResponseBodyApiExports] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The returned data export tasks.
        self.api_exports = api_exports
        # The request ID.
        self.request_id = request_id
        # The status of the data export task. Valid values:
        # 
        # *   **expired**: The file is expired.
        # *   **exporting**: Data is being exported.
        # *   **completed**: Data is exported.
        self.total = total

    def validate(self):
        if self.api_exports:
            for v1 in self.api_exports:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiExports'] = []
        if self.api_exports is not None:
            for k1 in self.api_exports:
                result['ApiExports'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_exports = []
        if m.get('ApiExports') is not None:
            for k1 in m.get('ApiExports'):
                temp_model = main_models.DescribeApiExportsResponseBodyApiExports()
                self.api_exports.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeApiExportsResponseBodyApiExports(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        file_name: str = None,
        file_url: str = None,
        format: str = None,
        status: str = None,
        type: str = None,
    ):
        # The time when the data export task was created. The value is a UNIX timestamp displayed in UTC. Unit: seconds.
        self.create_time = create_time
        # The name of the file.
        self.file_name = file_name
        # The download URL of the exported file.
        self.file_url = file_url
        # The format of the exported file.
        self.format = format
        # The status of the data export task. Valid values:
        # 
        # * **expired**: The file is expired.
        # 
        # * **exporting**: Data is being exported.
        # 
        # * **completed**: Data is exported.
        self.status = status
        # The type of the data export task. Valid values:
        # 
        # * **apisec_api**: API tasks
        # 
        # * **apisec_abnormal**: API risk tasks
        # 
        # * **apisec_event**: API security event tasks
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.format is not None:
            result['Format'] = self.format

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

