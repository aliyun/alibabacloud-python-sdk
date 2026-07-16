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
        # The filter conditions. This parameter is in JSON format. Pay attention to the letter case when you specify this parameter. The following fields are included:
        # 
        # - **filterParams**: The filter parameters. This parameter is in JSON format. The following fields are included:
        #   - **label**: The display name for the search in the console.
        #   - **value**: The filter parameter condition. This parameter is in JSON format. The following fields are included:
        # 
        #      - **name**: The filter condition field. For more information about the valid values of this field, see the description below.
        #      - **value**: The value that corresponds to the filter condition field.
        # 
        # - **LogicalExp**: The logical relationship between multiple filter conditions. Valid values:
        #   - **OR**: or
        #   - **AND**: and
        # > Valid values of **name**:
        # > - If **Type** is set to **ecs**, call the [DescribeCriteria](~~DescribeCriteria~~) operation to query the supported search conditions.
        # > - If **Type** is set to **cloud_product**, call the [GetCloudAssetCriteria](~~GetCloudAssetCriteria~~) operation to query the supported search conditions.
        self.filter_conditions = filter_conditions
        # The name of the common filter condition.
        # 
        # This parameter is required.
        self.name = name
        # The source IP address of the request. You do not need to specify this parameter. The system automatically obtains the value.
        self.source_ip = source_ip
        # The asset type. Default value: **ecs**. Valid values:
        # - **ecs**: host asset
        # - **cloud_product**: cloud service.
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

