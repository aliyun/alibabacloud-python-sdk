# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_tag20180828 import models as main_models
from darabonba.model import DaraModel

class ListSupportResourceTypesResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        support_resource_types: List[main_models.ListSupportResourceTypesResponseBodySupportResourceTypes] = None,
    ):
        # Indicates whether the next query is required.
        # 
        # *   If the value of this parameter is empty, all results are returned, and the next query is not required.
        # *   If the value of this parameter is not empty, the next query is required, and the value is the token used to start the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The supported resource types.
        self.support_resource_types = support_resource_types

    def validate(self):
        if self.support_resource_types:
            for v1 in self.support_resource_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SupportResourceTypes'] = []
        if self.support_resource_types is not None:
            for k1 in self.support_resource_types:
                result['SupportResourceTypes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.support_resource_types = []
        if m.get('SupportResourceTypes') is not None:
            for k1 in m.get('SupportResourceTypes'):
                temp_model = main_models.ListSupportResourceTypesResponseBodySupportResourceTypes()
                self.support_resource_types.append(temp_model.from_map(k1))

        return self

class ListSupportResourceTypesResponseBodySupportResourceTypes(DaraModel):
    def __init__(
        self,
        arn_template: str = None,
        product_code: str = None,
        resource_type: str = None,
        support_items: List[main_models.ListSupportResourceTypesResponseBodySupportResourceTypesSupportItems] = None,
    ):
        # The resource ARN template.
        self.arn_template = arn_template
        # The service code.
        self.product_code = product_code
        # The resource type.
        self.resource_type = resource_type
        # The supported tag-related capability items.
        # 
        # >  This parameter is returned only if the `ShowItems` parameter is set to `true`.
        self.support_items = support_items

    def validate(self):
        if self.support_items:
            for v1 in self.support_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn_template is not None:
            result['ArnTemplate'] = self.arn_template

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['SupportItems'] = []
        if self.support_items is not None:
            for k1 in self.support_items:
                result['SupportItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArnTemplate') is not None:
            self.arn_template = m.get('ArnTemplate')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.support_items = []
        if m.get('SupportItems') is not None:
            for k1 in m.get('SupportItems'):
                temp_model = main_models.ListSupportResourceTypesResponseBodySupportResourceTypesSupportItems()
                self.support_items.append(temp_model.from_map(k1))

        return self

class ListSupportResourceTypesResponseBodySupportResourceTypesSupportItems(DaraModel):
    def __init__(
        self,
        support: bool = None,
        support_code: str = None,
        support_details: List[Dict[str, str]] = None,
    ):
        # Indicates whether the tag-related capability item is supported. Valid values:
        # 
        # *   true
        # *   false
        self.support = support
        # The code of the tag-related capability item.
        self.support_code = support_code
        # The details of the support for the tag-related capability item.
        self.support_details = support_details

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.support is not None:
            result['Support'] = self.support

        if self.support_code is not None:
            result['SupportCode'] = self.support_code

        if self.support_details is not None:
            result['SupportDetails'] = self.support_details

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Support') is not None:
            self.support = m.get('Support')

        if m.get('SupportCode') is not None:
            self.support_code = m.get('SupportCode')

        if m.get('SupportDetails') is not None:
            self.support_details = m.get('SupportDetails')

        return self

