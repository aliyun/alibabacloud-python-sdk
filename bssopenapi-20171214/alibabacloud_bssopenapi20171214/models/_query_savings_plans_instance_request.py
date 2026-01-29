# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QuerySavingsPlansInstanceRequest(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        end_time: str = None,
        instance_id: str = None,
        locale: str = None,
        page_num: int = None,
        page_size: int = None,
        start_time: str = None,
        status: str = None,
        tag: List[main_models.QuerySavingsPlansInstanceRequestTag] = None,
    ):
        self.commodity_code = commodity_code
        # The end of the time range to query. Specify the time in the format of yyyy-MM-dd HH:mm:ss.
        self.end_time = end_time
        # The ID of the savings plan instance.
        self.instance_id = instance_id
        # The language of the return data. Valid values:
        # 
        # *   ZH: Chinese
        # *   EN: English
        self.locale = locale
        # The number of the page to return.
        self.page_num = page_num
        # The number of entries to return on each page.
        self.page_size = page_size
        # The beginning of the time range to query. Specify the time in the format of yyyy-MM-dd HH:mm:ss.
        self.start_time = start_time
        # The status of the Instance. 
        # 
        # *  NORMAL
        # * RELEASE
        self.status = status
        # The tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.locale is not None:
            result['Locale'] = self.locale

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Locale') is not None:
            self.locale = m.get('Locale')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.QuerySavingsPlansInstanceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class QuerySavingsPlansInstanceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag to query.
        self.key = key
        # The value of the tag to query.
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

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

