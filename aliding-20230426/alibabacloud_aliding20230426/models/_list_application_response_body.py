# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class ListApplicationResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListApplicationResponseBodyData] = None,
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
                temp_model = main_models.ListApplicationResponseBodyData()
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

class ListApplicationResponseBodyData(DaraModel):
    def __init__(
        self,
        app_config: str = None,
        app_type: str = None,
        application_status: str = None,
        corp_id: str = None,
        creator_user_id: str = None,
        description: str = None,
        icon: str = None,
        inexistence: str = None,
        name: str = None,
        sub_corp_id: str = None,
    ):
        self.app_config = app_config
        self.app_type = app_type
        self.application_status = application_status
        self.corp_id = corp_id
        self.creator_user_id = creator_user_id
        self.description = description
        self.icon = icon
        self.inexistence = inexistence
        self.name = name
        self.sub_corp_id = sub_corp_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_config is not None:
            result['AppConfig'] = self.app_config

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.application_status is not None:
            result['ApplicationStatus'] = self.application_status

        if self.corp_id is not None:
            result['CorpId'] = self.corp_id

        if self.creator_user_id is not None:
            result['CreatorUserId'] = self.creator_user_id

        if self.description is not None:
            result['Description'] = self.description

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.inexistence is not None:
            result['Inexistence'] = self.inexistence

        if self.name is not None:
            result['Name'] = self.name

        if self.sub_corp_id is not None:
            result['SubCorpId'] = self.sub_corp_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppConfig') is not None:
            self.app_config = m.get('AppConfig')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('ApplicationStatus') is not None:
            self.application_status = m.get('ApplicationStatus')

        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')

        if m.get('CreatorUserId') is not None:
            self.creator_user_id = m.get('CreatorUserId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Inexistence') is not None:
            self.inexistence = m.get('Inexistence')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SubCorpId') is not None:
            self.sub_corp_id = m.get('SubCorpId')

        return self

