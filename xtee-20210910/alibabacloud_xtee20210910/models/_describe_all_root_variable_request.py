# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAllRootVariableRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
        device_variable_ids: str = None,
        event_code: str = None,
        expression_variable_ids: str = None,
        id: int = None,
        native_variable_ids: str = None,
        query_variable_ids: str = None,
        reg_id: str = None,
        velocity_variable_ids: str = None,
    ):
        # Set the language type for requests and received messages, default value is **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Request source IP. No need to fill in, the system will automatically obtain it.
        self.source_ip = source_ip
        # Device variable list
        self.device_variable_ids = device_variable_ids
        # Event code
        self.event_code = event_code
        # Custom variable list
        self.expression_variable_ids = expression_variable_ids
        # Variable ID.
        self.id = id
        # Event field list
        self.native_variable_ids = native_variable_ids
        # Custom query variable
        self.query_variable_ids = query_variable_ids
        # Region code
        self.reg_id = reg_id
        # Custom cumulative variable
        self.velocity_variable_ids = velocity_variable_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.device_variable_ids is not None:
            result['deviceVariableIds'] = self.device_variable_ids

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.expression_variable_ids is not None:
            result['expressionVariableIds'] = self.expression_variable_ids

        if self.id is not None:
            result['id'] = self.id

        if self.native_variable_ids is not None:
            result['nativeVariableIds'] = self.native_variable_ids

        if self.query_variable_ids is not None:
            result['queryVariableIds'] = self.query_variable_ids

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.velocity_variable_ids is not None:
            result['velocityVariableIds'] = self.velocity_variable_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('deviceVariableIds') is not None:
            self.device_variable_ids = m.get('deviceVariableIds')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('expressionVariableIds') is not None:
            self.expression_variable_ids = m.get('expressionVariableIds')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('nativeVariableIds') is not None:
            self.native_variable_ids = m.get('nativeVariableIds')

        if m.get('queryVariableIds') is not None:
            self.query_variable_ids = m.get('queryVariableIds')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('velocityVariableIds') is not None:
            self.velocity_variable_ids = m.get('velocityVariableIds')

        return self

