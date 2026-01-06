# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class QueryReportDetailResponseBody(DaraModel):
    def __init__(
        self,
        content: List[main_models.QueryReportDetailResponseBodyContent] = None,
        create_time: int = None,
        creator_id: str = None,
        creator_name: str = None,
        dept_name: str = None,
        modified_time: int = None,
        remark: str = None,
        report_id: str = None,
        request_id: str = None,
        template_name: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.content = content
        self.create_time = create_time
        self.creator_id = creator_id
        self.creator_name = creator_name
        self.dept_name = dept_name
        self.modified_time = modified_time
        self.remark = remark
        self.report_id = report_id
        self.request_id = request_id
        self.template_name = template_name
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['content'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.creator_id is not None:
            result['creatorId'] = self.creator_id

        if self.creator_name is not None:
            result['creatorName'] = self.creator_name

        if self.dept_name is not None:
            result['deptName'] = self.dept_name

        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time

        if self.remark is not None:
            result['remark'] = self.remark

        if self.report_id is not None:
            result['reportId'] = self.report_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k1 in m.get('content'):
                temp_model = main_models.QueryReportDetailResponseBodyContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')

        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('deptName') is not None:
            self.dept_name = m.get('deptName')

        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class QueryReportDetailResponseBodyContent(DaraModel):
    def __init__(
        self,
        images: List[str] = None,
        key: str = None,
        sort: str = None,
        type: str = None,
        value: str = None,
    ):
        self.images = images
        self.key = key
        self.sort = sort
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.images is not None:
            result['Images'] = self.images

        if self.key is not None:
            result['Key'] = self.key

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Images') is not None:
            self.images = m.get('Images')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

