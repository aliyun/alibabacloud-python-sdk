# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class QueryNotifyResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.QueryNotifyResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.QueryNotifyResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryNotifyResponseBodyData(DaraModel):
    def __init__(
        self,
        notify_item_list: List[main_models.QueryNotifyResponseBodyDataNotifyItemList] = None,
        page_number: int = None,
        page_size: int = None,
        total_record_count: int = None,
    ):
        # The details of notifications.
        self.notify_item_list = notify_item_list
        # The page number of the page returned.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.notify_item_list:
            for v1 in self.notify_item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NotifyItemList'] = []
        if self.notify_item_list is not None:
            for k1 in self.notify_item_list:
                result['NotifyItemList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.notify_item_list = []
        if m.get('NotifyItemList') is not None:
            for k1 in m.get('NotifyItemList'):
                temp_model = main_models.QueryNotifyResponseBodyDataNotifyItemList()
                self.notify_item_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class QueryNotifyResponseBodyDataNotifyItemList(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        confirm_flag: bool = None,
        confirmor: int = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        id: int = None,
        idempotent_count: str = None,
        idempotent_id: str = None,
        level: str = None,
        notify_element: str = None,
        template_name: str = None,
        type: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # Indicates whether the notification has been confirmed. You can call the [ConfirmNotify](https://help.aliyun.com/document_detail/610444.html) operation to mark the notification as confirmed. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.confirm_flag = confirm_flag
        # The UID of the contact who called the [ConfirmNotify](https://help.aliyun.com/document_detail/610444.html) operation to mark the notification as confirmed. The contact belongs to the current Alibaba Cloud account.
        # 
        # The value **0** indicates that the notification is automatically confirmed by the system.
        self.confirmor = confirmor
        # The time when the notification was created.
        self.gmt_created = gmt_created
        # The time when the notification was modified.
        self.gmt_modified = gmt_modified
        # The ID of the notification.
        self.id = id
        # The number of times that repeatedly sent notifications are blocked.
        self.idempotent_count = idempotent_count
        # This parameter ensures the idempotence of the notification and prevents the notification from being repeatedly sent.
        self.idempotent_id = idempotent_id
        # The level of the notification. Valid values:
        # 
        # *   **help**
        # *   **success**
        # *   **warning**
        # *   **error**
        # *   **loading**
        # *   **notice**
        self.level = level
        # The element in the notification template. This parameter is a JSON string. Fields in the JSON string vary based on the value of the **TemplateName** parameter.
        # 
        # *   If the **TemplateName** parameter is **RenewalRecommend**, the JSON string contains the following fields:
        # 
        #     *   **instanceName**: the ID of the instance that is about to expire
        #     *   **reservedTime**: the remaining validity period of the instance in days
        # 
        # *   If the **TemplateName** parameter is **InstanceCreateFailed**, the JSON string contains the following fields:
        # 
        #     *   **orderId**: the ID of the order to purchase the instance
        #     *   **reason**: the cause of the instance creation failure
        self.notify_element = notify_element
        # The template of the notification. Valid values:
        # 
        # *   **RenewalRecommend**: The template that is used to notify of renewal suggestions.
        # *   **InstanceCreateFailed**: The template that is used to notify that an instance fails to be created and is refunded.
        self.template_name = template_name
        # The type of the notification. Valid values:
        # 
        # *   **Sell**: sales notification
        # *   **Operation**: O\\&M notification
        # *   **Promotion**: promotion notification
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.confirm_flag is not None:
            result['ConfirmFlag'] = self.confirm_flag

        if self.confirmor is not None:
            result['Confirmor'] = self.confirmor

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.idempotent_count is not None:
            result['IdempotentCount'] = self.idempotent_count

        if self.idempotent_id is not None:
            result['IdempotentId'] = self.idempotent_id

        if self.level is not None:
            result['Level'] = self.level

        if self.notify_element is not None:
            result['NotifyElement'] = self.notify_element

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('ConfirmFlag') is not None:
            self.confirm_flag = m.get('ConfirmFlag')

        if m.get('Confirmor') is not None:
            self.confirmor = m.get('Confirmor')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdempotentCount') is not None:
            self.idempotent_count = m.get('IdempotentCount')

        if m.get('IdempotentId') is not None:
            self.idempotent_id = m.get('IdempotentId')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('NotifyElement') is not None:
            self.notify_element = m.get('NotifyElement')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

