# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class UpdatePrometheusGlobalViewResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.UpdatePrometheusGlobalViewResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned struct.
        self.data = data
        # The error message that is returned if the request failed.
        self.message = message
        # The ID of the request. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.UpdatePrometheusGlobalViewResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdatePrometheusGlobalViewResponseBodyData(DaraModel):
    def __init__(
        self,
        failed_instances: List[main_models.UpdatePrometheusGlobalViewResponseBodyDataFailedInstances] = None,
        success: bool = None,
    ):
        # The data sources that failed to be updated.
        self.failed_instances = failed_instances
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`
        # *   `false`
        self.success = success

    def validate(self):
        if self.failed_instances:
            for v1 in self.failed_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailedInstances'] = []
        if self.failed_instances is not None:
            for k1 in self.failed_instances:
                result['FailedInstances'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_instances = []
        if m.get('FailedInstances') is not None:
            for k1 in m.get('FailedInstances'):
                temp_model = main_models.UpdatePrometheusGlobalViewResponseBodyDataFailedInstances()
                self.failed_instances.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdatePrometheusGlobalViewResponseBodyDataFailedInstances(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        source_name: str = None,
        source_type: str = None,
        user_id: str = None,
    ):
        # The ID of the Prometheus instance.
        self.cluster_id = cluster_id
        # The name of the data source.
        self.source_name = source_name
        # The type of the data source. AlibabaPrometheus MetricStore CustomPrometheus
        self.source_type = source_type
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.source_name is not None:
            result['SourceName'] = self.source_name

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

