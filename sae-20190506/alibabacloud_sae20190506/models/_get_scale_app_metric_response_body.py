# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class GetScaleAppMetricResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetScaleAppMetricResponseBodyData] = None,
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
        # The additional information that is returned. The following limits are imposed on the ID:
        # 
        # *   success: If the call is successful, **success** is returned.
        # *   An error code: If the call fails, an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the microservice list was obtained. The following limits are imposed on the ID:
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
                temp_model = main_models.GetScaleAppMetricResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetScaleAppMetricResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        max_replicas: int = None,
        name: str = None,
        region_id: str = None,
        runnings: int = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The maximum number of instances.
        self.max_replicas = max_replicas
        # The application name.
        self.name = name
        # The namespace ID.
        self.region_id = region_id
        # The current number of instances.
        self.runnings = runnings

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.runnings is not None:
            result['Runnings'] = self.runnings

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Runnings') is not None:
            self.runnings = m.get('Runnings')

        return self

