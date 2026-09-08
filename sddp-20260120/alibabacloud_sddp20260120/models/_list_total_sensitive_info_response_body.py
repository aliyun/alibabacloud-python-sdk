# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20260120 import models as main_models
from darabonba.model import DaraModel

class ListTotalSensitiveInfoResponseBody(DaraModel):
    def __init__(
        self,
        data_count_dolist: List[main_models.ListTotalSensitiveInfoResponseBodyDataCountDOList] = None,
        db_count: int = None,
        instance_count: int = None,
        request_id: str = None,
        rule_info_list: List[main_models.ListTotalSensitiveInfoResponseBodyRuleInfoList] = None,
        s_0count: int = None,
        s_10count: int = None,
        s_1count: int = None,
        s_2count: int = None,
        s_3count: int = None,
        s_4count: int = None,
        s_5count: int = None,
        s_6count: int = None,
        s_7count: int = None,
        s_8count: int = None,
        s_9count: int = None,
        sensitive_count: int = None,
        sensitive_db_count: int = None,
        sensitive_instance_count: int = None,
        sensitive_un_struct_size: int = None,
        sub_sensitive_count: int = None,
        sub_total_count: int = None,
        total_count: int = None,
        un_struct_size: int = None,
    ):
        self.data_count_dolist = data_count_dolist
        self.db_count = db_count
        self.instance_count = instance_count
        self.request_id = request_id
        self.rule_info_list = rule_info_list
        self.s_0count = s_0count
        self.s_10count = s_10count
        self.s_1count = s_1count
        self.s_2count = s_2count
        self.s_3count = s_3count
        self.s_4count = s_4count
        self.s_5count = s_5count
        self.s_6count = s_6count
        self.s_7count = s_7count
        self.s_8count = s_8count
        self.s_9count = s_9count
        self.sensitive_count = sensitive_count
        self.sensitive_db_count = sensitive_db_count
        self.sensitive_instance_count = sensitive_instance_count
        self.sensitive_un_struct_size = sensitive_un_struct_size
        self.sub_sensitive_count = sub_sensitive_count
        self.sub_total_count = sub_total_count
        self.total_count = total_count
        self.un_struct_size = un_struct_size

    def validate(self):
        if self.data_count_dolist:
            for v1 in self.data_count_dolist:
                 if v1:
                    v1.validate()
        if self.rule_info_list:
            for v1 in self.rule_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataCountDOList'] = []
        if self.data_count_dolist is not None:
            for k1 in self.data_count_dolist:
                result['DataCountDOList'].append(k1.to_map() if k1 else None)

        if self.db_count is not None:
            result['DbCount'] = self.db_count

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RuleInfoList'] = []
        if self.rule_info_list is not None:
            for k1 in self.rule_info_list:
                result['RuleInfoList'].append(k1.to_map() if k1 else None)

        if self.s_0count is not None:
            result['S0Count'] = self.s_0count

        if self.s_10count is not None:
            result['S10Count'] = self.s_10count

        if self.s_1count is not None:
            result['S1Count'] = self.s_1count

        if self.s_2count is not None:
            result['S2Count'] = self.s_2count

        if self.s_3count is not None:
            result['S3Count'] = self.s_3count

        if self.s_4count is not None:
            result['S4Count'] = self.s_4count

        if self.s_5count is not None:
            result['S5Count'] = self.s_5count

        if self.s_6count is not None:
            result['S6Count'] = self.s_6count

        if self.s_7count is not None:
            result['S7Count'] = self.s_7count

        if self.s_8count is not None:
            result['S8Count'] = self.s_8count

        if self.s_9count is not None:
            result['S9Count'] = self.s_9count

        if self.sensitive_count is not None:
            result['SensitiveCount'] = self.sensitive_count

        if self.sensitive_db_count is not None:
            result['SensitiveDbCount'] = self.sensitive_db_count

        if self.sensitive_instance_count is not None:
            result['SensitiveInstanceCount'] = self.sensitive_instance_count

        if self.sensitive_un_struct_size is not None:
            result['SensitiveUnStructSize'] = self.sensitive_un_struct_size

        if self.sub_sensitive_count is not None:
            result['SubSensitiveCount'] = self.sub_sensitive_count

        if self.sub_total_count is not None:
            result['SubTotalCount'] = self.sub_total_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.un_struct_size is not None:
            result['UnStructSize'] = self.un_struct_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_count_dolist = []
        if m.get('DataCountDOList') is not None:
            for k1 in m.get('DataCountDOList'):
                temp_model = main_models.ListTotalSensitiveInfoResponseBodyDataCountDOList()
                self.data_count_dolist.append(temp_model.from_map(k1))

        if m.get('DbCount') is not None:
            self.db_count = m.get('DbCount')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rule_info_list = []
        if m.get('RuleInfoList') is not None:
            for k1 in m.get('RuleInfoList'):
                temp_model = main_models.ListTotalSensitiveInfoResponseBodyRuleInfoList()
                self.rule_info_list.append(temp_model.from_map(k1))

        if m.get('S0Count') is not None:
            self.s_0count = m.get('S0Count')

        if m.get('S10Count') is not None:
            self.s_10count = m.get('S10Count')

        if m.get('S1Count') is not None:
            self.s_1count = m.get('S1Count')

        if m.get('S2Count') is not None:
            self.s_2count = m.get('S2Count')

        if m.get('S3Count') is not None:
            self.s_3count = m.get('S3Count')

        if m.get('S4Count') is not None:
            self.s_4count = m.get('S4Count')

        if m.get('S5Count') is not None:
            self.s_5count = m.get('S5Count')

        if m.get('S6Count') is not None:
            self.s_6count = m.get('S6Count')

        if m.get('S7Count') is not None:
            self.s_7count = m.get('S7Count')

        if m.get('S8Count') is not None:
            self.s_8count = m.get('S8Count')

        if m.get('S9Count') is not None:
            self.s_9count = m.get('S9Count')

        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')

        if m.get('SensitiveDbCount') is not None:
            self.sensitive_db_count = m.get('SensitiveDbCount')

        if m.get('SensitiveInstanceCount') is not None:
            self.sensitive_instance_count = m.get('SensitiveInstanceCount')

        if m.get('SensitiveUnStructSize') is not None:
            self.sensitive_un_struct_size = m.get('SensitiveUnStructSize')

        if m.get('SubSensitiveCount') is not None:
            self.sub_sensitive_count = m.get('SubSensitiveCount')

        if m.get('SubTotalCount') is not None:
            self.sub_total_count = m.get('SubTotalCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UnStructSize') is not None:
            self.un_struct_size = m.get('UnStructSize')

        return self

class ListTotalSensitiveInfoResponseBodyRuleInfoList(DaraModel):
    def __init__(
        self,
        rule_count: int = None,
        rule_id: int = None,
        rule_name: str = None,
    ):
        self.rule_count = rule_count
        self.rule_id = rule_id
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

class ListTotalSensitiveInfoResponseBodyDataCountDOList(DaraModel):
    def __init__(
        self,
        data_count_dolist: List[main_models.ListTotalSensitiveInfoResponseBodyDataCountDOListDataCountDOList] = None,
        date: int = None,
        region_id: str = None,
        rule_info_list: List[main_models.ListTotalSensitiveInfoResponseBodyDataCountDOListRuleInfoList] = None,
        s_0count: int = None,
        s_10count: int = None,
        s_1count: int = None,
        s_2count: int = None,
        s_3count: int = None,
        s_4count: int = None,
        s_5count: int = None,
        s_6count: int = None,
        s_7count: int = None,
        s_8count: int = None,
        s_9count: int = None,
        sensitive_count: int = None,
        struct_flag: int = None,
        template_id: int = None,
        template_name: str = None,
        total_count: int = None,
    ):
        self.data_count_dolist = data_count_dolist
        self.date = date
        self.region_id = region_id
        self.rule_info_list = rule_info_list
        self.s_0count = s_0count
        self.s_10count = s_10count
        self.s_1count = s_1count
        self.s_2count = s_2count
        self.s_3count = s_3count
        self.s_4count = s_4count
        self.s_5count = s_5count
        self.s_6count = s_6count
        self.s_7count = s_7count
        self.s_8count = s_8count
        self.s_9count = s_9count
        self.sensitive_count = sensitive_count
        self.struct_flag = struct_flag
        self.template_id = template_id
        self.template_name = template_name
        self.total_count = total_count

    def validate(self):
        if self.data_count_dolist:
            for v1 in self.data_count_dolist:
                 if v1:
                    v1.validate()
        if self.rule_info_list:
            for v1 in self.rule_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataCountDOList'] = []
        if self.data_count_dolist is not None:
            for k1 in self.data_count_dolist:
                result['DataCountDOList'].append(k1.to_map() if k1 else None)

        if self.date is not None:
            result['Date'] = self.date

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['RuleInfoList'] = []
        if self.rule_info_list is not None:
            for k1 in self.rule_info_list:
                result['RuleInfoList'].append(k1.to_map() if k1 else None)

        if self.s_0count is not None:
            result['S0Count'] = self.s_0count

        if self.s_10count is not None:
            result['S10Count'] = self.s_10count

        if self.s_1count is not None:
            result['S1Count'] = self.s_1count

        if self.s_2count is not None:
            result['S2Count'] = self.s_2count

        if self.s_3count is not None:
            result['S3Count'] = self.s_3count

        if self.s_4count is not None:
            result['S4Count'] = self.s_4count

        if self.s_5count is not None:
            result['S5Count'] = self.s_5count

        if self.s_6count is not None:
            result['S6Count'] = self.s_6count

        if self.s_7count is not None:
            result['S7Count'] = self.s_7count

        if self.s_8count is not None:
            result['S8Count'] = self.s_8count

        if self.s_9count is not None:
            result['S9Count'] = self.s_9count

        if self.sensitive_count is not None:
            result['SensitiveCount'] = self.sensitive_count

        if self.struct_flag is not None:
            result['StructFlag'] = self.struct_flag

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_count_dolist = []
        if m.get('DataCountDOList') is not None:
            for k1 in m.get('DataCountDOList'):
                temp_model = main_models.ListTotalSensitiveInfoResponseBodyDataCountDOListDataCountDOList()
                self.data_count_dolist.append(temp_model.from_map(k1))

        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.rule_info_list = []
        if m.get('RuleInfoList') is not None:
            for k1 in m.get('RuleInfoList'):
                temp_model = main_models.ListTotalSensitiveInfoResponseBodyDataCountDOListRuleInfoList()
                self.rule_info_list.append(temp_model.from_map(k1))

        if m.get('S0Count') is not None:
            self.s_0count = m.get('S0Count')

        if m.get('S10Count') is not None:
            self.s_10count = m.get('S10Count')

        if m.get('S1Count') is not None:
            self.s_1count = m.get('S1Count')

        if m.get('S2Count') is not None:
            self.s_2count = m.get('S2Count')

        if m.get('S3Count') is not None:
            self.s_3count = m.get('S3Count')

        if m.get('S4Count') is not None:
            self.s_4count = m.get('S4Count')

        if m.get('S5Count') is not None:
            self.s_5count = m.get('S5Count')

        if m.get('S6Count') is not None:
            self.s_6count = m.get('S6Count')

        if m.get('S7Count') is not None:
            self.s_7count = m.get('S7Count')

        if m.get('S8Count') is not None:
            self.s_8count = m.get('S8Count')

        if m.get('S9Count') is not None:
            self.s_9count = m.get('S9Count')

        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')

        if m.get('StructFlag') is not None:
            self.struct_flag = m.get('StructFlag')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTotalSensitiveInfoResponseBodyDataCountDOListRuleInfoList(DaraModel):
    def __init__(
        self,
        rule_count: int = None,
        rule_id: int = None,
        rule_name: str = None,
    ):
        self.rule_count = rule_count
        self.rule_id = rule_id
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

class ListTotalSensitiveInfoResponseBodyDataCountDOListDataCountDOList(DaraModel):
    def __init__(
        self,
        date: int = None,
        sensitive_count: int = None,
        total_count: int = None,
    ):
        self.date = date
        self.sensitive_count = sensitive_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.sensitive_count is not None:
            result['SensitiveCount'] = self.sensitive_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

