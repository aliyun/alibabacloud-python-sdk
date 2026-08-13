# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class GetEntitiyStatResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.GetEntitiyStatResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - true: The request was successful.
        # - false: The request failed.
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
                temp_model = main_models.GetEntitiyStatResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetEntitiyStatResponseBodyData(DaraModel):
    def __init__(
        self,
        alert_num: int = None,
        entity_num: int = None,
        entity_type: str = None,
        entity_uuid: str = None,
        incident_num: int = None,
    ):
        self.alert_num = alert_num
        # The number of entities.
        self.entity_num = entity_num
        # The entity type.
        self.entity_type = entity_type
        # The entity UUID.
        self.entity_uuid = entity_uuid
        self.incident_num = incident_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_num is not None:
            result['AlertNum'] = self.alert_num

        if self.entity_num is not None:
            result['EntityNum'] = self.entity_num

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.entity_uuid is not None:
            result['EntityUuid'] = self.entity_uuid

        if self.incident_num is not None:
            result['IncidentNum'] = self.incident_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertNum') is not None:
            self.alert_num = m.get('AlertNum')

        if m.get('EntityNum') is not None:
            self.entity_num = m.get('EntityNum')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('EntityUuid') is not None:
            self.entity_uuid = m.get('EntityUuid')

        if m.get('IncidentNum') is not None:
            self.incident_num = m.get('IncidentNum')

        return self

