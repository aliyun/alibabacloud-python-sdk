# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class ListCustomAudienceResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[main_models.ListCustomAudienceResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.total = total

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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListCustomAudienceResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListCustomAudienceResponseBodyData(DaraModel):
    def __init__(
        self,
        ad_account_id: str = None,
        create_time: int = None,
        custom_audience_id: str = None,
        custom_audience_name: str = None,
        description: str = None,
        page_id: str = None,
        status: str = None,
        token_total: int = None,
        token_type: str = None,
        update_time: int = None,
        upload_type: str = None,
    ):
        self.ad_account_id = ad_account_id
        self.create_time = create_time
        self.custom_audience_id = custom_audience_id
        self.custom_audience_name = custom_audience_name
        self.description = description
        self.page_id = page_id
        self.status = status
        self.token_total = token_total
        self.token_type = token_type
        self.update_time = update_time
        self.upload_type = upload_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_account_id is not None:
            result['AdAccountId'] = self.ad_account_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.custom_audience_id is not None:
            result['CustomAudienceId'] = self.custom_audience_id

        if self.custom_audience_name is not None:
            result['CustomAudienceName'] = self.custom_audience_name

        if self.description is not None:
            result['Description'] = self.description

        if self.page_id is not None:
            result['PageId'] = self.page_id

        if self.status is not None:
            result['Status'] = self.status

        if self.token_total is not None:
            result['TokenTotal'] = self.token_total

        if self.token_type is not None:
            result['TokenType'] = self.token_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.upload_type is not None:
            result['UploadType'] = self.upload_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdAccountId') is not None:
            self.ad_account_id = m.get('AdAccountId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CustomAudienceId') is not None:
            self.custom_audience_id = m.get('CustomAudienceId')

        if m.get('CustomAudienceName') is not None:
            self.custom_audience_name = m.get('CustomAudienceName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PageId') is not None:
            self.page_id = m.get('PageId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TokenTotal') is not None:
            self.token_total = m.get('TokenTotal')

        if m.get('TokenType') is not None:
            self.token_type = m.get('TokenType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')

        return self

