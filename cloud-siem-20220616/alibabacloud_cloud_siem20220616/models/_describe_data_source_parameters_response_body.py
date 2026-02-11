# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeDataSourceParametersResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeDataSourceParametersResponseBodyData] = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeDataSourceParametersResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDataSourceParametersResponseBodyData(DaraModel):
    def __init__(
        self,
        can_editted: int = None,
        cloud_code: str = None,
        data_source_type: str = None,
        default_value: str = None,
        disabled: bool = None,
        format_check: str = None,
        hit: str = None,
        para_code: str = None,
        para_level: int = None,
        para_name: str = None,
        para_type: str = None,
        param_value: List[main_models.DescribeDataSourceParametersResponseBodyDataParamValue] = None,
        required: int = None,
        title: str = None,
    ):
        # Indicates whether the edit operation is supported. Valid values:
        # 
        # *   **0**
        # *   **1**
        self.can_editted = can_editted
        # The code of the cloud service provider. Valid values:
        # 
        # *   **qcloud**: Tencent Cloud
        # *   **aliyun**: Alibaba Cloud
        # *   **hcloud**: Huawei Cloud
        self.cloud_code = cloud_code
        # The type of the data source. Valid values:
        # 
        # *   **obs**: Huawei Cloud Object Storage Service (OBS)
        # *   **wafApi**: download API of Tencent Cloud Web Application Firewall (WAF)
        # *   **ckafka**: Tencent Cloud TDMQ for CKafka
        self.data_source_type = data_source_type
        # The default value of the parameter.
        self.default_value = default_value
        # Indicates whether the modification operation is forbidden. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.disabled = disabled
        # The method that is used to check the parameter format.
        self.format_check = format_check
        # The additional information.
        self.hit = hit
        # The code of the parameter.
        self.para_code = para_code
        # The parameter level. Valid values:
        # 
        # *   **1**: the parameters of the data source
        # *   **2**: the parameters of the log
        self.para_level = para_level
        # The name of the parameter.
        self.para_name = para_name
        # The data type of the parameter.
        self.para_type = para_type
        # The value of the parameter.
        self.param_value = param_value
        # Indicates whether the parameter is required. Valid values:
        # 
        # *   **1**: required
        # *   **0**: optional
        self.required = required
        # The note for the parameter value.
        self.title = title

    def validate(self):
        if self.param_value:
            for v1 in self.param_value:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_editted is not None:
            result['CanEditted'] = self.can_editted

        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.format_check is not None:
            result['FormatCheck'] = self.format_check

        if self.hit is not None:
            result['Hit'] = self.hit

        if self.para_code is not None:
            result['ParaCode'] = self.para_code

        if self.para_level is not None:
            result['ParaLevel'] = self.para_level

        if self.para_name is not None:
            result['ParaName'] = self.para_name

        if self.para_type is not None:
            result['ParaType'] = self.para_type

        result['ParamValue'] = []
        if self.param_value is not None:
            for k1 in self.param_value:
                result['ParamValue'].append(k1.to_map() if k1 else None)

        if self.required is not None:
            result['Required'] = self.required

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanEditted') is not None:
            self.can_editted = m.get('CanEditted')

        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('FormatCheck') is not None:
            self.format_check = m.get('FormatCheck')

        if m.get('Hit') is not None:
            self.hit = m.get('Hit')

        if m.get('ParaCode') is not None:
            self.para_code = m.get('ParaCode')

        if m.get('ParaLevel') is not None:
            self.para_level = m.get('ParaLevel')

        if m.get('ParaName') is not None:
            self.para_name = m.get('ParaName')

        if m.get('ParaType') is not None:
            self.para_type = m.get('ParaType')

        self.param_value = []
        if m.get('ParamValue') is not None:
            for k1 in m.get('ParamValue'):
                temp_model = main_models.DescribeDataSourceParametersResponseBodyDataParamValue()
                self.param_value.append(temp_model.from_map(k1))

        if m.get('Required') is not None:
            self.required = m.get('Required')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class DescribeDataSourceParametersResponseBodyDataParamValue(DaraModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        # The display value.
        self.label = label
        # The actual value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

