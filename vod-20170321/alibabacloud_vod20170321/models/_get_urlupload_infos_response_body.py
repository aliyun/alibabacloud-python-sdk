# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetURLUploadInfosResponseBody(DaraModel):
    def __init__(
        self,
        non_exists: List[str] = None,
        request_id: str = None,
        urlupload_info_list: List[main_models.GetURLUploadInfosResponseBodyURLUploadInfoList] = None,
    ):
        # The job IDs or upload URLs that do not exist.
        self.non_exists = non_exists
        # The ID of the request.
        self.request_id = request_id
        # The information about URL-based upload jobs. For more information, see the "URLUploadInfo: the information about a URL-based upload job" section of the [Basic structures](https://help.aliyun.com/document_detail/52839.html) topic.
        self.urlupload_info_list = urlupload_info_list

    def validate(self):
        if self.urlupload_info_list:
            for v1 in self.urlupload_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.non_exists is not None:
            result['NonExists'] = self.non_exists

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['URLUploadInfoList'] = []
        if self.urlupload_info_list is not None:
            for k1 in self.urlupload_info_list:
                result['URLUploadInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NonExists') is not None:
            self.non_exists = m.get('NonExists')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.urlupload_info_list = []
        if m.get('URLUploadInfoList') is not None:
            for k1 in m.get('URLUploadInfoList'):
                temp_model = main_models.GetURLUploadInfosResponseBodyURLUploadInfoList()
                self.urlupload_info_list.append(temp_model.from_map(k1))

        return self

class GetURLUploadInfosResponseBodyURLUploadInfoList(DaraModel):
    def __init__(
        self,
        complete_time: str = None,
        creation_time: str = None,
        error_code: str = None,
        error_message: str = None,
        file_size: str = None,
        job_id: str = None,
        media_id: str = None,
        registered_media_id: str = None,
        status: str = None,
        upload_url: str = None,
        user_data: str = None,
    ):
        # The time when the upload job was complete. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.complete_time = complete_time
        # The time when the upload job was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The size of the uploaded media file. Unit: byte.
        self.file_size = file_size
        # The ID of the upload job.
        self.job_id = job_id
        # The ID of the uploaded media file.
        self.media_id = media_id
        self.registered_media_id = registered_media_id
        # The status of the URL-based upload job. For more information about the valid values and value description of the parameter, see the "Status: the status of a video" section of the [Basic structures](https://help.aliyun.com/document_detail/52839.html) topic.
        self.status = status
        # The upload URL of the source file.
        # 
        # > A maximum of 100 URLs can be returned.
        self.upload_url = upload_url
        # The custom configurations. The value is a JSON string. For more information, see the "UserData: specifies the custom configurations for media upload" section of the [Request parameters](https://help.aliyun.com/document_detail/86952.html) topic.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.registered_media_id is not None:
            result['RegisteredMediaId'] = self.registered_media_id

        if self.status is not None:
            result['Status'] = self.status

        if self.upload_url is not None:
            result['UploadURL'] = self.upload_url

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('RegisteredMediaId') is not None:
            self.registered_media_id = m.get('RegisteredMediaId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UploadURL') is not None:
            self.upload_url = m.get('UploadURL')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

