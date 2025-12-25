# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetUserUploadFileJobResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        upload_file_job_detail: main_models.GetUserUploadFileJobResponseBodyUploadFileJobDetail = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The details of the file upload task.
        self.upload_file_job_detail = upload_file_job_detail

    def validate(self):
        if self.upload_file_job_detail:
            self.upload_file_job_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.upload_file_job_detail is not None:
            result['UploadFileJobDetail'] = self.upload_file_job_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('UploadFileJobDetail') is not None:
            temp_model = main_models.GetUserUploadFileJobResponseBodyUploadFileJobDetail()
            self.upload_file_job_detail = temp_model.from_map(m.get('UploadFileJobDetail'))

        return self

class GetUserUploadFileJobResponseBodyUploadFileJobDetail(DaraModel):
    def __init__(
        self,
        attachment_key: str = None,
        file_name: str = None,
        file_size: int = None,
        file_source: str = None,
        job_key: str = None,
        job_status: str = None,
        job_status_desc: str = None,
        upload_ossparam: main_models.GetUserUploadFileJobResponseBodyUploadFileJobDetailUploadOSSParam = None,
        upload_type: str = None,
        upload_url: str = None,
        uploaded_size: int = None,
    ):
        # The key of the file that is returned after the file is uploaded. You can use this key when you upload the file as an attachment in a ticket.
        self.attachment_key = attachment_key
        # The name of the file.
        self.file_name = file_name
        # The size of the file. Unit: byte.
        self.file_size = file_size
        # The purpose of the uploaded file. Valid values:
        # 
        # *   **datacorrect**: The file is uploaded to change data.
        # *   **order_info_attachment**: The file is uploaded as an attachment in a ticket.
        # *   **big-file**: The file is uploaded to import multiple data records at a time.
        # *   **sqlreview**: The file is uploaded for SQL review.
        self.file_source = file_source
        # The key of the file upload task.
        self.job_key = job_key
        # The status of the file upload task. Valid values:
        # 
        # *   **INIT**: The file upload task was initialized.
        # *   **PENDING**: The file upload task waited to be run.
        # *   **BE_SCHEDULED**: The file upload task waited to be scheduled.
        # *   **FAIL**: The file upload task failed.
        # *   **SUCCESS**: The file upload task was successful.
        # *   **RUNNING**: The file upload task was being run.
        self.job_status = job_status
        # The information about the status of the file upload task.
        self.job_status_desc = job_status_desc
        # The information about the Object Storage Service (OSS) bucket from which the file is uploaded.
        # 
        # > This parameter is returned if the value of **UploadType** is **OSS**.
        self.upload_ossparam = upload_ossparam
        # The method used to upload the file. Valid values:
        # 
        # *   **URL**
        # *   **OSS**
        self.upload_type = upload_type
        # The URL of the file.
        # 
        # > This parameter is returned if the value of **UploadType** is **URL**.
        self.upload_url = upload_url
        # The size of the uploaded file. Unit: byte.
        self.uploaded_size = uploaded_size

    def validate(self):
        if self.upload_ossparam:
            self.upload_ossparam.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachment_key is not None:
            result['AttachmentKey'] = self.attachment_key

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.file_source is not None:
            result['FileSource'] = self.file_source

        if self.job_key is not None:
            result['JobKey'] = self.job_key

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.job_status_desc is not None:
            result['JobStatusDesc'] = self.job_status_desc

        if self.upload_ossparam is not None:
            result['UploadOSSParam'] = self.upload_ossparam.to_map()

        if self.upload_type is not None:
            result['UploadType'] = self.upload_type

        if self.upload_url is not None:
            result['UploadURL'] = self.upload_url

        if self.uploaded_size is not None:
            result['UploadedSize'] = self.uploaded_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKey') is not None:
            self.attachment_key = m.get('AttachmentKey')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('FileSource') is not None:
            self.file_source = m.get('FileSource')

        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('JobStatusDesc') is not None:
            self.job_status_desc = m.get('JobStatusDesc')

        if m.get('UploadOSSParam') is not None:
            temp_model = main_models.GetUserUploadFileJobResponseBodyUploadFileJobDetailUploadOSSParam()
            self.upload_ossparam = temp_model.from_map(m.get('UploadOSSParam'))

        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')

        if m.get('UploadURL') is not None:
            self.upload_url = m.get('UploadURL')

        if m.get('UploadedSize') is not None:
            self.uploaded_size = m.get('UploadedSize')

        return self

class GetUserUploadFileJobResponseBodyUploadFileJobDetailUploadOSSParam(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        endpoint: str = None,
        object_name: str = None,
    ):
        # The name of the OSS bucket.
        self.bucket_name = bucket_name
        # The endpoint of the OSS bucket.
        self.endpoint = endpoint
        # The name of the OSS object.
        self.object_name = object_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        return self

