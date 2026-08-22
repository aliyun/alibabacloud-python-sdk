# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeAlertTypeResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.DescribeAlertTypeResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The request status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # - true: successful.
        # - false: failed.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeAlertTypeResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeAlertTypeResponseBodyData(DaraModel):
    def __init__(
        self,
        alert_type: str = None,
        alert_type_category: str = None,
        alert_type_category_mds: str = None,
        alert_type_category_order: int = None,
        alert_type_mds: str = None,
        alert_type_name_en: str = None,
        alert_type_name_zh: str = None,
    ):
        # The threat type.
        self.alert_type = alert_type
        # The threat type category identifier.
        self.alert_type_category = alert_type_category
        # The threat type category name in the language of the current request. Empty if no translation is available.
        self.alert_type_category_mds = alert_type_category_mds
        # The display order of the threat type category.
        self.alert_type_category_order = alert_type_category_order
        # The Medusa code of the threat type.
        self.alert_type_mds = alert_type_mds
        # The English name of the threat type. Empty if no translation is available.
        self.alert_type_name_en = alert_type_name_en
        # The Chinese name of the threat type. Empty if no translation is available.
        self.alert_type_name_zh = alert_type_name_zh

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.alert_type_category is not None:
            result['AlertTypeCategory'] = self.alert_type_category

        if self.alert_type_category_mds is not None:
            result['AlertTypeCategoryMds'] = self.alert_type_category_mds

        if self.alert_type_category_order is not None:
            result['AlertTypeCategoryOrder'] = self.alert_type_category_order

        if self.alert_type_mds is not None:
            result['AlertTypeMds'] = self.alert_type_mds

        if self.alert_type_name_en is not None:
            result['AlertTypeNameEn'] = self.alert_type_name_en

        if self.alert_type_name_zh is not None:
            result['AlertTypeNameZh'] = self.alert_type_name_zh

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('AlertTypeCategory') is not None:
            self.alert_type_category = m.get('AlertTypeCategory')

        if m.get('AlertTypeCategoryMds') is not None:
            self.alert_type_category_mds = m.get('AlertTypeCategoryMds')

        if m.get('AlertTypeCategoryOrder') is not None:
            self.alert_type_category_order = m.get('AlertTypeCategoryOrder')

        if m.get('AlertTypeMds') is not None:
            self.alert_type_mds = m.get('AlertTypeMds')

        if m.get('AlertTypeNameEn') is not None:
            self.alert_type_name_en = m.get('AlertTypeNameEn')

        if m.get('AlertTypeNameZh') is not None:
            self.alert_type_name_zh = m.get('AlertTypeNameZh')

        return self

