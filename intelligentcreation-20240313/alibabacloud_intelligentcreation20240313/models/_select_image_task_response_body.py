# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class SelectImageTaskResponseBody(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        failed: str = None,
        generation_source: str = None,
        gmt_create: str = None,
        image_infos: List[main_models.SelectImageTaskResponseBodyImageInfos] = None,
        request_id: str = None,
        scene: str = None,
        status: str = None,
        subtask_processing: str = None,
        success: str = None,
        total: str = None,
    ):
        self.error_message = error_message
        self.failed = failed
        self.generation_source = generation_source
        self.gmt_create = gmt_create
        self.image_infos = image_infos
        # Id of the request
        self.request_id = request_id
        self.scene = scene
        self.status = status
        self.subtask_processing = subtask_processing
        self.success = success
        self.total = total

    def validate(self):
        if self.image_infos:
            for v1 in self.image_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.failed is not None:
            result['failed'] = self.failed

        if self.generation_source is not None:
            result['generationSource'] = self.generation_source

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        result['imageInfos'] = []
        if self.image_infos is not None:
            for k1 in self.image_infos:
                result['imageInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.scene is not None:
            result['scene'] = self.scene

        if self.status is not None:
            result['status'] = self.status

        if self.subtask_processing is not None:
            result['subtaskProcessing'] = self.subtask_processing

        if self.success is not None:
            result['success'] = self.success

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('failed') is not None:
            self.failed = m.get('failed')

        if m.get('generationSource') is not None:
            self.generation_source = m.get('generationSource')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        self.image_infos = []
        if m.get('imageInfos') is not None:
            for k1 in m.get('imageInfos'):
                temp_model = main_models.SelectImageTaskResponseBodyImageInfos()
                self.image_infos.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scene') is not None:
            self.scene = m.get('scene')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('subtaskProcessing') is not None:
            self.subtask_processing = m.get('subtaskProcessing')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class SelectImageTaskResponseBodyImageInfos(DaraModel):
    def __init__(
        self,
        custom_image_url: str = None,
        gmt_create: str = None,
        image_h: str = None,
        image_w: str = None,
    ):
        self.custom_image_url = custom_image_url
        self.gmt_create = gmt_create
        self.image_h = image_h
        self.image_w = image_w

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_image_url is not None:
            result['customImageUrl'] = self.custom_image_url

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.image_h is not None:
            result['imageH'] = self.image_h

        if self.image_w is not None:
            result['imageW'] = self.image_w

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customImageUrl') is not None:
            self.custom_image_url = m.get('customImageUrl')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('imageH') is not None:
            self.image_h = m.get('imageH')

        if m.get('imageW') is not None:
            self.image_w = m.get('imageW')

        return self

