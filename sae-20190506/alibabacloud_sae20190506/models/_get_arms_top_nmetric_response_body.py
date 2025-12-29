# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class GetArmsTopNMetricResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetArmsTopNMetricResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The following limits are imposed on the ID:
        # 
        # *   **2xx**: The call was successful.
        # *   **3xx**: The call was redirected.
        # *   **4xx**: The call failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The details of applications.
        self.data = data
        # The request ID.
        self.message = message
        # 3B763F98-0BA2-5C23-B6B8-558568D2C1C2
        self.request_id = request_id
        # Indicates whether the list of applications was obtained. The following limits are imposed on the ID:
        # 
        # *   **true**: The namespaces were obtained.
        # *   **false**: no
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
                temp_model = main_models.GetArmsTopNMetricResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetArmsTopNMetricResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        count: int = None,
        error: int = None,
        name: str = None,
        region_id: str = None,
        rt: int = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The total number of requests.
        self.count = count
        # The number of errors.
        self.error = error
        # The application name.
        self.name = name
        # The namespace ID.
        self.region_id = region_id
        # The average response time. Unit: milliseconds.
        self.rt = rt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.count is not None:
            result['Count'] = self.count

        if self.error is not None:
            result['Error'] = self.error

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rt is not None:
            result['Rt'] = self.rt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Rt') is not None:
            self.rt = m.get('Rt')

        return self

