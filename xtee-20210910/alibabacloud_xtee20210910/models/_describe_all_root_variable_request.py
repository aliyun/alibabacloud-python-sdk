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
        # The language of the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The source IP address of the request. You do not need to specify this parameter. The system automatically obtains the value.
        self.source_ip = source_ip
        # The list of device variables.
        self.device_variable_ids = device_variable_ids
        # The event code.
        self.event_code = event_code
        # The list of custom variables.
        self.expression_variable_ids = expression_variable_ids
        # The variable ID.
        self.id = id
        # The list of event fields.
        self.native_variable_ids = native_variable_ids
        # The custom query variables.
        self.query_variable_ids = query_variable_ids
        # The region code.
        self.reg_id = reg_id
        # The custom cumulative variables.
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

