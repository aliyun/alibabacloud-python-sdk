# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class Index(DaraModel):
    def __init__(
        self,
        keys: Dict[str, main_models.IndexKey] = None,
        line: main_models.IndexLine = None,
        log_reduce: bool = None,
        log_reduce_black_list: List[str] = None,
        log_reduce_white_list: List[str] = None,
        max_text_len: int = None,
        scan_index: bool = None,
    ):
        self.keys = keys
        self.line = line
        self.log_reduce = log_reduce
        self.log_reduce_black_list = log_reduce_black_list
        self.log_reduce_white_list = log_reduce_white_list
        self.max_text_len = max_text_len
        self.scan_index = scan_index

    def validate(self):
        if self.keys:
            for v1 in self.keys.values():
                 if v1:
                    v1.validate()
        if self.line:
            self.line.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['keys'] = {}
        if self.keys is not None:
            for k1, v1 in self.keys.items():
                result['keys'][k1] = v1.to_map() if v1 else None

        if self.line is not None:
            result['line'] = self.line.to_map()

        if self.log_reduce is not None:
            result['log_reduce'] = self.log_reduce

        if self.log_reduce_black_list is not None:
            result['log_reduce_black_list'] = self.log_reduce_black_list

        if self.log_reduce_white_list is not None:
            result['log_reduce_white_list'] = self.log_reduce_white_list

        if self.max_text_len is not None:
            result['max_text_len'] = self.max_text_len

        if self.scan_index is not None:
            result['scan_index'] = self.scan_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.keys = {}
        if m.get('keys') is not None:
            for k1, v1 in m.get('keys').items():
                temp_model = main_models.IndexKey()
                self.keys[k1] = temp_model.from_map(v1)

        if m.get('line') is not None:
            temp_model = main_models.IndexLine()
            self.line = temp_model.from_map(m.get('line'))

        if m.get('log_reduce') is not None:
            self.log_reduce = m.get('log_reduce')

        if m.get('log_reduce_black_list') is not None:
            self.log_reduce_black_list = m.get('log_reduce_black_list')

        if m.get('log_reduce_white_list') is not None:
            self.log_reduce_white_list = m.get('log_reduce_white_list')

        if m.get('max_text_len') is not None:
            self.max_text_len = m.get('max_text_len')

        if m.get('scan_index') is not None:
            self.scan_index = m.get('scan_index')

        return self

class IndexLine(DaraModel):
    def __init__(
        self,
        case_sensitive: bool = None,
        chn: bool = None,
        exclude_keys: List[str] = None,
        include_keys: List[str] = None,
        token: List[str] = None,
    ):
        self.case_sensitive = case_sensitive
        self.chn = chn
        self.exclude_keys = exclude_keys
        self.include_keys = include_keys
        # This parameter is required.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive

        if self.chn is not None:
            result['chn'] = self.chn

        if self.exclude_keys is not None:
            result['exclude_keys'] = self.exclude_keys

        if self.include_keys is not None:
            result['include_keys'] = self.include_keys

        if self.token is not None:
            result['token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')

        if m.get('chn') is not None:
            self.chn = m.get('chn')

        if m.get('exclude_keys') is not None:
            self.exclude_keys = m.get('exclude_keys')

        if m.get('include_keys') is not None:
            self.include_keys = m.get('include_keys')

        if m.get('token') is not None:
            self.token = m.get('token')

        return self

