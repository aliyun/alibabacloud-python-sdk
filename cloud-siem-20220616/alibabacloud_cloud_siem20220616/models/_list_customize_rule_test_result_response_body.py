# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class ListCustomizeRuleTestResultResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListCustomizeRuleTestResultResponseBodyData = None,
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
            temp_model = main_models.ListCustomizeRuleTestResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCustomizeRuleTestResultResponseBodyData(DaraModel):
    def __init__(
        self,
        page_info: main_models.ListCustomizeRuleTestResultResponseBodyDataPageInfo = None,
        response_data: List[main_models.ListCustomizeRuleTestResultResponseBodyDataResponseData] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The detailed data.
        self.response_data = response_data

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for v1 in self.response_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        result['ResponseData'] = []
        if self.response_data is not None:
            for k1 in self.response_data:
                result['ResponseData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.ListCustomizeRuleTestResultResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.response_data = []
        if m.get('ResponseData') is not None:
            for k1 in m.get('ResponseData'):
                temp_model = main_models.ListCustomizeRuleTestResultResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k1))

        return self

class ListCustomizeRuleTestResultResponseBodyDataResponseData(DaraModel):
    def __init__(
        self,
        alert_desc: str = None,
        alert_detail: str = None,
        alert_src_prod: str = None,
        alert_src_prod_module: str = None,
        att_ck: str = None,
        event_name: str = None,
        event_type: str = None,
        level: str = None,
        log_source: str = None,
        log_time: str = None,
        log_type: str = None,
        main_user_id: str = None,
        online_status: str = None,
        sub_user_id: str = None,
        uuid: str = None,
        verify_type: str = None,
    ):
        # The description of the alert.
        self.alert_desc = alert_desc
        # The alert details in the JSON format.
        self.alert_detail = alert_detail
        # The source of the alert.
        self.alert_src_prod = alert_src_prod
        # The sub-module of the source.
        self.alert_src_prod_module = alert_src_prod_module
        # The tag of the ATT\\&CK attack.
        self.att_ck = att_ck
        # The name of the alert, which corresponds to the name of the custom rule.
        self.event_name = event_name
        # The threat type, which indicates the alert type.
        self.event_type = event_type
        # The threat level. Valid values:
        # 
        # *   serious: high.
        # *   suspicious: medium.
        # *   remind: low.
        self.level = level
        # The log source of the rule.
        self.log_source = log_source
        # The time when the alert was recorded.
        self.log_time = log_time
        # The log type of the rule.
        self.log_type = log_type
        # The ID of the Alibaba Cloud account that is associated with the alert in SIEM.
        self.main_user_id = main_user_id
        # The status of the alert data. Valid values:
        # 
        # *   test: business test data.
        # *   online: online data.
        self.online_status = online_status
        # The ID of the Alibaba Cloud account within which the alert is generated.
        self.sub_user_id = sub_user_id
        # The UUID of the alert.
        self.uuid = uuid
        self.verify_type = verify_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_desc is not None:
            result['AlertDesc'] = self.alert_desc

        if self.alert_detail is not None:
            result['AlertDetail'] = self.alert_detail

        if self.alert_src_prod is not None:
            result['AlertSrcProd'] = self.alert_src_prod

        if self.alert_src_prod_module is not None:
            result['AlertSrcProdModule'] = self.alert_src_prod_module

        if self.att_ck is not None:
            result['AttCk'] = self.att_ck

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.level is not None:
            result['Level'] = self.level

        if self.log_source is not None:
            result['LogSource'] = self.log_source

        if self.log_time is not None:
            result['LogTime'] = self.log_time

        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id

        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertDesc') is not None:
            self.alert_desc = m.get('AlertDesc')

        if m.get('AlertDetail') is not None:
            self.alert_detail = m.get('AlertDetail')

        if m.get('AlertSrcProd') is not None:
            self.alert_src_prod = m.get('AlertSrcProd')

        if m.get('AlertSrcProdModule') is not None:
            self.alert_src_prod_module = m.get('AlertSrcProdModule')

        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')

        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')

        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')

        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')

        return self

class ListCustomizeRuleTestResultResponseBodyDataPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        verified_count: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count
        self.verified_count = verified_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.verified_count is not None:
            result['VerifiedCount'] = self.verified_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('VerifiedCount') is not None:
            self.verified_count = m.get('VerifiedCount')

        return self

