# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetAutoResourceOptimizeRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetAutoResourceOptimizeRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
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
            temp_model = main_models.GetAutoResourceOptimizeRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAutoResourceOptimizeRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        enable_auto_resource_optimize_count: int = None,
        enable_auto_resource_optimize_list: List[main_models.GetAutoResourceOptimizeRulesResponseBodyDataEnableAutoResourceOptimizeList] = None,
        has_enable_rule_but_not_das_pro_count: int = None,
        has_enable_rule_but_not_das_pro_list: List[main_models.GetAutoResourceOptimizeRulesResponseBodyDataHasEnableRuleButNotDasProList] = None,
        never_enable_auto_resource_optimize_or_released_instance_count: int = None,
        never_enable_auto_resource_optimize_or_released_instance_id_list: List[str] = None,
        total_auto_resource_optimize_rules_count: int = None,
        turn_off_auto_resource_optimize_count: int = None,
        turn_off_auto_resource_optimize_list: List[main_models.GetAutoResourceOptimizeRulesResponseBodyDataTurnOffAutoResourceOptimizeList] = None,
    ):
        # The number of database instances for which the automatic fragment recycling feature is currently enabled.
        self.enable_auto_resource_optimize_count = enable_auto_resource_optimize_count
        # The database instances for which the automatic fragment recycling feature is currently enabled.
        self.enable_auto_resource_optimize_list = enable_auto_resource_optimize_list
        # The number of database instances for which the automatic fragment recycling feature is enabled and DAS Enterprise Edition is disabled.
        self.has_enable_rule_but_not_das_pro_count = has_enable_rule_but_not_das_pro_count
        # The database instances for which the automatic fragment recycling feature is enabled and DAS Enterprise Edition is disabled.
        # 
        # >  Automatic fragment recycling tasks are run on this type of database instances only if DAS Enterprise Edition is enabled for the database instances again.
        self.has_enable_rule_but_not_das_pro_list = has_enable_rule_but_not_das_pro_list
        # The number of database instances that do not exist or for which the automatic fragment recycling feature has never been enabled.
        # 
        # >  If a database instance does not exist, the instance has been released or the specified instance ID is invalid.
        self.never_enable_auto_resource_optimize_or_released_instance_count = never_enable_auto_resource_optimize_or_released_instance_count
        # The database instances that do not exist or for which the automatic fragment recycling feature has never been enabled.
        self.never_enable_auto_resource_optimize_or_released_instance_id_list = never_enable_auto_resource_optimize_or_released_instance_id_list
        # The number of database instances for which the automatic fragment recycling feature has been enabled.
        self.total_auto_resource_optimize_rules_count = total_auto_resource_optimize_rules_count
        # The number of database instances for which the automatic fragment recycling feature was once enabled but is currently disabled.
        self.turn_off_auto_resource_optimize_count = turn_off_auto_resource_optimize_count
        # The database instances for which the automatic fragment recycling feature was once enabled but is currently disabled.
        self.turn_off_auto_resource_optimize_list = turn_off_auto_resource_optimize_list

    def validate(self):
        if self.enable_auto_resource_optimize_list:
            for v1 in self.enable_auto_resource_optimize_list:
                 if v1:
                    v1.validate()
        if self.has_enable_rule_but_not_das_pro_list:
            for v1 in self.has_enable_rule_but_not_das_pro_list:
                 if v1:
                    v1.validate()
        if self.turn_off_auto_resource_optimize_list:
            for v1 in self.turn_off_auto_resource_optimize_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_auto_resource_optimize_count is not None:
            result['EnableAutoResourceOptimizeCount'] = self.enable_auto_resource_optimize_count

        result['EnableAutoResourceOptimizeList'] = []
        if self.enable_auto_resource_optimize_list is not None:
            for k1 in self.enable_auto_resource_optimize_list:
                result['EnableAutoResourceOptimizeList'].append(k1.to_map() if k1 else None)

        if self.has_enable_rule_but_not_das_pro_count is not None:
            result['HasEnableRuleButNotDasProCount'] = self.has_enable_rule_but_not_das_pro_count

        result['HasEnableRuleButNotDasProList'] = []
        if self.has_enable_rule_but_not_das_pro_list is not None:
            for k1 in self.has_enable_rule_but_not_das_pro_list:
                result['HasEnableRuleButNotDasProList'].append(k1.to_map() if k1 else None)

        if self.never_enable_auto_resource_optimize_or_released_instance_count is not None:
            result['NeverEnableAutoResourceOptimizeOrReleasedInstanceCount'] = self.never_enable_auto_resource_optimize_or_released_instance_count

        if self.never_enable_auto_resource_optimize_or_released_instance_id_list is not None:
            result['NeverEnableAutoResourceOptimizeOrReleasedInstanceIdList'] = self.never_enable_auto_resource_optimize_or_released_instance_id_list

        if self.total_auto_resource_optimize_rules_count is not None:
            result['TotalAutoResourceOptimizeRulesCount'] = self.total_auto_resource_optimize_rules_count

        if self.turn_off_auto_resource_optimize_count is not None:
            result['TurnOffAutoResourceOptimizeCount'] = self.turn_off_auto_resource_optimize_count

        result['TurnOffAutoResourceOptimizeList'] = []
        if self.turn_off_auto_resource_optimize_list is not None:
            for k1 in self.turn_off_auto_resource_optimize_list:
                result['TurnOffAutoResourceOptimizeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAutoResourceOptimizeCount') is not None:
            self.enable_auto_resource_optimize_count = m.get('EnableAutoResourceOptimizeCount')

        self.enable_auto_resource_optimize_list = []
        if m.get('EnableAutoResourceOptimizeList') is not None:
            for k1 in m.get('EnableAutoResourceOptimizeList'):
                temp_model = main_models.GetAutoResourceOptimizeRulesResponseBodyDataEnableAutoResourceOptimizeList()
                self.enable_auto_resource_optimize_list.append(temp_model.from_map(k1))

        if m.get('HasEnableRuleButNotDasProCount') is not None:
            self.has_enable_rule_but_not_das_pro_count = m.get('HasEnableRuleButNotDasProCount')

        self.has_enable_rule_but_not_das_pro_list = []
        if m.get('HasEnableRuleButNotDasProList') is not None:
            for k1 in m.get('HasEnableRuleButNotDasProList'):
                temp_model = main_models.GetAutoResourceOptimizeRulesResponseBodyDataHasEnableRuleButNotDasProList()
                self.has_enable_rule_but_not_das_pro_list.append(temp_model.from_map(k1))

        if m.get('NeverEnableAutoResourceOptimizeOrReleasedInstanceCount') is not None:
            self.never_enable_auto_resource_optimize_or_released_instance_count = m.get('NeverEnableAutoResourceOptimizeOrReleasedInstanceCount')

        if m.get('NeverEnableAutoResourceOptimizeOrReleasedInstanceIdList') is not None:
            self.never_enable_auto_resource_optimize_or_released_instance_id_list = m.get('NeverEnableAutoResourceOptimizeOrReleasedInstanceIdList')

        if m.get('TotalAutoResourceOptimizeRulesCount') is not None:
            self.total_auto_resource_optimize_rules_count = m.get('TotalAutoResourceOptimizeRulesCount')

        if m.get('TurnOffAutoResourceOptimizeCount') is not None:
            self.turn_off_auto_resource_optimize_count = m.get('TurnOffAutoResourceOptimizeCount')

        self.turn_off_auto_resource_optimize_list = []
        if m.get('TurnOffAutoResourceOptimizeList') is not None:
            for k1 in m.get('TurnOffAutoResourceOptimizeList'):
                temp_model = main_models.GetAutoResourceOptimizeRulesResponseBodyDataTurnOffAutoResourceOptimizeList()
                self.turn_off_auto_resource_optimize_list.append(temp_model.from_map(k1))

        return self

class GetAutoResourceOptimizeRulesResponseBodyDataTurnOffAutoResourceOptimizeList(DaraModel):
    def __init__(
        self,
        auto_defragment: bool = None,
        das_pro_on: bool = None,
        instance_id: str = None,
        table_fragmentation_ratio: float = None,
        table_space_size: float = None,
        user_id: str = None,
    ):
        # Indicates whether the automatic fragment recycling feature is enabled. Valid values:
        # 
        # *   **true**:
        # *   **false**
        self.auto_defragment = auto_defragment
        # Indicates whether DAS Enterprise Edition is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.das_pro_on = das_pro_on
        # The database instance ID.
        self.instance_id = instance_id
        # The fragmentation rate of a single physical table for which the automatic fragment recycling feature is enabled.
        self.table_fragmentation_ratio = table_fragmentation_ratio
        # The minimum storage usage of a single physical table for which the automatic fragment recycling feature is enabled. Unit: GB.
        self.table_space_size = table_space_size
        # The ID of the Alibaba Cloud account that is used to create the database instance.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_defragment is not None:
            result['AutoDefragment'] = self.auto_defragment

        if self.das_pro_on is not None:
            result['DasProOn'] = self.das_pro_on

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.table_fragmentation_ratio is not None:
            result['TableFragmentationRatio'] = self.table_fragmentation_ratio

        if self.table_space_size is not None:
            result['TableSpaceSize'] = self.table_space_size

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDefragment') is not None:
            self.auto_defragment = m.get('AutoDefragment')

        if m.get('DasProOn') is not None:
            self.das_pro_on = m.get('DasProOn')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TableFragmentationRatio') is not None:
            self.table_fragmentation_ratio = m.get('TableFragmentationRatio')

        if m.get('TableSpaceSize') is not None:
            self.table_space_size = m.get('TableSpaceSize')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetAutoResourceOptimizeRulesResponseBodyDataHasEnableRuleButNotDasProList(DaraModel):
    def __init__(
        self,
        auto_defragment: bool = None,
        das_pro_on: bool = None,
        instance_id: str = None,
        table_fragmentation_ratio: float = None,
        table_space_size: float = None,
        user_id: str = None,
    ):
        # Indicates whether the automatic fragment recycling feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.auto_defragment = auto_defragment
        # Indicates whether DAS Enterprise Edition is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.das_pro_on = das_pro_on
        # The database instance ID.
        self.instance_id = instance_id
        # The fragmentation rate of a single physical table for which the automatic fragment recycling feature is enabled.
        self.table_fragmentation_ratio = table_fragmentation_ratio
        # The minimum storage usage of a single physical table for which the automatic fragment recycling feature is enabled. Unit: GB.
        self.table_space_size = table_space_size
        # The ID of the Alibaba Cloud account that is used to create the database instance.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_defragment is not None:
            result['AutoDefragment'] = self.auto_defragment

        if self.das_pro_on is not None:
            result['DasProOn'] = self.das_pro_on

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.table_fragmentation_ratio is not None:
            result['TableFragmentationRatio'] = self.table_fragmentation_ratio

        if self.table_space_size is not None:
            result['TableSpaceSize'] = self.table_space_size

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDefragment') is not None:
            self.auto_defragment = m.get('AutoDefragment')

        if m.get('DasProOn') is not None:
            self.das_pro_on = m.get('DasProOn')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TableFragmentationRatio') is not None:
            self.table_fragmentation_ratio = m.get('TableFragmentationRatio')

        if m.get('TableSpaceSize') is not None:
            self.table_space_size = m.get('TableSpaceSize')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetAutoResourceOptimizeRulesResponseBodyDataEnableAutoResourceOptimizeList(DaraModel):
    def __init__(
        self,
        auto_defragment: bool = None,
        das_pro_on: bool = None,
        instance_id: str = None,
        table_fragmentation_ratio: float = None,
        table_space_size: float = None,
        user_id: str = None,
    ):
        # Indicates whether the automatic fragment recycling feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.auto_defragment = auto_defragment
        # Indicates whether DAS Enterprise Edition is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.das_pro_on = das_pro_on
        # The database instance ID.
        self.instance_id = instance_id
        # The fragmentation rate of a single physical table for which the automatic fragment recycling feature is enabled.
        self.table_fragmentation_ratio = table_fragmentation_ratio
        # The minimum storage usage of a single physical table for which the automatic fragment recycling feature is enabled. Unit: GB.
        self.table_space_size = table_space_size
        # The ID of the Alibaba Cloud account that is used to create the database instance.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_defragment is not None:
            result['AutoDefragment'] = self.auto_defragment

        if self.das_pro_on is not None:
            result['DasProOn'] = self.das_pro_on

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.table_fragmentation_ratio is not None:
            result['TableFragmentationRatio'] = self.table_fragmentation_ratio

        if self.table_space_size is not None:
            result['TableSpaceSize'] = self.table_space_size

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDefragment') is not None:
            self.auto_defragment = m.get('AutoDefragment')

        if m.get('DasProOn') is not None:
            self.das_pro_on = m.get('DasProOn')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TableFragmentationRatio') is not None:
            self.table_fragmentation_ratio = m.get('TableFragmentationRatio')

        if m.get('TableSpaceSize') is not None:
            self.table_space_size = m.get('TableSpaceSize')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

