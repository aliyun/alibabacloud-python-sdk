# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class SubmitAsyncSqlParams(DaraModel):
    def __init__(
        self,
        extensions: main_models.SubmitAsyncSqlParamsExtensions = None,
        from_: int = None,
        logstore: str = None,
        query: str = None,
        to: int = None,
    ):
        self.extensions = extensions
        # This parameter is required.
        self.from_ = from_
        # This parameter is required.
        self.logstore = logstore
        # This parameter is required.
        self.query = query
        # This parameter is required.
        self.to = to

    def validate(self):
        if self.extensions:
            self.extensions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extensions is not None:
            result['extensions'] = self.extensions.to_map()

        if self.from_ is not None:
            result['from'] = self.from_

        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.query is not None:
            result['query'] = self.query

        if self.to is not None:
            result['to'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extensions') is not None:
            temp_model = main_models.SubmitAsyncSqlParamsExtensions()
            self.extensions = temp_model.from_map(m.get('extensions'))

        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('to') is not None:
            self.to = m.get('to')

        return self

class SubmitAsyncSqlParamsExtensions(DaraModel):
    def __init__(
        self,
        max_run_time: int = None,
        power_sql: bool = None,
    ):
        self.max_run_time = max_run_time
        self.power_sql = power_sql

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_run_time is not None:
            result['maxRunTime'] = self.max_run_time

        if self.power_sql is not None:
            result['powerSql'] = self.power_sql

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxRunTime') is not None:
            self.max_run_time = m.get('maxRunTime')

        if m.get('powerSql') is not None:
            self.power_sql = m.get('powerSql')

        return self

