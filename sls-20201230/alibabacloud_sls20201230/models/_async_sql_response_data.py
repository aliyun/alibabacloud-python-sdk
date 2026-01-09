# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class AsyncSqlResponseData(DaraModel):
    def __init__(
        self,
        async_sql_meta_pb: main_models.AsyncSqlResponseDataAsyncSqlMetaPB = None,
        error_code: str = None,
        error_message: str = None,
        id: str = None,
        rows: List[List[str]] = None,
        state: str = None,
    ):
        self.async_sql_meta_pb = async_sql_meta_pb
        self.error_code = error_code
        self.error_message = error_message
        # This parameter is required.
        self.id = id
        self.rows = rows
        # This parameter is required.
        self.state = state

    def validate(self):
        if self.async_sql_meta_pb:
            self.async_sql_meta_pb.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_sql_meta_pb is not None:
            result['AsyncSqlMetaPB'] = self.async_sql_meta_pb.to_map()

        if self.error_code is not None:
            result['error_code'] = self.error_code

        if self.error_message is not None:
            result['error_message'] = self.error_message

        if self.id is not None:
            result['id'] = self.id

        if self.rows is not None:
            result['rows'] = self.rows

        if self.state is not None:
            result['state'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncSqlMetaPB') is not None:
            temp_model = main_models.AsyncSqlResponseDataAsyncSqlMetaPB()
            self.async_sql_meta_pb = temp_model.from_map(m.get('AsyncSqlMetaPB'))

        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')

        if m.get('error_message') is not None:
            self.error_message = m.get('error_message')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('rows') is not None:
            self.rows = m.get('rows')

        if m.get('state') is not None:
            self.state = m.get('state')

        return self



class AsyncSqlResponseDataAsyncSqlMetaPB(DaraModel):
    def __init__(
        self,
        cpu_cores: int = None,
        cpu_sec: float = None,
        elapsed_milli: int = None,
        keys: List[str] = None,
        processed_rows: int = None,
        progress: str = None,
        result_rows: int = None,
    ):
        self.cpu_cores = cpu_cores
        self.cpu_sec = cpu_sec
        self.elapsed_milli = elapsed_milli
        self.keys = keys
        self.processed_rows = processed_rows
        self.progress = progress
        self.result_rows = result_rows

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_cores is not None:
            result['cpu_cores'] = self.cpu_cores

        if self.cpu_sec is not None:
            result['cpu_sec'] = self.cpu_sec

        if self.elapsed_milli is not None:
            result['elapsed_milli'] = self.elapsed_milli

        if self.keys is not None:
            result['keys'] = self.keys

        if self.processed_rows is not None:
            result['processed_rows'] = self.processed_rows

        if self.progress is not None:
            result['progress'] = self.progress

        if self.result_rows is not None:
            result['result_rows'] = self.result_rows

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu_cores') is not None:
            self.cpu_cores = m.get('cpu_cores')

        if m.get('cpu_sec') is not None:
            self.cpu_sec = m.get('cpu_sec')

        if m.get('elapsed_milli') is not None:
            self.elapsed_milli = m.get('elapsed_milli')

        if m.get('keys') is not None:
            self.keys = m.get('keys')

        if m.get('processed_rows') is not None:
            self.processed_rows = m.get('processed_rows')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        if m.get('result_rows') is not None:
            self.result_rows = m.get('result_rows')

        return self

