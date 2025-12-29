# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class ListFileUploadResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListFileUploadResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListFileUploadResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListFileUploadResponseBodyData(DaraModel):
    def __init__(
        self,
        aliyun_parent_uid: str = None,
        aliyun_uid: str = None,
        download_link: str = None,
        file_category: str = None,
        file_from: str = None,
        file_id: str = None,
        file_name: str = None,
        file_size: int = None,
        file_type: str = None,
        gmt_created: str = None,
        intranet_download_link: str = None,
        region: str = None,
        session_id: str = None,
        upload_location: str = None,
    ):
        self.aliyun_parent_uid = aliyun_parent_uid
        self.aliyun_uid = aliyun_uid
        self.download_link = download_link
        self.file_category = file_category
        self.file_from = file_from
        self.file_id = file_id
        self.file_name = file_name
        self.file_size = file_size
        self.file_type = file_type
        self.gmt_created = gmt_created
        self.intranet_download_link = intranet_download_link
        self.region = region
        self.session_id = session_id
        self.upload_location = upload_location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_parent_uid is not None:
            result['AliyunParentUid'] = self.aliyun_parent_uid

        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

        if self.download_link is not None:
            result['DownloadLink'] = self.download_link

        if self.file_category is not None:
            result['FileCategory'] = self.file_category

        if self.file_from is not None:
            result['FileFrom'] = self.file_from

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.intranet_download_link is not None:
            result['IntranetDownloadLink'] = self.intranet_download_link

        if self.region is not None:
            result['Region'] = self.region

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.upload_location is not None:
            result['UploadLocation'] = self.upload_location

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunParentUid') is not None:
            self.aliyun_parent_uid = m.get('AliyunParentUid')

        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')

        if m.get('FileCategory') is not None:
            self.file_category = m.get('FileCategory')

        if m.get('FileFrom') is not None:
            self.file_from = m.get('FileFrom')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('IntranetDownloadLink') is not None:
            self.intranet_download_link = m.get('IntranetDownloadLink')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('UploadLocation') is not None:
            self.upload_location = m.get('UploadLocation')

        return self

