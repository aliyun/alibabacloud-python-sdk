# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySavingsPlansDeductLogRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        instance_id: str = None,
        instance_type: str = None,
        locale: str = None,
        page_num: int = None,
        page_size: int = None,
        start_time: str = None,
    ):
        # The end of the time range to query. Specify the time in the format of yyyy-MM-dd HH:mm:ss.
        self.end_time = end_time
        # The ID of the instance.
        self.instance_id = instance_id
        # The type of the instance ID based on which the data is queried. Valid values:
        # 
        # *   spn: queries data based on the ID of the savings plan instance.
        # *   product: queries data based on the ID of the cloud service instance.
        self.instance_type = instance_type
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

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.locale is not None:
            result['Locale'] = self.locale

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Locale') is not None:
            self.locale = m.get('Locale')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

