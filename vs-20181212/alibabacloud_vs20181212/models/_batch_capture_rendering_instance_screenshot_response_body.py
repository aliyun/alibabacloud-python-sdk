# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class BatchCaptureRenderingInstanceScreenshotResponseBody(DaraModel):
    def __init__(
        self,
        datatest: main_models.BatchCaptureRenderingInstanceScreenshotResponseBodyDatatest = None,
        failed_count: int = None,
        failed_items: List[main_models.BatchCaptureRenderingInstanceScreenshotResponseBodyFailedItems] = None,
        request_id: str = None,
        success_count: int = None,
        success_items: List[main_models.BatchCaptureRenderingInstanceScreenshotResponseBodySuccessItems] = None,
    ):
        # The dry run result.
        self.datatest = datatest
        # The number of failed instances.
        self.failed_count = failed_count
        # The list of instances for which screenshots failed.
        self.failed_items = failed_items
        # Id of the request
        self.request_id = request_id
        # The number of successful instances.
        self.success_count = success_count
        # The list of successful instances.
        self.success_items = success_items

    def validate(self):
        if self.datatest:
            self.datatest.validate()
        if self.failed_items:
            for v1 in self.failed_items:
                 if v1:
                    v1.validate()
        if self.success_items:
            for v1 in self.success_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.datatest is not None:
            result['Datatest'] = self.datatest.to_map()

        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        result['FailedItems'] = []
        if self.failed_items is not None:
            for k1 in self.failed_items:
                result['FailedItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        result['SuccessItems'] = []
        if self.success_items is not None:
            for k1 in self.success_items:
                result['SuccessItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Datatest') is not None:
            temp_model = main_models.BatchCaptureRenderingInstanceScreenshotResponseBodyDatatest()
            self.datatest = temp_model.from_map(m.get('Datatest'))

        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        self.failed_items = []
        if m.get('FailedItems') is not None:
            for k1 in m.get('FailedItems'):
                temp_model = main_models.BatchCaptureRenderingInstanceScreenshotResponseBodyFailedItems()
                self.failed_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        self.success_items = []
        if m.get('SuccessItems') is not None:
            for k1 in m.get('SuccessItems'):
                temp_model = main_models.BatchCaptureRenderingInstanceScreenshotResponseBodySuccessItems()
                self.success_items.append(temp_model.from_map(k1))

        return self

class BatchCaptureRenderingInstanceScreenshotResponseBodySuccessItems(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        download_url: str = None,
        rendering_instance_id: str = None,
    ):
        # The time when the screenshot was created.
        self.creation_time = creation_time
        # The download URL of the screenshot.
        self.download_url = download_url
        # The instance ID of the cloud application service instance.
        self.rendering_instance_id = rendering_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self

class BatchCaptureRenderingInstanceScreenshotResponseBodyFailedItems(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        rendering_instance_id: str = None,
    ):
        # The error code of the failure.
        self.err_code = err_code
        # The error message of the failure.
        self.err_message = err_message
        # The instance ID of the cloud application service instance.
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

class BatchCaptureRenderingInstanceScreenshotResponseBodyDatatest(DaraModel):
    def __init__(
        self,
        result: main_models.BatchCaptureRenderingInstanceScreenshotResponseBodyDatatestResult = None,
    ):
        # The dry run result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            temp_model = main_models.BatchCaptureRenderingInstanceScreenshotResponseBodyDatatestResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class BatchCaptureRenderingInstanceScreenshotResponseBodyDatatestResult(DaraModel):
    def __init__(
        self,
        success_count: int = None,
    ):
        # The number of successful instances.
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        return self

