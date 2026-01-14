# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEventsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        deal_user_id: str = None,
        end_time: str = None,
        id: int = None,
        instance_name: str = None,
        lang: str = None,
        page_size: int = None,
        product_code: str = None,
        start_time: str = None,
        status: str = None,
        sub_type_code: str = None,
        target_product_code: str = None,
        type_code: str = None,
        user_id: int = None,
        user_name: str = None,
        warn_level: int = None,
    ):
        # The page number of the page to return.
        self.current_page = current_page
        # The ID of the account that handles the anomalous event.
        self.deal_user_id = deal_user_id
        # The end of the time range during which the anomalous events are detected. The value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time
        # The unique ID of the anomalous event.
        self.id = id
        # The name of the data asset.
        self.instance_name = instance_name
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Chinese
        # *   **en_us**: English
        self.lang = lang
        # The number of entries to return on each page.
        self.page_size = page_size
        # The name of the service to which the table belongs. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.product_code = product_code
        # The beginning of the time range during which the anomalous events are detected. The value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time
        # The handling status of the anomalous event. Valid values:
        # 
        # *   0: unhandled
        # *   1: confirmed
        # *   2: marked as false positive
        self.status = status
        # The name of the anomalous event subtype.
        # 
        # > You can call the **DescribeEventTypes** operation to query the name of the anomalous event subtype.
        self.sub_type_code = sub_type_code
        # The name of the destination service in an anomalous data flow. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**
        self.target_product_code = target_product_code
        # The name of the anomalous event type. Valid values:
        # 
        # *   01: anomalous permission usage
        # *   02: anomalous data flow
        # *   03: anomalous data operation
        self.type_code = type_code
        # The ID of the account that triggered the anomalous event.
        self.user_id = user_id
        # The username of the RAM user.
        self.user_name = user_name
        # The risk level of the alert that is triggered. Valid values:
        # 
        # *   **1**: low
        # *   **2**: medium
        # *   **3**: high
        self.warn_level = warn_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.deal_user_id is not None:
            result['DealUserId'] = self.deal_user_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_type_code is not None:
            result['SubTypeCode'] = self.sub_type_code

        if self.target_product_code is not None:
            result['TargetProductCode'] = self.target_product_code

        if self.type_code is not None:
            result['TypeCode'] = self.type_code

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.warn_level is not None:
            result['WarnLevel'] = self.warn_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DealUserId') is not None:
            self.deal_user_id = m.get('DealUserId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubTypeCode') is not None:
            self.sub_type_code = m.get('SubTypeCode')

        if m.get('TargetProductCode') is not None:
            self.target_product_code = m.get('TargetProductCode')

        if m.get('TypeCode') is not None:
            self.type_code = m.get('TypeCode')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('WarnLevel') is not None:
            self.warn_level = m.get('WarnLevel')

        return self

