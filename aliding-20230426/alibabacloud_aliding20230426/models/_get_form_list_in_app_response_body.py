# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetFormListInAppResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[main_models.GetFormListInAppResponseBodyData] = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.current_page = current_page
        self.data = data
        self.request_id = request_id
        self.success = success
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
        if self.current_page is not None:
            result['currentPage'] = self.current_page

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetFormListInAppResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetFormListInAppResponseBodyData(DaraModel):
    def __init__(
        self,
        creator: str = None,
        form_type: str = None,
        form_uuid: str = None,
        gmt_create: str = None,
        title: main_models.GetFormListInAppResponseBodyDataTitle = None,
    ):
        self.creator = creator
        self.form_type = form_type
        self.form_uuid = form_uuid
        self.gmt_create = gmt_create
        self.title = title

    def validate(self):
        if self.title:
            self.title.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator

        if self.form_type is not None:
            result['FormType'] = self.form_type

        if self.form_uuid is not None:
            result['FormUuid'] = self.form_uuid

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.title is not None:
            result['Title'] = self.title.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('FormType') is not None:
            self.form_type = m.get('FormType')

        if m.get('FormUuid') is not None:
            self.form_uuid = m.get('FormUuid')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Title') is not None:
            temp_model = main_models.GetFormListInAppResponseBodyDataTitle()
            self.title = temp_model.from_map(m.get('Title'))

        return self

class GetFormListInAppResponseBodyDataTitle(DaraModel):
    def __init__(
        self,
        en_us: str = None,
        zh_cn: str = None,
    ):
        self.en_us = en_us
        self.zh_cn = zh_cn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.en_us is not None:
            result['EnUS'] = self.en_us

        if self.zh_cn is not None:
            result['ZhCN'] = self.zh_cn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnUS') is not None:
            self.en_us = m.get('EnUS')

        if m.get('ZhCN') is not None:
            self.zh_cn = m.get('ZhCN')

        return self

