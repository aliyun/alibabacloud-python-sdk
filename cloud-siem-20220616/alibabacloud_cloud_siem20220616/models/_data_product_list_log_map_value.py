# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DataProductListLogMapValue(DaraModel):
    def __init__(
        self,
        log_code: str = None,
        log_name: str = None,
        log_name_en: str = None,
        log_name_key: str = None,
        status: bool = None,
        can_operate_or_not: bool = None,
        topic: str = None,
        extra_parameters: List[main_models.DataProductListLogMapValueExtraParameters] = None,
    ):
        # The log code.
        self.log_code = log_code
        # **[Deprecated]** This parameter is deprecated and can be ignored.
        self.log_name = log_name
        # **[Deprecated]** This parameter is deprecated and can be ignored.
        self.log_name_en = log_name_en
        # The language code of the log, which is used to display multilingual names.
        self.log_name_key = log_name_key
        # The log delivery status. Valid values:
        # - true: Delivery is in progress.  
        # - false: Delivery is disabled.
        self.status = status
        # Specifies whether the log delivery switch can be operated. Only the delegated administrator of Threat Analysis can operate the log delivery switch. Valid values:
        # - true: The switch can be operated.  
        # - false: The switch cannot be operated.
        self.can_operate_or_not = can_operate_or_not
        # The topic of the log in the Logstore. It is an index field of the Logstore and can be used to distinguish different logs.
        self.topic = topic
        # The extended parameters.
        self.extra_parameters = extra_parameters

    def validate(self):
        if self.extra_parameters:
            for v1 in self.extra_parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_code is not None:
            result['LogCode'] = self.log_code

        if self.log_name is not None:
            result['LogName'] = self.log_name

        if self.log_name_en is not None:
            result['LogNameEn'] = self.log_name_en

        if self.log_name_key is not None:
            result['LogNameKey'] = self.log_name_key

        if self.status is not None:
            result['Status'] = self.status

        if self.can_operate_or_not is not None:
            result['CanOperateOrNot'] = self.can_operate_or_not

        if self.topic is not None:
            result['Topic'] = self.topic

        result['ExtraParameters'] = []
        if self.extra_parameters is not None:
            for k1 in self.extra_parameters:
                result['ExtraParameters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')

        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')

        if m.get('LogNameEn') is not None:
            self.log_name_en = m.get('LogNameEn')

        if m.get('LogNameKey') is not None:
            self.log_name_key = m.get('LogNameKey')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('CanOperateOrNot') is not None:
            self.can_operate_or_not = m.get('CanOperateOrNot')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        self.extra_parameters = []
        if m.get('ExtraParameters') is not None:
            for k1 in m.get('ExtraParameters'):
                temp_model = main_models.DataProductListLogMapValueExtraParameters()
                self.extra_parameters.append(temp_model.from_map(k1))

        return self



class DataProductListLogMapValueExtraParameters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The identifier of the extended parameter.
        self.key = key
        # The value of the extended parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

