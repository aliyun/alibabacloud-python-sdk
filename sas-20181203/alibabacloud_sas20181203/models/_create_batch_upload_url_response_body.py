# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class CreateBatchUploadUrlResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        upload_url_list: List[main_models.CreateBatchUploadUrlResponseBodyUploadUrlList] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array consisting of the parameters that are required to upload a file.
        self.upload_url_list = upload_url_list

    def validate(self):
        if self.upload_url_list:
            for v1 in self.upload_url_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UploadUrlList'] = []
        if self.upload_url_list is not None:
            for k1 in self.upload_url_list:
                result['UploadUrlList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.upload_url_list = []
        if m.get('UploadUrlList') is not None:
            for k1 in m.get('UploadUrlList'):
                temp_model = main_models.CreateBatchUploadUrlResponseBodyUploadUrlList()
                self.upload_url_list.append(temp_model.from_map(k1))

        return self

class CreateBatchUploadUrlResponseBodyUploadUrlList(DaraModel):
    def __init__(
        self,
        context: main_models.CreateBatchUploadUrlResponseBodyUploadUrlListContext = None,
        expire: str = None,
        file_exist: bool = None,
        internal_url: str = None,
        md_5: str = None,
        public_url: str = None,
    ):
        # The signature information.
        self.context = context
        # The timestamp when the values of the parameters expire. Unit: milliseconds.
        self.expire = expire
        # Indicates whether the file exists in the cloud. Valid values:
        # 
        # *   **true**: The file exists in the cloud. You do not need to upload the file.
        # *   **false**: The file does not exist in the cloud. You must upload the file.
        self.file_exist = file_exist
        # The internal endpoint of the URL to which the file is uploaded.
        self.internal_url = internal_url
        # The identifier of the file.
        self.md_5 = md_5
        # The public endpoint of the URL to which the file is uploaded.
        self.public_url = public_url

    def validate(self):
        if self.context:
            self.context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context is not None:
            result['Context'] = self.context.to_map()

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.file_exist is not None:
            result['FileExist'] = self.file_exist

        if self.internal_url is not None:
            result['InternalUrl'] = self.internal_url

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.public_url is not None:
            result['PublicUrl'] = self.public_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            temp_model = main_models.CreateBatchUploadUrlResponseBodyUploadUrlListContext()
            self.context = temp_model.from_map(m.get('Context'))

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('FileExist') is not None:
            self.file_exist = m.get('FileExist')

        if m.get('InternalUrl') is not None:
            self.internal_url = m.get('InternalUrl')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('PublicUrl') is not None:
            self.public_url = m.get('PublicUrl')

        return self

class CreateBatchUploadUrlResponseBodyUploadUrlListContext(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        oss_key: str = None,
        policy: str = None,
        signature: str = None,
    ):
        # The AccessKey ID that is used to access the OSS bucket.
        self.access_id = access_id
        # The key of the file that is used after the file is uploaded to the OSS bucket.
        self.oss_key = oss_key
        # The policy that poses limits on file upload. For example, the policy can limit the size of the file.
        self.policy = policy
        # The signature that is used to upload the file.
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['AccessId'] = self.access_id

        if self.oss_key is not None:
            result['OssKey'] = self.oss_key

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.signature is not None:
            result['Signature'] = self.signature

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')

        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        return self

