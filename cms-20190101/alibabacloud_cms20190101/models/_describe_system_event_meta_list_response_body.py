# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeSystemEventMetaListResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeSystemEventMetaListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The queried meta information.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeSystemEventMetaListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSystemEventMetaListResponseBodyData(DaraModel):
    def __init__(
        self,
        resource: List[main_models.DescribeSystemEventMetaListResponseBodyDataResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for v1 in self.resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Resource'] = []
        if self.resource is not None:
            for k1 in self.resource:
                result['Resource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k1 in m.get('Resource'):
                temp_model = main_models.DescribeSystemEventMetaListResponseBodyDataResource()
                self.resource.append(temp_model.from_map(k1))

        return self

class DescribeSystemEventMetaListResponseBodyDataResource(DaraModel):
    def __init__(
        self,
        event_type: str = None,
        level: str = None,
        name: str = None,
        name_desc: str = None,
        name_desc_en: str = None,
        product: str = None,
        status: str = None,
        status_desc: str = None,
    ):
        # The type of the system event. Valid values:
        # 
        # *   StatusNotification: fault notifications
        # *   Exception: exceptions
        # *   Maintenance: O\\&M
        self.event_type = event_type
        # The alert level. Valid values:
        # 
        # *   CRITICAL
        # *   WARN
        # *   INFO
        self.level = level
        # The name of the system event.
        self.name = name
        # The description of the event name.
        self.name_desc = name_desc
        self.name_desc_en = name_desc_en
        # The abbreviation of the service name.
        self.product = product
        # The status of the system event.
        self.status = status
        # The description of the event status.
        self.status_desc = status_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.level is not None:
            result['Level'] = self.level

        if self.name is not None:
            result['Name'] = self.name

        if self.name_desc is not None:
            result['NameDesc'] = self.name_desc

        if self.name_desc_en is not None:
            result['NameDesc.En'] = self.name_desc_en

        if self.product is not None:
            result['Product'] = self.product

        if self.status is not None:
            result['Status'] = self.status

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NameDesc') is not None:
            self.name_desc = m.get('NameDesc')

        if m.get('NameDesc.En') is not None:
            self.name_desc_en = m.get('NameDesc.En')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        return self

