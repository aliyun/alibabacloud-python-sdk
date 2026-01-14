# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeEventsResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.DescribeEventsResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # An array that consists of the anomalous events.
        self.items = items
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeEventsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeEventsResponseBodyItems(DaraModel):
    def __init__(
        self,
        alert_time: int = None,
        backed: bool = None,
        deal_display_name: str = None,
        deal_login_name: str = None,
        deal_time: int = None,
        deal_user_id: int = None,
        display_name: str = None,
        event_time: int = None,
        id: int = None,
        login_name: str = None,
        product_code: str = None,
        status: int = None,
        status_name: str = None,
        sub_type_code: str = None,
        sub_type_name: str = None,
        target_product_code: str = None,
        type_code: str = None,
        type_name: str = None,
        user_id: int = None,
        warn_level: int = None,
    ):
        # The time when an alert was triggered for the anomalous event. The value is a UNIX timestamp. Unit: milliseconds.
        self.alert_time = alert_time
        # Indicates whether the detection of anomalous events is enhanced. If the detection of anomalous events is enhanced, the detection accuracy and the rate of triggering alerts for anomalous events are improved. Valid values:
        # 
        # *   true: yes
        # *   false: no
        self.backed = backed
        # The display name of the account that is used to handle the anomalous event.
        self.deal_display_name = deal_display_name
        # The username of the account that is used to handle the anomalous event.
        self.deal_login_name = deal_login_name
        # The time when the anomalous event was handled. The value is a UNIX timestamp. Unit: milliseconds.
        self.deal_time = deal_time
        # The ID of the account that is used to handle the anomalous event.
        self.deal_user_id = deal_user_id
        # The display name of the account that triggered the anomalous event.
        self.display_name = display_name
        # The time when the anomalous event occurred. The value is a UNIX timestamp. Unit: milliseconds.
        self.event_time = event_time
        # The ID of the anomalous event.
        self.id = id
        # The username of the account that triggered the anomalous event.
        self.login_name = login_name
        # The name of the service in which the anomalous event was detected.
        self.product_code = product_code
        # The handling status for the anomalous event. Valid values:
        # 
        # *   0: unhandled
        # *   1: confirmed
        # *   2: marked as false positive
        self.status = status
        # The name of the handling status for the anomalous event.
        self.status_name = status_name
        # The code of the anomalous event subtype.
        self.sub_type_code = sub_type_code
        # The name of the anomalous event subtype.
        self.sub_type_name = sub_type_name
        # The name of the destination service in an anomalous data flow.
        self.target_product_code = target_product_code
        # The code of the anomalous event type.
        self.type_code = type_code
        # The name of the anomalous event type.
        self.type_name = type_name
        # The ID of the account that triggered the anomalous event.
        self.user_id = user_id
        # The severity of the anomalous event.
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
        if self.alert_time is not None:
            result['AlertTime'] = self.alert_time

        if self.backed is not None:
            result['Backed'] = self.backed

        if self.deal_display_name is not None:
            result['DealDisplayName'] = self.deal_display_name

        if self.deal_login_name is not None:
            result['DealLoginName'] = self.deal_login_name

        if self.deal_time is not None:
            result['DealTime'] = self.deal_time

        if self.deal_user_id is not None:
            result['DealUserId'] = self.deal_user_id

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.event_time is not None:
            result['EventTime'] = self.event_time

        if self.id is not None:
            result['Id'] = self.id

        if self.login_name is not None:
            result['LoginName'] = self.login_name

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.status is not None:
            result['Status'] = self.status

        if self.status_name is not None:
            result['StatusName'] = self.status_name

        if self.sub_type_code is not None:
            result['SubTypeCode'] = self.sub_type_code

        if self.sub_type_name is not None:
            result['SubTypeName'] = self.sub_type_name

        if self.target_product_code is not None:
            result['TargetProductCode'] = self.target_product_code

        if self.type_code is not None:
            result['TypeCode'] = self.type_code

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.warn_level is not None:
            result['WarnLevel'] = self.warn_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertTime') is not None:
            self.alert_time = m.get('AlertTime')

        if m.get('Backed') is not None:
            self.backed = m.get('Backed')

        if m.get('DealDisplayName') is not None:
            self.deal_display_name = m.get('DealDisplayName')

        if m.get('DealLoginName') is not None:
            self.deal_login_name = m.get('DealLoginName')

        if m.get('DealTime') is not None:
            self.deal_time = m.get('DealTime')

        if m.get('DealUserId') is not None:
            self.deal_user_id = m.get('DealUserId')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')

        if m.get('SubTypeCode') is not None:
            self.sub_type_code = m.get('SubTypeCode')

        if m.get('SubTypeName') is not None:
            self.sub_type_name = m.get('SubTypeName')

        if m.get('TargetProductCode') is not None:
            self.target_product_code = m.get('TargetProductCode')

        if m.get('TypeCode') is not None:
            self.type_code = m.get('TypeCode')

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WarnLevel') is not None:
            self.warn_level = m.get('WarnLevel')

        return self

