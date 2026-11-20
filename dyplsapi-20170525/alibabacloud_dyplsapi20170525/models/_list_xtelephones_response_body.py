# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyplsapi20170525 import models as main_models
from darabonba.model import DaraModel

class ListXTelephonesResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.ListXTelephonesResponseBodyData = None,
        message: str = None,
        success: bool = None,
    ):
        # The details of the access denied error.
        self.access_denied_detail = access_denied_detail
        # The response status code. Valid values:
        # 
        # - 0000: Success.
        # 
        # - Other values: Failure.
        self.code = code
        # The data collection.
        self.data = data
        # The response message.
        self.message = message
        # Indicates whether the request is successful. Valid values:
        # 
        # - true: Success.
        # 
        # - false: Failure.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListXTelephonesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListXTelephonesResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListXTelephonesResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The data list.
        self.list = list
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries that meet the query conditions.
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListXTelephonesResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListXTelephonesResponseBodyDataList(DaraModel):
    def __init__(
        self,
        auth_msg: str = None,
        bind_time: str = None,
        buy_time: str = None,
        customer_pool_key: str = None,
        customer_pool_name: str = None,
        release_time: str = None,
        sms_status: str = None,
        telephone: str = None,
        telephone_status: str = None,
        unbind_time: str = None,
    ):
        # The reason for binding failure.
        self.auth_msg = auth_msg
        # The binding time. The format is YYYY-MM-DD HH:mm:ss.
        self.bind_time = bind_time
        # The purchase time. The format is YYYY-MM-DD HH:mm:ss.
        self.buy_time = buy_time
        # The customer number pool key.
        self.customer_pool_key = customer_pool_key
        # The number pool name.
        self.customer_pool_name = customer_pool_name
        # The release time. The format is YYYY-MM-DD HH:mm:ss.
        self.release_time = release_time
        # The SMS activation status. Valid values:
        # - 0: Not activated.
        # - 1: Activated.
        self.sms_status = sms_status
        # The X number.
        self.telephone = telephone
        # The number status. Valid values:
        # - 0: Idle.
        # - 1: Allocation completed and pending purchase.
        # - 2: Purchase completed and pending verification.
        # - 3: Real-name verification in progress.
        # - 4: Real-name verification succeeded.
        # - 5: Verification failed.
        # - 6: Unbinding in progress.
        # - 7: Unbinding failed.
        # - 8: Released.
        # - 99: Released due to timeout.
        self.telephone_status = telephone_status
        # The unbinding time. The format is YYYY-MM-DD HH:mm:ss.
        self.unbind_time = unbind_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_msg is not None:
            result['AuthMsg'] = self.auth_msg

        if self.bind_time is not None:
            result['BindTime'] = self.bind_time

        if self.buy_time is not None:
            result['BuyTime'] = self.buy_time

        if self.customer_pool_key is not None:
            result['CustomerPoolKey'] = self.customer_pool_key

        if self.customer_pool_name is not None:
            result['CustomerPoolName'] = self.customer_pool_name

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        if self.sms_status is not None:
            result['SmsStatus'] = self.sms_status

        if self.telephone is not None:
            result['Telephone'] = self.telephone

        if self.telephone_status is not None:
            result['TelephoneStatus'] = self.telephone_status

        if self.unbind_time is not None:
            result['UnbindTime'] = self.unbind_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthMsg') is not None:
            self.auth_msg = m.get('AuthMsg')

        if m.get('BindTime') is not None:
            self.bind_time = m.get('BindTime')

        if m.get('BuyTime') is not None:
            self.buy_time = m.get('BuyTime')

        if m.get('CustomerPoolKey') is not None:
            self.customer_pool_key = m.get('CustomerPoolKey')

        if m.get('CustomerPoolName') is not None:
            self.customer_pool_name = m.get('CustomerPoolName')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        if m.get('SmsStatus') is not None:
            self.sms_status = m.get('SmsStatus')

        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')

        if m.get('TelephoneStatus') is not None:
            self.telephone_status = m.get('TelephoneStatus')

        if m.get('UnbindTime') is not None:
            self.unbind_time = m.get('UnbindTime')

        return self

