# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryFaceRecordRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        face_group_code: str = None,
        face_id: str = None,
        max_results: int = None,
        merchant_user_id: str = None,
        next_token: str = None,
        page_size: int = None,
        registration_type: str = None,
    ):
        # Current Page.
        # 
        # This parameter is required.
        self.current_page = current_page
        # Face Group Code.
        # 
        # This parameter is required.
        self.face_group_code = face_group_code
        # Face ID.
        self.face_id = face_id
        # Number of rows per page for paginated queries.
        self.max_results = max_results
        # Merchant User ID.
        self.merchant_user_id = merchant_user_id
        # Used to request the next page of search results.
        self.next_token = next_token
        # Number of items per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Registration Type.
        self.registration_type = registration_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.face_group_code is not None:
            result['FaceGroupCode'] = self.face_group_code

        if self.face_id is not None:
            result['FaceId'] = self.face_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.registration_type is not None:
            result['RegistrationType'] = self.registration_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FaceGroupCode') is not None:
            self.face_group_code = m.get('FaceGroupCode')

        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegistrationType') is not None:
            self.registration_type = m.get('RegistrationType')

        return self

