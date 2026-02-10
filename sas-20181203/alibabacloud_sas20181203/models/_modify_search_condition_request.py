# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySearchConditionRequest(DaraModel):
    def __init__(
        self,
        filter_conditions: str = None,
        name: str = None,
        source_ip: str = None,
        type: str = None,
    ):
        # The filter condition. The value of this parameter is in the JSON format and is case-sensitive. The value contains the following fields:
        # 
        # *   **filterParams**: the filter-related parameters. The value is in the JSON format. Valid values:
        # 
        #     *   **label**: the display name of the filter condition in the console.
        # 
        #     *   **value**: the settings of the filter condition. The value is in the JSON format. The value contains the following fields:
        # 
        #         *   **name**: the name of the field for filtering. For more information, see the value description of name.
        #         *   **value**: the value of the field for filtering.
        # 
        # *   **LogicalExp**: the logical relationship among multiple filter conditions. Valid values:
        # 
        #     *   **OR**
        #     *   **AND**
        # 
        # >  Value description of **name**:
        # 
        # *   If **Type** is set to **ecs**, you can call the [DescribeCriteria](~~DescribeCriteria~~) operation to query the supported filter conditions.
        # 
        # *   If **Type** is set to **cloud_product**, you can call the [GetCloudAssetCriteria](~~GetCloudAssetCriteria~~) operation to query the supported filter conditions.
        self.filter_conditions = filter_conditions
        # The name of the common filter condition.
        # 
        # This parameter is required.
        self.name = name
        # The source IP address of the request. You do not need to specify this parameter. It is automatically obtained by the system.
        self.source_ip = source_ip
        # The type of the asset. Default value: **ecs**. Valid values:
        # 
        # *   **ecs**: host
        # *   **cloud_product**: Alibaba Cloud service
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_conditions is not None:
            result['FilterConditions'] = self.filter_conditions

        if self.name is not None:
            result['Name'] = self.name

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterConditions') is not None:
            self.filter_conditions = m.get('FilterConditions')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

