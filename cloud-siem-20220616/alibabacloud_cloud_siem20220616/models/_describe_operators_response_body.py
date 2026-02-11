# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeOperatorsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.DescribeOperatorsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data returned.
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
                temp_model = main_models.DescribeOperatorsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeOperatorsResponseBodyData(DaraModel):
    def __init__(
        self,
        index: int = None,
        operator: str = None,
        operator_desc_cn: str = None,
        operator_desc_en: str = None,
        operator_name: str = None,
        support_data_type: str = None,
        support_tag: List[str] = None,
    ):
        # The position of the operator in the operator list.
        self.index = index
        # The operator.
        self.operator = operator
        # The description of the operator in Chinese.
        self.operator_desc_cn = operator_desc_cn
        # The description of the operator in English.
        self.operator_desc_en = operator_desc_en
        # The name of the operator.
        self.operator_name = operator_name
        # The data types that are supported by the operator. The data types are separated by commas (,).
        self.support_data_type = support_data_type
        # The scenarios that are supported by the operator. Multiple scenarios are separated by commas (,), such as AGGREGATE scenarios. By default, this parameter is empty.
        self.support_tag = support_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['Index'] = self.index

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.operator_desc_cn is not None:
            result['OperatorDescCn'] = self.operator_desc_cn

        if self.operator_desc_en is not None:
            result['OperatorDescEn'] = self.operator_desc_en

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        if self.support_data_type is not None:
            result['SupportDataType'] = self.support_data_type

        if self.support_tag is not None:
            result['SupportTag'] = self.support_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('OperatorDescCn') is not None:
            self.operator_desc_cn = m.get('OperatorDescCn')

        if m.get('OperatorDescEn') is not None:
            self.operator_desc_en = m.get('OperatorDescEn')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        if m.get('SupportDataType') is not None:
            self.support_data_type = m.get('SupportDataType')

        if m.get('SupportTag') is not None:
            self.support_tag = m.get('SupportTag')

        return self

