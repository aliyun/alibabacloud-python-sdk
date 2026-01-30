# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class RebootRenderingServerResponseBody(DaraModel):
    def __init__(
        self,
        failed_instance_count: int = None,
        failed_instances: List[main_models.RebootRenderingServerResponseBodyFailedInstances] = None,
        request_id: str = None,
        success_instance_count: int = None,
        success_instances: List[main_models.RebootRenderingServerResponseBodySuccessInstances] = None,
    ):
        self.failed_instance_count = failed_instance_count
        self.failed_instances = failed_instances
        self.request_id = request_id
        self.success_instance_count = success_instance_count
        self.success_instances = success_instances

    def validate(self):
        if self.failed_instances:
            for v1 in self.failed_instances:
                 if v1:
                    v1.validate()
        if self.success_instances:
            for v1 in self.success_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_instance_count is not None:
            result['FailedInstanceCount'] = self.failed_instance_count

        result['FailedInstances'] = []
        if self.failed_instances is not None:
            for k1 in self.failed_instances:
                result['FailedInstances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success_instance_count is not None:
            result['SuccessInstanceCount'] = self.success_instance_count

        result['SuccessInstances'] = []
        if self.success_instances is not None:
            for k1 in self.success_instances:
                result['SuccessInstances'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedInstanceCount') is not None:
            self.failed_instance_count = m.get('FailedInstanceCount')

        self.failed_instances = []
        if m.get('FailedInstances') is not None:
            for k1 in m.get('FailedInstances'):
                temp_model = main_models.RebootRenderingServerResponseBodyFailedInstances()
                self.failed_instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuccessInstanceCount') is not None:
            self.success_instance_count = m.get('SuccessInstanceCount')

        self.success_instances = []
        if m.get('SuccessInstances') is not None:
            for k1 in m.get('SuccessInstances'):
                temp_model = main_models.RebootRenderingServerResponseBodySuccessInstances()
                self.success_instances.append(temp_model.from_map(k1))

        return self

class RebootRenderingServerResponseBodySuccessInstances(DaraModel):
    def __init__(
        self,
        rendering_instance_id: str = None,
    ):
        self.rendering_instance_id = rendering_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self

class RebootRenderingServerResponseBodyFailedInstances(DaraModel):
    def __init__(
        self,
        err_code: int = None,
        err_message: str = None,
        rendering_instance_id: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.rendering_instance_id = rendering_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self

