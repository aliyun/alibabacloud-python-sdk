# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetImageTestResultResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        test_result: main_models.GetImageTestResultResponseBodyTestResult = None,
    ):
        # The request ID, which is used to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The details of the image test result.
        self.test_result = test_result

    def validate(self):
        if self.test_result:
            self.test_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.test_result is not None:
            result['TestResult'] = self.test_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TestResult') is not None:
            temp_model = main_models.GetImageTestResultResponseBodyTestResult()
            self.test_result = temp_model.from_map(m.get('TestResult'))

        return self

class GetImageTestResultResponseBodyTestResult(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        message: str = None,
        operate_time: int = None,
        process_id: str = None,
        publish_stage: str = None,
        resource_group_id: int = None,
        status: str = None,
    ):
        # The image ID.
        self.image_id = image_id
        # The test result message.
        self.message = message
        # The operation time, represented as a 64-bit timestamp.
        self.operate_time = operate_time
        # The process ID.
        self.process_id = process_id
        # The image publish status. Valid values:
        # - Untest: Not tested.
        # - Testing: Testing in progress.
        # - TestFailed: Test failed.
        # - Unpublished: Not published.
        # - Publishing: Publishing in progress.
        # - Published: Published.
        # - PublishFailed: Publish failed.
        # - Building: Building in progress.
        # - BuildSuccess: Build succeeded.
        # - BuildFailed: Build failed.
        # - Accelerating: Acceleration in progress.
        # - AccelerateSuccess: Acceleration succeeded.
        # - AccelerateFailed: Acceleration failed.
        self.publish_stage = publish_stage
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The test process status. Valid values:
        # - running: Running.
        # - completed: Completed.
        # - failed: Failed.
        # - cancelled: Cancelled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.message is not None:
            result['Message'] = self.message

        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.publish_stage is not None:
            result['PublishStage'] = self.publish_stage

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('PublishStage') is not None:
            self.publish_stage = m.get('PublishStage')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

