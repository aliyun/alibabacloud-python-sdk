# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeEventTypesResponseBody(DaraModel):
    def __init__(
        self,
        event_type_list: List[main_models.DescribeEventTypesResponseBodyEventTypeList] = None,
        request_id: str = None,
    ):
        # An array that consists of the types of anomalous events.
        # 
        # > If you leave the ParentTypeId parameter empty, anomalous event types are returned. If you set the ParentTypeId parameter, anomalous event subtypes under the specified anomalous event type are returned.
        self.event_type_list = event_type_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.event_type_list:
            for v1 in self.event_type_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventTypeList'] = []
        if self.event_type_list is not None:
            for k1 in self.event_type_list:
                result['EventTypeList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_type_list = []
        if m.get('EventTypeList') is not None:
            for k1 in m.get('EventTypeList'):
                temp_model = main_models.DescribeEventTypesResponseBodyEventTypeList()
                self.event_type_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEventTypesResponseBodyEventTypeList(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        id: int = None,
        name: str = None,
        sub_type_list: List[main_models.DescribeEventTypesResponseBodyEventTypeListSubTypeList] = None,
    ):
        # The code of the anomalous event type.
        self.code = code
        # The description of the anomalous event type.
        self.description = description
        # The ID of the anomalous event type.
        self.id = id
        # The name of the anomalous event type.
        self.name = name
        # An array that consists of anomalous event subtypes.
        self.sub_type_list = sub_type_list

    def validate(self):
        if self.sub_type_list:
            for v1 in self.sub_type_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        result['SubTypeList'] = []
        if self.sub_type_list is not None:
            for k1 in self.sub_type_list:
                result['SubTypeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.sub_type_list = []
        if m.get('SubTypeList') is not None:
            for k1 in m.get('SubTypeList'):
                temp_model = main_models.DescribeEventTypesResponseBodyEventTypeListSubTypeList()
                self.sub_type_list.append(temp_model.from_map(k1))

        return self

class DescribeEventTypesResponseBodyEventTypeListSubTypeList(DaraModel):
    def __init__(
        self,
        adapted_product: str = None,
        code: str = None,
        config_code: str = None,
        config_content_type: int = None,
        config_description: str = None,
        config_value: str = None,
        description: str = None,
        event_hit_count: int = None,
        id: int = None,
        name: str = None,
        status: int = None,
    ):
        # The service to which the anomalous event detection rule applies. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.adapted_product = adapted_product
        # The code of the anomalous event subtype.
        self.code = code
        # The code of the configuration.
        self.config_code = config_code
        # The content format of anomalous event detection rule. Valid values:
        # 
        # *   **0**: numeric values such as thresholds
        # *   **1**: text such as IP addresses
        self.config_content_type = config_content_type
        # The description of the configuration.
        self.config_description = config_description
        # The value of the configuration.
        self.config_value = config_value
        # The description of the anomalous event subtype.
        self.description = description
        # The number of times that the anomalous event hits the anomalous event detection rule.
        self.event_hit_count = event_hit_count
        # The ID of the anomalous event subtype.
        self.id = id
        # The name of the anomalous event subtype.
        self.name = name
        # Indicates whether detection is enabled for the anomalous event subtype. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adapted_product is not None:
            result['AdaptedProduct'] = self.adapted_product

        if self.code is not None:
            result['Code'] = self.code

        if self.config_code is not None:
            result['ConfigCode'] = self.config_code

        if self.config_content_type is not None:
            result['ConfigContentType'] = self.config_content_type

        if self.config_description is not None:
            result['ConfigDescription'] = self.config_description

        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        if self.description is not None:
            result['Description'] = self.description

        if self.event_hit_count is not None:
            result['EventHitCount'] = self.event_hit_count

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptedProduct') is not None:
            self.adapted_product = m.get('AdaptedProduct')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ConfigCode') is not None:
            self.config_code = m.get('ConfigCode')

        if m.get('ConfigContentType') is not None:
            self.config_content_type = m.get('ConfigContentType')

        if m.get('ConfigDescription') is not None:
            self.config_description = m.get('ConfigDescription')

        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EventHitCount') is not None:
            self.event_hit_count = m.get('EventHitCount')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

