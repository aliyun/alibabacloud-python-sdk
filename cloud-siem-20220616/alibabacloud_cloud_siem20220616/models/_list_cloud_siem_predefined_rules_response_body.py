# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class ListCloudSiemPredefinedRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListCloudSiemPredefinedRulesResponseBodyData = None,
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
            temp_model = main_models.ListCloudSiemPredefinedRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCloudSiemPredefinedRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        page_info: main_models.ListCloudSiemPredefinedRulesResponseBodyDataPageInfo = None,
        response_data: List[main_models.ListCloudSiemPredefinedRulesResponseBodyDataResponseData] = None,
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
            temp_model = main_models.ListCloudSiemPredefinedRulesResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.response_data = []
        if m.get('ResponseData') is not None:
            for k1 in m.get('ResponseData'):
                temp_model = main_models.ListCloudSiemPredefinedRulesResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k1))

        return self

class ListCloudSiemPredefinedRulesResponseBodyDataResponseData(DaraModel):
    def __init__(
        self,
        alert_type: str = None,
        att_ck: str = None,
        event_transfer_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        rule_desc_mds: str = None,
        rule_name: str = None,
        rule_name_cn: str = None,
        rule_name_en: str = None,
        rule_name_mds: str = None,
        source: str = None,
        status: int = None,
        threat_level: str = None,
    ):
        # The type of the risk.
        self.alert_type = alert_type
        # The alert additional field for ATT\\&CK.
        self.att_ck = att_ck
        # The method that is used to generate an event. Valid values:
        # 
        # *   default: built-in method.
        # *   singleToSingle: The system generates an event for each alert.
        # *   allToSingle: The system generates an event for alerts within a period of time.
        self.event_transfer_type = event_transfer_type
        # The time when the rule was created.
        self.gmt_create = gmt_create
        # The time when the rule was modified.
        self.gmt_modified = gmt_modified
        # The ID of the predefined rule.
        self.id = id
        # The internal code of the rule description.
        self.rule_desc_mds = rule_desc_mds
        # The name of the rule.
        self.rule_name = rule_name
        # The rule name in Chinese.
        self.rule_name_cn = rule_name_cn
        # The rule name in English.
        self.rule_name_en = rule_name_en
        # The internal code of the rule name.
        self.rule_name_mds = rule_name_mds
        # The log source of the rule.
        self.source = source
        # The status of the predefined rule. Valid values:
        # 
        # *   0: The rule is in the initial state.
        # *   100: The rule takes effect.
        self.status = status
        # The risk level. Valid values:
        # 
        # *   serious: high.
        # *   suspicious: medium.
        # *   remind: low.
        self.threat_level = threat_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.att_ck is not None:
            result['AttCk'] = self.att_ck

        if self.event_transfer_type is not None:
            result['EventTransferType'] = self.event_transfer_type

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.rule_desc_mds is not None:
            result['RuleDescMds'] = self.rule_desc_mds

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_name_cn is not None:
            result['RuleNameCn'] = self.rule_name_cn

        if self.rule_name_en is not None:
            result['RuleNameEn'] = self.rule_name_en

        if self.rule_name_mds is not None:
            result['RuleNameMds'] = self.rule_name_mds

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')

        if m.get('EventTransferType') is not None:
            self.event_transfer_type = m.get('EventTransferType')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RuleDescMds') is not None:
            self.rule_desc_mds = m.get('RuleDescMds')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleNameCn') is not None:
            self.rule_name_cn = m.get('RuleNameCn')

        if m.get('RuleNameEn') is not None:
            self.rule_name_en = m.get('RuleNameEn')

        if m.get('RuleNameMds') is not None:
            self.rule_name_mds = m.get('RuleNameMds')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')

        return self

class ListCloudSiemPredefinedRulesResponseBodyDataPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

