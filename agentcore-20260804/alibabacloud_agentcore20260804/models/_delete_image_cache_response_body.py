# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class DeleteImageCacheResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DeleteImageCacheResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business response code.
        # 
        # This parameter is required.
        self.code = code
        # The result of deleting the image cache.
        # 
        # This parameter is required.
        self.data = data
        # The HTTP status code.
        # 
        # This parameter is required.
        self.http_status_code = http_status_code
        # The response message.
        # 
        # This parameter is required.
        self.message = message
        # The request ID, which is used for troubleshooting.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Indicates whether the request is successful. This does not mean that the cache creation is complete.
        # 
        # This parameter is required.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.DeleteImageCacheResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class DeleteImageCacheResponseBodyData(DaraModel):
    def __init__(
        self,
        deletion_pending: bool = None,
        image_id: str = None,
    ):
        # Indicates whether the deletion is still in progress. A value of true indicates that the deletion is accepted but not yet complete, and a Get request returns DELETING until ImageCacheNotFound is explicitly returned. A value of false indicates that the current workspace is deleted or no longer exists.
        # 
        # This parameter is required.
        self.deletion_pending = deletion_pending
        # The image cache ID, which matches the request. The requested ID is still returned even if the current workspace no longer exists.
        # 
        # This parameter is required.
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deletion_pending is not None:
            result['deletionPending'] = self.deletion_pending

        if self.image_id is not None:
            result['imageId'] = self.image_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deletionPending') is not None:
            self.deletion_pending = m.get('deletionPending')

        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')

        return self

