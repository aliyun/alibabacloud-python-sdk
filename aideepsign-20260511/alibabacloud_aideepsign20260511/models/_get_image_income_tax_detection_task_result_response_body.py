# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aideepsign20260511 import models as main_models
from darabonba.model import DaraModel

class GetImageIncomeTaxDetectionTaskResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.GetImageIncomeTaxDetectionTaskResultResponseBodyItems] = None,
        message: str = None,
        request_id: str = None,
        result: str = None,
        status: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # **The business error code.** The value "OK" is returned if the request is successful.
        self.code = code
        # **The HTTP status code.** The value 200 is returned if the request is successful.
        self.http_status_code = http_status_code
        # **The list of detected abnormal items.** Returned only when `Status` is `succeeded`. An empty array indicates that no abnormal items are detected.
        self.items = items
        # The failure reason when the task fails.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The raw downstream detection result (extend.result string) for troubleshooting and passing through new fields.
        self.result = result
        # **The task status.** Valid values: `running` (in progress), `succeeded` (completed), `failed` (failed).
        self.status = status
        # Indicates whether the request was successful.
        self.success = success
        # **The task ID.**
        self.task_id = task_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.GetImageIncomeTaxDetectionTaskResultResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class GetImageIncomeTaxDetectionTaskResultResponseBodyItems(DaraModel):
    def __init__(
        self,
        abnormal_item: str = None,
        coordinates: List[main_models.GetImageIncomeTaxDetectionTaskResultResponseBodyItemsCoordinates] = None,
        stage: str = None,
    ):
        # The text description of the abnormal item.
        self.abnormal_item = abnormal_item
        # The bounding box position of the abnormal item in the image. May be an empty array for image-wide abnormalities.
        self.coordinates = coordinates
        # The detection stage identifier for the abnormality.
        self.stage = stage

    def validate(self):
        if self.coordinates:
            for v1 in self.coordinates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abnormal_item is not None:
            result['AbnormalItem'] = self.abnormal_item

        result['Coordinates'] = []
        if self.coordinates is not None:
            for k1 in self.coordinates:
                result['Coordinates'].append(k1.to_map() if k1 else None)

        if self.stage is not None:
            result['Stage'] = self.stage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalItem') is not None:
            self.abnormal_item = m.get('AbnormalItem')

        self.coordinates = []
        if m.get('Coordinates') is not None:
            for k1 in m.get('Coordinates'):
                temp_model = main_models.GetImageIncomeTaxDetectionTaskResultResponseBodyItemsCoordinates()
                self.coordinates.append(temp_model.from_map(k1))

        if m.get('Stage') is not None:
            self.stage = m.get('Stage')

        return self

class GetImageIncomeTaxDetectionTaskResultResponseBodyItemsCoordinates(DaraModel):
    def __init__(
        self,
        x_1: int = None,
        x_2: int = None,
        y_1: int = None,
        y_2: int = None,
    ):
        # The X-coordinate of the upper-left corner (pixels).
        self.x_1 = x_1
        # The X-coordinate of the lower-right corner of the bounding box (pixels).
        self.x_2 = x_2
        # The Y-coordinate of the upper-left corner (pixels).
        self.y_1 = y_1
        # The Y-coordinate of the lower-right corner of the bounding box (pixels).
        self.y_2 = y_2

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_1 is not None:
            result['X1'] = self.x_1

        if self.x_2 is not None:
            result['X2'] = self.x_2

        if self.y_1 is not None:
            result['Y1'] = self.y_1

        if self.y_2 is not None:
            result['Y2'] = self.y_2

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X1') is not None:
            self.x_1 = m.get('X1')

        if m.get('X2') is not None:
            self.x_2 = m.get('X2')

        if m.get('Y1') is not None:
            self.y_1 = m.get('Y1')

        if m.get('Y2') is not None:
            self.y_2 = m.get('Y2')

        return self

