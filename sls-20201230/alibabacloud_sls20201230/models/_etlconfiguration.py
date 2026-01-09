# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class ETLConfiguration(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        from_time: int = None,
        lang: str = None,
        logstore: str = None,
        parameters: Dict[str, Any] = None,
        role_arn: str = None,
        script: str = None,
        sinks: List[main_models.ETLConfigurationSink] = None,
        to_time: int = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        # This parameter is required.
        self.from_time = from_time
        self.lang = lang
        # This parameter is required.
        self.logstore = logstore
        self.parameters = parameters
        # This parameter is required.
        self.role_arn = role_arn
        # This parameter is required.
        self.script = script
        # This parameter is required.
        self.sinks = sinks
        # This parameter is required.
        self.to_time = to_time

    def validate(self):
        if self.sinks:
            for v1 in self.sinks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id

        if self.access_key_secret is not None:
            result['accessKeySecret'] = self.access_key_secret

        if self.from_time is not None:
            result['fromTime'] = self.from_time

        if self.lang is not None:
            result['lang'] = self.lang

        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.parameters is not None:
            result['parameters'] = self.parameters

        if self.role_arn is not None:
            result['roleArn'] = self.role_arn

        if self.script is not None:
            result['script'] = self.script

        result['sinks'] = []
        if self.sinks is not None:
            for k1 in self.sinks:
                result['sinks'].append(k1.to_map() if k1 else None)

        if self.to_time is not None:
            result['toTime'] = self.to_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')

        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')

        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')

        if m.get('lang') is not None:
            self.lang = m.get('lang')

        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        if m.get('script') is not None:
            self.script = m.get('script')

        self.sinks = []
        if m.get('sinks') is not None:
            for k1 in m.get('sinks'):
                temp_model = main_models.ETLConfigurationSink()
                self.sinks.append(temp_model.from_map(k1))

        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')

        return self

