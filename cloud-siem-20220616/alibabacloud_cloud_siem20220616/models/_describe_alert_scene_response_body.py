# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeAlertSceneResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.DescribeAlertSceneResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
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
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeAlertSceneResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeAlertSceneResponseBodyData(DaraModel):
    def __init__(
        self,
        alert_name: str = None,
        alert_name_id: str = None,
        alert_tile: str = None,
        alert_tile_id: str = None,
        alert_type: str = None,
        alert_type_id: str = None,
        targets: List[main_models.DescribeAlertSceneResponseBodyDataTargets] = None,
    ):
        # The name of the alert. The value varies based on the display language (Chinese or English) of the Security Center console.
        self.alert_name = alert_name
        # The ID of the alert name.
        self.alert_name_id = alert_name_id
        # The title of the alert notification. The value varies based on the display language (Chinese or English) of the Security Center console.
        self.alert_tile = alert_tile
        # The ID of the alert title.
        self.alert_tile_id = alert_tile_id
        # The type of the alert. The value varies based on the display language (Chinese or English) of the Security Center console.
        self.alert_type = alert_type
        # The ID of the alert type.
        self.alert_type_id = alert_type_id
        # The information about the entities for which you need to add the alert to the whitelist.
        self.targets = targets

    def validate(self):
        if self.targets:
            for v1 in self.targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name

        if self.alert_name_id is not None:
            result['AlertNameId'] = self.alert_name_id

        if self.alert_tile is not None:
            result['AlertTile'] = self.alert_tile

        if self.alert_tile_id is not None:
            result['AlertTileId'] = self.alert_tile_id

        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.alert_type_id is not None:
            result['AlertTypeId'] = self.alert_type_id

        result['Targets'] = []
        if self.targets is not None:
            for k1 in self.targets:
                result['Targets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')

        if m.get('AlertNameId') is not None:
            self.alert_name_id = m.get('AlertNameId')

        if m.get('AlertTile') is not None:
            self.alert_tile = m.get('AlertTile')

        if m.get('AlertTileId') is not None:
            self.alert_tile_id = m.get('AlertTileId')

        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('AlertTypeId') is not None:
            self.alert_type_id = m.get('AlertTypeId')

        self.targets = []
        if m.get('Targets') is not None:
            for k1 in m.get('Targets'):
                temp_model = main_models.DescribeAlertSceneResponseBodyDataTargets()
                self.targets.append(temp_model.from_map(k1))

        return self

class DescribeAlertSceneResponseBodyDataTargets(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
        values: List[str] = None,
    ):
        # The display name of the attribute for the entity.
        self.name = name
        # The attribute of the entity.
        self.type = type
        # The right operand that is displayed by default in the whitelist rule.
        self.value = value
        # The right operands supported by the whitelist rule.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

