# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class CreateVideoCreationTaskRequest(DaraModel):
    def __init__(
        self,
        creation_instruction: main_models.CreateVideoCreationTaskRequestCreationInstruction = None,
        file_info: main_models.CreateVideoCreationTaskRequestFileInfo = None,
        image_detection_task_id: str = None,
        request_id: str = None,
        user_id: str = None,
    ):
        self.creation_instruction = creation_instruction
        self.file_info = file_info
        # This parameter is required.
        self.image_detection_task_id = image_detection_task_id
        # This parameter is required.
        self.request_id = request_id
        self.user_id = user_id

    def validate(self):
        if self.creation_instruction:
            self.creation_instruction.validate()
        if self.file_info:
            self.file_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_instruction is not None:
            result['creationInstruction'] = self.creation_instruction.to_map()

        if self.file_info is not None:
            result['fileInfo'] = self.file_info.to_map()

        if self.image_detection_task_id is not None:
            result['imageDetectionTaskId'] = self.image_detection_task_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creationInstruction') is not None:
            temp_model = main_models.CreateVideoCreationTaskRequestCreationInstruction()
            self.creation_instruction = temp_model.from_map(m.get('creationInstruction'))

        if m.get('fileInfo') is not None:
            temp_model = main_models.CreateVideoCreationTaskRequestFileInfo()
            self.file_info = temp_model.from_map(m.get('fileInfo'))

        if m.get('imageDetectionTaskId') is not None:
            self.image_detection_task_id = m.get('imageDetectionTaskId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class CreateVideoCreationTaskRequestFileInfo(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        file_name: str = None,
        file_trace_id: str = None,
        oss_key: str = None,
    ):
        self.file_id = file_id
        self.file_name = file_name
        self.file_trace_id = file_trace_id
        self.oss_key = oss_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['fileId'] = self.file_id

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_trace_id is not None:
            result['fileTraceId'] = self.file_trace_id

        if self.oss_key is not None:
            result['ossKey'] = self.oss_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileTraceId') is not None:
            self.file_trace_id = m.get('fileTraceId')

        if m.get('ossKey') is not None:
            self.oss_key = m.get('ossKey')

        return self

class CreateVideoCreationTaskRequestCreationInstruction(DaraModel):
    def __init__(
        self,
        instruction: str = None,
        template_id: str = None,
    ):
        self.instruction = instruction
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instruction is not None:
            result['instruction'] = self.instruction

        if self.template_id is not None:
            result['templateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        return self

