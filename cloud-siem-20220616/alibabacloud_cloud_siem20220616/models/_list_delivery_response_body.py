# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class ListDeliveryResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListDeliveryResponseBodyData = None,
        request_id: str = None,
    ):
        # The detailed response data.
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
            temp_model = main_models.ListDeliveryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDeliveryResponseBodyData(DaraModel):
    def __init__(
        self,
        dashboard_url: str = None,
        display_switch_or_not: bool = None,
        log_store_name: str = None,
        product_list: List[main_models.ListDeliveryResponseBodyDataProductList] = None,
        project_name: str = None,
        search_url: str = None,
    ):
        # The URL for dashboard display on the log analysis page.
        self.dashboard_url = dashboard_url
        # Specifies whether to display the delivery switch. Default value: true. Valid values:
        # - true: Display the delivery switch.
        # - false: Hide the delivery switch.
        self.display_switch_or_not = display_switch_or_not
        # The name of the Logstore on the user side of Threat Analysis. Format: cloud_siem.
        self.log_store_name = log_store_name
        # The list of products.
        self.product_list = product_list
        # The name of the Log Service project on the user side of Threat Analysis. Format: aliyun-cloudsiem-data-${aliUid}-${region}.
        self.project_name = project_name
        # The URL for query and analysis on the log analysis page.
        self.search_url = search_url

    def validate(self):
        if self.product_list:
            for v1 in self.product_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dashboard_url is not None:
            result['DashboardUrl'] = self.dashboard_url

        if self.display_switch_or_not is not None:
            result['DisplaySwitchOrNot'] = self.display_switch_or_not

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        result['ProductList'] = []
        if self.product_list is not None:
            for k1 in self.product_list:
                result['ProductList'].append(k1.to_map() if k1 else None)

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.search_url is not None:
            result['SearchUrl'] = self.search_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DashboardUrl') is not None:
            self.dashboard_url = m.get('DashboardUrl')

        if m.get('DisplaySwitchOrNot') is not None:
            self.display_switch_or_not = m.get('DisplaySwitchOrNot')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        self.product_list = []
        if m.get('ProductList') is not None:
            for k1 in m.get('ProductList'):
                temp_model = main_models.ListDeliveryResponseBodyDataProductList()
                self.product_list.append(temp_model.from_map(k1))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SearchUrl') is not None:
            self.search_url = m.get('SearchUrl')

        return self

class ListDeliveryResponseBodyDataProductList(DaraModel):
    def __init__(
        self,
        log_list: List[main_models.ListDeliveryResponseBodyDataProductListLogList] = None,
        log_map: Dict[str, List[main_models.DataProductListLogMapValue]] = None,
        product_code: str = None,
        product_name: str = None,
    ):
        # The cloud services that do not have finer categories.
        self.log_list = log_list
        # The list of logs that have categories. For example, Security Center has groups such as host and network. The group information is the key, and the logs included in the group are the value.
        self.log_map = log_map
        # The code of the cloud service. Valid values:
        # - qcloud_waf
        # - qlcoud_cfw
        # - hcloud_waf
        # - hcloud_cfw
        # - ddos
        # - sas
        # - cfw
        # - config
        # - csk
        # - fc
        # - rds
        # - nas
        # - apigateway
        # - cdn
        # - mongodb
        # - eip
        # - slb
        # - vpc
        # - actiontrail
        # - waf
        # - bastionhost
        # - oss
        # - polardb
        self.product_code = product_code
        # **[Deprecated]** This parameter is deprecated and can be ignored.
        self.product_name = product_name

    def validate(self):
        if self.log_list:
            for v1 in self.log_list:
                 if v1:
                    v1.validate()
        if self.log_map:
            for v1 in self.log_map.values():
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LogList'] = []
        if self.log_list is not None:
            for k1 in self.log_list:
                result['LogList'].append(k1.to_map() if k1 else None)

        result['LogMap'] = {}
        if self.log_map is not None:
            for k1, v1 in self.log_map.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['LogMap'][k1] = l1

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_list = []
        if m.get('LogList') is not None:
            for k1 in m.get('LogList'):
                temp_model = main_models.ListDeliveryResponseBodyDataProductListLogList()
                self.log_list.append(temp_model.from_map(k1))

        self.log_map = {}
        if m.get('LogMap') is not None:
            for k1, v1 in m.get('LogMap').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.DataProductListLogMapValue()
                    l1.append(temp_model.from_map(k2))
                self.log_map[k1] = l1

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        return self

class ListDeliveryResponseBodyDataProductListLogList(DaraModel):
    def __init__(
        self,
        can_operate_or_not: bool = None,
        extra_parameters: List[main_models.ListDeliveryResponseBodyDataProductListLogListExtraParameters] = None,
        log_code: str = None,
        log_name: str = None,
        log_name_en: str = None,
        log_name_key: str = None,
        status: bool = None,
        topic: str = None,
    ):
        # Specifies whether the log delivery switch can be operated. Only the delegated administrator of Threat Analysis can operate the log delivery switch. Valid values:
        # - true: The switch can be operated.
        # - false: The switch cannot be operated.
        self.can_operate_or_not = can_operate_or_not
        # The extended parameters.
        self.extra_parameters = extra_parameters
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
        # The topic of the log in the Logstore. It is an index field of the Logstore and can be used to distinguish different logs.
        self.topic = topic

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
        if self.can_operate_or_not is not None:
            result['CanOperateOrNot'] = self.can_operate_or_not

        result['ExtraParameters'] = []
        if self.extra_parameters is not None:
            for k1 in self.extra_parameters:
                result['ExtraParameters'].append(k1.to_map() if k1 else None)

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

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanOperateOrNot') is not None:
            self.can_operate_or_not = m.get('CanOperateOrNot')

        self.extra_parameters = []
        if m.get('ExtraParameters') is not None:
            for k1 in m.get('ExtraParameters'):
                temp_model = main_models.ListDeliveryResponseBodyDataProductListLogListExtraParameters()
                self.extra_parameters.append(temp_model.from_map(k1))

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

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

class ListDeliveryResponseBodyDataProductListLogListExtraParameters(DaraModel):
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

