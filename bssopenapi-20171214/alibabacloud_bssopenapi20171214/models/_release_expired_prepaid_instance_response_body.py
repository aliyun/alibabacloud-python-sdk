# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class ReleaseExpiredPrepaidInstanceResponseBody(DaraModel):
    def __init__(
        self,
        class_: str = None,
        code: str = None,
        data: main_models.ReleaseExpiredPrepaidInstanceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # **[Deprecated]** The field is deprecated.
        self.class_ = class_
        # The error code returned when the call fails. For more information, see Error codes.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_ is not None:
            result['Class'] = self.class_

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ReleaseExpiredPrepaidInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ReleaseExpiredPrepaidInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        host_id: str = None,
        instance_results: List[main_models.ReleaseExpiredPrepaidInstanceResponseBodyDataInstanceResults] = None,
        release_result: bool = None,
    ):
        # **[Deprecated]** The field is deprecated.
        self.host_id = host_id
        # The list of instance results.
        self.instance_results = instance_results
        # Indicates whether the release operation is successful.
        self.release_result = release_result

    def validate(self):
        if self.instance_results:
            for v1 in self.instance_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_id is not None:
            result['HostId'] = self.host_id

        result['InstanceResults'] = []
        if self.instance_results is not None:
            for k1 in self.instance_results:
                result['InstanceResults'].append(k1.to_map() if k1 else None)

        if self.release_result is not None:
            result['ReleaseResult'] = self.release_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        self.instance_results = []
        if m.get('InstanceResults') is not None:
            for k1 in m.get('InstanceResults'):
                temp_model = main_models.ReleaseExpiredPrepaidInstanceResponseBodyDataInstanceResults()
                self.instance_results.append(temp_model.from_map(k1))

        if m.get('ReleaseResult') is not None:
            self.release_result = m.get('ReleaseResult')

        return self

class ReleaseExpiredPrepaidInstanceResponseBodyDataInstanceResults(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        success: bool = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # Indicates whether the operation is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

