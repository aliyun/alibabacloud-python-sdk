# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetAIImageJobsResponseBody(DaraModel):
    def __init__(
        self,
        aiimage_job_list: List[main_models.GetAIImageJobsResponseBodyAIImageJobList] = None,
        request_id: str = None,
    ):
        # The image AI processing jobs.
        self.aiimage_job_list = aiimage_job_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.aiimage_job_list:
            for v1 in self.aiimage_job_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AIImageJobList'] = []
        if self.aiimage_job_list is not None:
            for k1 in self.aiimage_job_list:
                result['AIImageJobList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aiimage_job_list = []
        if m.get('AIImageJobList') is not None:
            for k1 in m.get('AIImageJobList'):
                temp_model = main_models.GetAIImageJobsResponseBodyAIImageJobList()
                self.aiimage_job_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAIImageJobsResponseBodyAIImageJobList(DaraModel):
    def __init__(
        self,
        aiimage_result: str = None,
        code: str = None,
        creation_time: str = None,
        job_id: str = None,
        message: str = None,
        status: str = None,
        template_config: str = None,
        template_id: str = None,
        user_data: str = None,
        video_id: str = None,
    ):
        # The Object Storage Service (OSS) URL of the image file.
        # 
        # > This parameter does not include the complete authentication information. To obtain the authentication information, you must generate a signed URL. Alternatively, you can call the [ListAIImageInfo](~~ListAIImageInfo~~) operation to obtain the image information.
        self.aiimage_result = aiimage_result
        # The error code.
        self.code = code
        # The time when the image AI processing job was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The ID of the image AI processing job.
        self.job_id = job_id
        # The error message.
        self.message = message
        # The status of the job. Valid values:
        # 
        # *   **success**
        # *   **fail**
        self.status = status
        # The configurations of the AI template that was used to submit the job.
        self.template_config = template_config
        # The ID of the AI template.
        self.template_id = template_id
        # The user data.
        # 
        # *   The value must be a JSON string.
        # *   The MessageCallback or Extend parameter is returned.
        # *   The value contains a maximum of 512 bytes.
        # 
        # For more information, see the "UserData: specifies the custom configurations for media upload" section of the [Request parameters](https://help.aliyun.com/document_detail/86952.html) topic.
        self.user_data = user_data
        # The ID of the video.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aiimage_result is not None:
            result['AIImageResult'] = self.aiimage_result

        if self.code is not None:
            result['Code'] = self.code

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.message is not None:
            result['Message'] = self.message

        if self.status is not None:
            result['Status'] = self.status

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIImageResult') is not None:
            self.aiimage_result = m.get('AIImageResult')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

