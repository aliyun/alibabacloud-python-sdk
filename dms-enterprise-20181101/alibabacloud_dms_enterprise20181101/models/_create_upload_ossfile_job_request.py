# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class CreateUploadOSSFileJobRequest(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_source: str = None,
        tid: int = None,
        upload_target: main_models.CreateUploadOSSFileJobRequestUploadTarget = None,
    ):
        # The name of the file.
        # 
        # > The file name must end with .txt or .sql. For example, the file name can be text.txt.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The purpose of the file upload task. Valid values:
        # 
        # *   **datacorrect**: The file is uploaded to change data.
        # *   **order_info_attachment**: The file is uploaded as an attachment in a ticket.
        # *   **big-file**: The file is uploaded to import multiple data records at a time.
        # *   **sqlreview**: The file is uploaded for SQL review.
        # 
        # This parameter is required.
        self.file_source = file_source
        # The ID of the tenant.
        # 
        # > To view the ID of the tenant, move the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console. For more information, see the "View information about the current tenant" section of the [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html) topic.
        self.tid = tid
        # The information about the OSS file to be uploaded.
        # 
        # This parameter is required.
        self.upload_target = upload_target

    def validate(self):
        if self.upload_target:
            self.upload_target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_source is not None:
            result['FileSource'] = self.file_source

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.upload_target is not None:
            result['UploadTarget'] = self.upload_target.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSource') is not None:
            self.file_source = m.get('FileSource')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('UploadTarget') is not None:
            temp_model = main_models.CreateUploadOSSFileJobRequestUploadTarget()
            self.upload_target = temp_model.from_map(m.get('UploadTarget'))

        return self

class CreateUploadOSSFileJobRequestUploadTarget(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        endpoint: str = None,
        object_name: str = None,
    ):
        # The name of the OSS bucket.
        # 
        # This parameter is required.
        self.bucket_name = bucket_name
        # The endpoint of the OSS bucket.
        # 
        # This parameter is required.
        self.endpoint = endpoint
        # The name of the OSS object.
        # 
        # This parameter is required.
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

