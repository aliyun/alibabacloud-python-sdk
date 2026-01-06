# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetNotifyMeResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetNotifyMeResponseBodyData] = None,
        page_number: int = None,
        request_id: str = None,
        total_count: int = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.data = data
        self.page_number = page_number
        self.request_id = request_id
        self.total_count = total_count
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

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
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetNotifyMeResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetNotifyMeResponseBodyData(DaraModel):
    def __init__(
        self,
        activity_id: str = None,
        app_type: str = None,
        corp_id: str = None,
        create_time_gmt: str = None,
        creator_user_id: str = None,
        form_instance_id: str = None,
        inst_status: str = None,
        mobile_url: str = None,
        modified_time_gmt: str = None,
    ):
        self.activity_id = activity_id
        self.app_type = app_type
        self.corp_id = corp_id
        self.create_time_gmt = create_time_gmt
        self.creator_user_id = creator_user_id
        self.form_instance_id = form_instance_id
        self.inst_status = inst_status
        self.mobile_url = mobile_url
        self.modified_time_gmt = modified_time_gmt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.corp_id is not None:
            result['CorpId'] = self.corp_id

        if self.create_time_gmt is not None:
            result['CreateTimeGMT'] = self.create_time_gmt

        if self.creator_user_id is not None:
            result['CreatorUserId'] = self.creator_user_id

        if self.form_instance_id is not None:
            result['FormInstanceId'] = self.form_instance_id

        if self.inst_status is not None:
            result['InstStatus'] = self.inst_status

        if self.mobile_url is not None:
            result['MobileUrl'] = self.mobile_url

        if self.modified_time_gmt is not None:
            result['ModifiedTimeGMT'] = self.modified_time_gmt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')

        if m.get('CreateTimeGMT') is not None:
            self.create_time_gmt = m.get('CreateTimeGMT')

        if m.get('CreatorUserId') is not None:
            self.creator_user_id = m.get('CreatorUserId')

        if m.get('FormInstanceId') is not None:
            self.form_instance_id = m.get('FormInstanceId')

        if m.get('InstStatus') is not None:
            self.inst_status = m.get('InstStatus')

        if m.get('MobileUrl') is not None:
            self.mobile_url = m.get('MobileUrl')

        if m.get('ModifiedTimeGMT') is not None:
            self.modified_time_gmt = m.get('ModifiedTimeGMT')

        return self

