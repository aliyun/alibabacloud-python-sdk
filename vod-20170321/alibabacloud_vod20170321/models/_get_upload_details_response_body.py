# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetUploadDetailsResponseBody(DaraModel):
    def __init__(
        self,
        forbidden_media_ids: List[str] = None,
        non_exist_media_ids: List[str] = None,
        request_id: str = None,
        upload_details: List[main_models.GetUploadDetailsResponseBodyUploadDetails] = None,
    ):
        # The IDs of the media files that cannot be accessed.
        self.forbidden_media_ids = forbidden_media_ids
        # The IDs of the media files that do not exist.
        self.non_exist_media_ids = non_exist_media_ids
        # The ID of the request.
        self.request_id = request_id
        # The upload details.
        self.upload_details = upload_details

    def validate(self):
        if self.upload_details:
            for v1 in self.upload_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forbidden_media_ids is not None:
            result['ForbiddenMediaIds'] = self.forbidden_media_ids

        if self.non_exist_media_ids is not None:
            result['NonExistMediaIds'] = self.non_exist_media_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UploadDetails'] = []
        if self.upload_details is not None:
            for k1 in self.upload_details:
                result['UploadDetails'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForbiddenMediaIds') is not None:
            self.forbidden_media_ids = m.get('ForbiddenMediaIds')

        if m.get('NonExistMediaIds') is not None:
            self.non_exist_media_ids = m.get('NonExistMediaIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.upload_details = []
        if m.get('UploadDetails') is not None:
            for k1 in m.get('UploadDetails'):
                temp_model = main_models.GetUploadDetailsResponseBodyUploadDetails()
                self.upload_details.append(temp_model.from_map(k1))

        return self

class GetUploadDetailsResponseBodyUploadDetails(DaraModel):
    def __init__(
        self,
        completion_time: str = None,
        creation_time: str = None,
        device_model: str = None,
        file_size: int = None,
        media_id: str = None,
        modification_time: str = None,
        status: str = None,
        title: str = None,
        upload_ip: str = None,
        upload_ratio: float = None,
        upload_size: int = None,
        upload_source: str = None,
        upload_status: str = None,
    ):
        # The time when the upload job was complete. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.completion_time = completion_time
        # The time when the upload job was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The device model.
        self.device_model = device_model
        # The size of the uploaded file. Unit: byte.
        self.file_size = file_size
        # The ID of the uploaded audio or video.
        self.media_id = media_id
        # The time when the information about the media file was updated. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.modification_time = modification_time
        # The status of the video. For more information about the valid values and value description of the parameter, see the "Status: the status of a video" section of the [Basic structures](https://help.aliyun.com/document_detail/52839.html) topic.
        self.status = status
        # The title of the media file.
        self.title = title
        # The IP address of the server that uploads the media file.
        self.upload_ip = upload_ip
        # The upload ratio.
        self.upload_ratio = upload_ratio
        # The upload size. Unit: byte.
        self.upload_size = upload_size
        # The method that is used to upload the media file.
        self.upload_source = upload_source
        # The status of the upload job. For more information about the valid values and value description of the parameter, see the "Status: the status of a URL-based upload job" section of the [Basic structures](https://help.aliyun.com/document_detail/52839.html) topic.
        self.upload_status = upload_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.device_model is not None:
            result['DeviceModel'] = self.device_model

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        if self.upload_ip is not None:
            result['UploadIP'] = self.upload_ip

        if self.upload_ratio is not None:
            result['UploadRatio'] = self.upload_ratio

        if self.upload_size is not None:
            result['UploadSize'] = self.upload_size

        if self.upload_source is not None:
            result['UploadSource'] = self.upload_source

        if self.upload_status is not None:
            result['UploadStatus'] = self.upload_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UploadIP') is not None:
            self.upload_ip = m.get('UploadIP')

        if m.get('UploadRatio') is not None:
            self.upload_ratio = m.get('UploadRatio')

        if m.get('UploadSize') is not None:
            self.upload_size = m.get('UploadSize')

        if m.get('UploadSource') is not None:
            self.upload_source = m.get('UploadSource')

        if m.get('UploadStatus') is not None:
            self.upload_status = m.get('UploadStatus')

        return self

