# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20251111 import models as main_models
from darabonba.model import DaraModel

class ListInstructionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListInstructionsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The data returned for the list of instructions.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The result message.
        self.message = message
        # A list of request parameters that are echoed in the response.
        self.params = params
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
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListInstructionsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListInstructionsResponseBodyData(DaraModel):
    def __init__(
        self,
        instructions: List[main_models.ListInstructionsResponseBodyDataInstructions] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of instructions.
        self.instructions = instructions
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The total number of instructions.
        self.total_count = total_count

    def validate(self):
        if self.instructions:
            for v1 in self.instructions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instructions'] = []
        if self.instructions is not None:
            for k1 in self.instructions:
                result['Instructions'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instructions = []
        if m.get('Instructions') is not None:
            for k1 in m.get('Instructions'):
                temp_model = main_models.ListInstructionsResponseBodyDataInstructions()
                self.instructions.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstructionsResponseBodyDataInstructions(DaraModel):
    def __init__(
        self,
        code: str = None,
        config: str = None,
        instance_id: str = None,
        name: str = None,
        type: str = None,
    ):
        # The instruction code.
        self.code = code
        # The instruction configuration, in a JSON string format.
        # 
        # > - `providerId`: The ID of the call center provider. You can obtain this ID by calling the `ListCallCenterProviders` operation.
        # >
        # > - `transferMethod`: The transfer method. Valid values: `BYE`, `BRIDGE`, and `REFER`.
        # >
        # > - `transferType`: The transfer target type. Valid values: `External` (external number), `Agent` (agent), and `SkillGroup` (skill group).
        # >
        # > - `transferTarget`: The transfer target.
        # >
        # > - `transferor`: The caller ID. If not specified, the caller\\"s phone number is used.
        # >
        # > - `timeoutSeconds`: The transfer timeout, in seconds. The default value is 30.
        self.config = config
        # The instance ID.
        self.instance_id = instance_id
        # The instruction name.
        self.name = name
        # The instruction type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.config is not None:
            result['Config'] = self.config

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

