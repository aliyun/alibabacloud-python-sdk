# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DeleteImagesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DeleteImagesResponseBodyData = None,
        request_id: str = None,
    ):
        # The images.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DeleteImagesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DeleteImagesResponseBodyData(DaraModel):
    def __init__(
        self,
        fail_delete_image_ids: List[str] = None,
        success_delete_image_ids: List[str] = None,
    ):
        # The IDs of the images that failed to be deleted.
        self.fail_delete_image_ids = fail_delete_image_ids
        # The IDs of the images that are successfully deleted.
        self.success_delete_image_ids = success_delete_image_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_delete_image_ids is not None:
            result['FailDeleteImageIds'] = self.fail_delete_image_ids

        if self.success_delete_image_ids is not None:
            result['SuccessDeleteImageIds'] = self.success_delete_image_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailDeleteImageIds') is not None:
            self.fail_delete_image_ids = m.get('FailDeleteImageIds')

        if m.get('SuccessDeleteImageIds') is not None:
            self.success_delete_image_ids = m.get('SuccessDeleteImageIds')

        return self

