# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class ListReportResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.ListReportResponseBodyDataList] = None,
        has_more: bool = None,
        next_cursor: int = None,
        request_id: str = None,
        size: int = None,
    ):
        self.data_list = data_list
        self.has_more = has_more
        self.next_cursor = next_cursor
        # requestId
        self.request_id = request_id
        self.size = size

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['dataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['dataList'].append(k1.to_map() if k1 else None)

        if self.has_more is not None:
            result['hasMore'] = self.has_more

        if self.next_cursor is not None:
            result['nextCursor'] = self.next_cursor

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('dataList') is not None:
            for k1 in m.get('dataList'):
                temp_model = main_models.ListReportResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        if m.get('nextCursor') is not None:
            self.next_cursor = m.get('nextCursor')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

class ListReportResponseBodyDataList(DaraModel):
    def __init__(
        self,
        contents: List[main_models.ListReportResponseBodyDataListContents] = None,
        create_time: int = None,
        creator_id: str = None,
        creator_name: str = None,
        dept_name: str = None,
        images: List[str] = None,
        latitude: str = None,
        longitude: str = None,
        modified_time: int = None,
        remark: str = None,
        report_id: str = None,
        template_name: str = None,
    ):
        self.contents = contents
        self.create_time = create_time
        self.creator_id = creator_id
        self.creator_name = creator_name
        self.dept_name = dept_name
        self.images = images
        self.latitude = latitude
        self.longitude = longitude
        self.modified_time = modified_time
        self.remark = remark
        self.report_id = report_id
        self.template_name = template_name

    def validate(self):
        if self.contents:
            for v1 in self.contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Contents'] = []
        if self.contents is not None:
            for k1 in self.contents:
                result['Contents'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.dept_name is not None:
            result['DeptName'] = self.dept_name

        if self.images is not None:
            result['Images'] = self.images

        if self.latitude is not None:
            result['Latitude'] = self.latitude

        if self.longitude is not None:
            result['Longitude'] = self.longitude

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contents = []
        if m.get('Contents') is not None:
            for k1 in m.get('Contents'):
                temp_model = main_models.ListReportResponseBodyDataListContents()
                self.contents.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('DeptName') is not None:
            self.dept_name = m.get('DeptName')

        if m.get('Images') is not None:
            self.images = m.get('Images')

        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')

        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class ListReportResponseBodyDataListContents(DaraModel):
    def __init__(
        self,
        key: str = None,
        sort: str = None,
        type: str = None,
        value: str = None,
    ):
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
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

