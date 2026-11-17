# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetKnowledgeBaseBuildTaskResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetKnowledgeBaseBuildTaskResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business error code, which is used to determine the error type when the request fails.
        self.code = code
        # The business data returned when the request is successful.
        self.data = data
        # The error message returned when the request fails.
        self.message = message
        # The unique identifier of the request, which can be used for troubleshooting.
        self.request_id = request_id
        # Indicates whether the request is successful.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetKnowledgeBaseBuildTaskResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetKnowledgeBaseBuildTaskResultResponseBodyData(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        expires_in: int = None,
        knowledge_base_id: str = None,
        task_instance_id: str = None,
    ):
        # The temporary Object Storage Service (OSS) download URL issued to the current caller when this operation is called. The URL is not stored.
        self.download_url = download_url
        # The validity period of the download URL, in seconds. Request a new URL after it expires.
        self.expires_in = expires_in
        # The ID of the knowledge base to which the result belongs.
        self.knowledge_base_id = knowledge_base_id
        # The ID of the task instance that produced the result.
        self.task_instance_id = task_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.expires_in is not None:
            result['ExpiresIn'] = self.expires_in

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.task_instance_id is not None:
            result['TaskInstanceId'] = self.task_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('ExpiresIn') is not None:
            self.expires_in = m.get('ExpiresIn')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('TaskInstanceId') is not None:
            self.task_instance_id = m.get('TaskInstanceId')

        return self

