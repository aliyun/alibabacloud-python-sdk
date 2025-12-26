# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class QueryFaceRecordResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        items: List[main_models.QueryFaceRecordResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # Return code.
        self.code = code
        # Current query page number.
        self.current_page = current_page
        # List of returned information.
        self.items = items
        # Maximum number of data entries per page.
        self.max_results = max_results
        # Return message.
        self.message = message
        # Token for the next query start.
        self.next_token = next_token
        # Number of items per page.
        self.page_size = page_size
        # ID of the request
        self.request_id = request_id
        # Total number of records.
        self.total_count = total_count
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.QueryFaceRecordResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class QueryFaceRecordResponseBodyItems(DaraModel):
    def __init__(
        self,
        face_id: str = None,
        gmt_create: str = None,
        id: int = None,
        img_oss_url: str = None,
        merchant_user_id: str = None,
        registration_type: str = None,
    ):
        # Face ID.
        self.face_id = face_id
        # Creation time.
        self.gmt_create = gmt_create
        # Primary key ID.
        self.id = id
        # Face image URL.
        self.img_oss_url = img_oss_url
        # Merchant User ID.
        self.merchant_user_id = merchant_user_id
        # Registration type.
        self.registration_type = registration_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.face_id is not None:
            result['FaceId'] = self.face_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.id is not None:
            result['Id'] = self.id

        if self.img_oss_url is not None:
            result['ImgOssUrl'] = self.img_oss_url

        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id

        if self.registration_type is not None:
            result['RegistrationType'] = self.registration_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ImgOssUrl') is not None:
            self.img_oss_url = m.get('ImgOssUrl')

        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')

        if m.get('RegistrationType') is not None:
            self.registration_type = m.get('RegistrationType')

        return self

