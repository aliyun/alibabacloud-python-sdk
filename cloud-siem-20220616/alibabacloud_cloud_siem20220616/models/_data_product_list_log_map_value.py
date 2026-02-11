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
        # The code of the log.
        self.log_code = log_code
        # This parameter is deprecated.
        self.log_name = log_name
        # This parameter is deprecated.
        self.log_name_en = log_name_en
        # The language code of the log that is used to indicate the language in which the log is displayed.
        self.log_name_key = log_name_key
        # The status of the log delivery. Valid values:
        # 
        # *   true: The logs are being delivered.
        # *   false: The log delivery feature is disabled.
        self.status = status
        # Indicates whether the log delivery feature can be enabled or disabled. The feature can be enabled or disabled only by the administrator of the threat analysis feature. Valid values:
        # 
        # *   true
        # *   false
        self.can_operate_or_not = can_operate_or_not
        # The topic of the log in the Logstore. The value is an index field in the Logstore that can be used to distinguish different logs.
        self.topic = topic
        # The extended parameter.
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
        # The ID of the extended parameter.
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

